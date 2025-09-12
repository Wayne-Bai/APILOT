import os
from datetime import datetime
import sys
import re
import ast
from typing import Dict
from prune_utils import RemoveExprTransformer


# from ast2json import ast2json
# import astunparse

"""
  Module: AST manager
  Function: AST operation per file source
"""


class ASTManager:
    def __init__(self) -> None:
        return

    """
    check whether a python file has a _all_ flag
    """

    def hasAllFlag(self, file_source) -> bool:
        tree = ast.parse(file_source)

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if "id" in node.targets[0].__dict__.keys():
                    if node.targets[0].id == "__all__":
                        return True

        return False

    """
    prune the line information of the ast tree
    """

    def ASTprune(self, tree) -> object:

        tree = RemoveExprTransformer().visit(tree)

        for node in ast.walk(tree):
            if hasattr(node, "col_offset"):
                delattr(node, "col_offset")
            if hasattr(node, "lineno"):
                delattr(node, "lineno")
            if hasattr(node, "end_col_offset"):
                delattr(node, "end_col_offset")
            if hasattr(node, "end_lineno"):
                delattr(node, "end_lineno")

        return tree

    """
    collect the class definition in the ast tree
    """

    def collectClass(self, file_source) -> list:
        class_list = []
        original_tree = ast.parse(file_source)
        tree = self.ASTprune(original_tree)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_list.append(str(node.name))

        return class_list

    """
    collect the function definition in the ast tree
    """

    def collectFunction(self, file_source) -> list:
        func_list = []
        original_tree = ast.parse(file_source)
        tree = self.ASTprune(original_tree)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_list.append(str(node.name))

        return func_list

    """
    collect the function and class definition in the ast tree
    """

    def collectFuncAndClass(self, file_source) -> list:
        func_class_list = []
        original_tree = ast.parse(file_source)
        tree = self.ASTprune(original_tree)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
                func_class_list.append(str(node.name))

        return func_class_list

    """
    get the external apis in the ast tree
    """

    def getExternalApis(self, file_source) -> list:
        external_apis = []
        original_tree = ast.parse(file_source)
        tree = self.ASTprune(original_tree)

        # find all apis in the __all__
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if "id" in node.targets[0].__dict__.keys():
                    if node.targets[0].id == "__all__":
                        if isinstance(node.value, ast.List):
                            for i in node.value.elts:
                                external_apis.append(str(i.value))

        # find all the class definition in the source
        class_def = self.collectClass(file_source)

        # find the class definition in the external
        external_class = set(class_def) & set(external_apis)

        # append the children node
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for class_name in external_class:
                    if node.name == class_name:
                        # append all its function
                        for body_node in node.body:
                            if isinstance(body_node, ast.FunctionDef):
                                external_apis.append(str(body_node.name))
        return external_apis

    """
    find the key word deprecation in the current file
    """

    def findDeprecated(self, file_source, path) -> list:
        deprecateList = []
        original_tree = ast.parse(file_source)
        tree = self.ASTprune(original_tree)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if "deprecate" in node.name or "deprecation" in node.name:
                    deprecate_map = {}
                    deprecate_map["func_name"] = str(node.name)
                    deprecate_map["path"] = path
                    deprecate_map["parent"] = self.findParent(file_source, node.name)
                    deprecateList.append(deprecate_map)
        return deprecateList

    """
    given a function name and src tree
    extract the function ast tree
    """

    def getFunctionAst(self, func_name, src) -> object:
        # Parse the source code into an AST
        original_tree = ast.parse(src)
        tree = self.ASTprune(original_tree)

        # Find the function definition in the AST
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                # Return the AST node for the function
                return node

        # If the function is not found, return None
        return None

    """
    compare two trees, find the parameter changed apis
    """

    def findParamChanged(
        self, api_name, source_old, source_new, api_path
    ) -> Dict[str, str]:
        para_map = {}
        func_ast_old = self.getFunctionAst(api_name, source_old)
        func_ast_new = self.getFunctionAst(api_name, source_new)

        if func_ast_old == None or func_ast_new == None:
            return None

        #  Extract parameters
        old_params = [arg.arg for arg in func_ast_old.args.args]
        new_params = [arg.arg for arg in func_ast_new.args.args]

        # Compare parameters

        # if they are the same return none
        if old_params == new_params:
            return None

        # else return a map of param change
        para_map["func_name"] = api_name
        para_map["path"] = api_path
        para_map["parent"] = self.findParent(source_new, api_name)
        para_map["old"] = old_params
        para_map["new"] = new_params

        return para_map

    """
    compare if two node has the same type in return info map 
    """

    def compare_return_types(self, return_info1, return_info2):
        # Parse symbols back into AST nodes
        parsed_symbols1 = [
            ast.parse(symbol).body[0].value if symbol != "None" else None
            for symbol in return_info1["symbols"]
        ]
        parsed_symbols2 = [
            ast.parse(symbol).body[0].value if symbol != "None" else None
            for symbol in return_info2["symbols"]
        ]

        # Compare the types of the parsed symbols
        for sym1, sym2 in zip(parsed_symbols1, parsed_symbols2):
            if type(sym1) != type(sym2):
                return False  # Found different types
        return True  # All types are the same

    """
    get the return information for a function
    """


    def getReturnInfo(self, ast_node) -> object:
        return_info = {"num_returns": 0, "symbols": []}

        if isinstance(ast_node, ast.FunctionDef):
            for stmt in ast_node.body:
                if isinstance(stmt, ast.Return):
                    return_info["num_returns"] += 1
                    if stmt.value is None:
                        return_info["symbols"].append("None")
                    else:
                        return_info["symbols"].append(ast.dump(stmt.value))

        return return_info

    """
    compare two trees, find return changed apis in the same file
    """

    def findReturnChanged(
        self, api_name, source_old, source_new, path
    ) -> Dict[str, str]:
        return_change = {}
        func_ast_old = self.getFunctionAst(api_name, source_old)
        func_ast_new = self.getFunctionAst(api_name, source_new)

        if func_ast_old == None or func_ast_new == None:
            return None

        old_return = self.getReturnInfo(func_ast_old)
        new_return = self.getReturnInfo(func_ast_new)

        if old_return == new_return:
            return None

        # compare the return value nums
        if old_return["num_returns"] != new_return["num_returns"]:
            return_change["func_name"] = api_name
            return_change["path"] = path
            return_change["parent"] = self.findParent(source_new, api_name)
            return_change["old"] = old_return["num_returns"]
            return_change["new"] = new_return["num_returns"]
            # num of return changed
            # return_change["likelihood"] = "high"

        # compare the return value symbols
        if old_return["symbols"] != new_return["symbols"]:
            return_change["func_name"] = api_name
            return_change["path"] = path
            return_change["parent"] = self.findParent(source_new, api_name)
            return_change["old"] = old_return["symbols"]
            return_change["new"] = new_return["symbols"]
            # if self.compare_return_types(old_return, new_return):
            #   return_change["likelihood"] = "high"
            # else:
            #   return_change["likelihood"] = "normal"

        return return_change

    """
    find the parent node for a given node
    """

    def findParent(self, file_source, api_name) -> str:

        tree = ast.parse(file_source)
        # get its parent
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.FunctionDef):
                    if isinstance(node, ast.ClassDef):
                        if child.name == api_name:
                            return node.name

        return "Module"
