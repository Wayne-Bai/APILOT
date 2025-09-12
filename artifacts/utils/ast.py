import builtins
import ast
import json

##### Called Functions Extractor #####
class ASTNodeEncoder(json.JSONEncoder):
    """ Custom JSON Encoder for ast nodes """
    def default(self, obj):
        if isinstance(obj, ast.AST):
            fields = {field: getattr(obj, field) for field in obj._fields}
            fields['type'] = type(obj).__name__
            return fields
        return json.JSONEncoder.default(self, obj)
    
def ast_to_dict(node):
    """ Convert ast node to dictionary format """
    if isinstance(node, ast.AST):
        node_dict = {'type': type(node).__name__}
        for field, value in ast.iter_fields(node):
            node_dict[field] = ast_to_dict(value)
        return node_dict
    elif isinstance(node, list):
        return [ast_to_dict(n) for n in node]
    else:
        return node
    
def extract_functions_and_attributes_with_parents(ast_json, package):
    functions = []
    attributes = []
    packages = []
    variable_types = {}  # Dictionary to track the types of variables
    built_in_functions = dir(builtins)

    def recurse(node, parent_type=None):
        node_type = node.get("type")

        if node_type == "Import":
            for name in node.get("names", []):
                if name.get("asname"):
                    packages.append((name["name"], name["asname"]))
                else:
                    packages.append((name["name"], None))
                    
        elif node_type == "ImportFrom":
            module = node.get("module")
            if module:
                packages.append((module, node.get("level")))
                for name in node.get("names", []):
                    if name.get("name"):
                        functions.append((name["name"], module))
            
        if node_type == "Assign":
            targets = node.get("targets", [])
            value = node.get("value")
            if value.get("type") == "Call":
                called_func_name, _ = extract_name_and_parent(value.get("func"))
                # Assuming the assignment type is the function's return type (simplification)
                for target in targets:
                    if target.get("type") == "Name":
                        variable_types[target["id"]] = called_func_name

        # Extract function calls
        if node_type == "Call":
            func = node.get("func")
            if func:
                func_name, parent = extract_name_and_parent(func)
                if func_name in built_in_functions:
                    parent = None
                # Infer the type if parent is a variable
                else:
                    parent_type = variable_types.get(parent, parent)
                functions.append((func_name, parent_type))

        # Extract attribute accesses
        if node_type == "Attribute":
            attr_name, parent = extract_name_and_parent(node)
            # Infer the type if parent is a variable
            parent_type = variable_types.get(parent, parent)
            attributes.append((attr_name, parent_type))

        if node_type == "Expr":
            value = node.get("value")
            if value:
                recurse(value, parent_type)

        # Recursively handle children nodes
        for key, value in node.items():
            if isinstance(value, dict):
                recurse(value, parent_type)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        recurse(item, parent_type)

    def extract_name_and_parent(node):
        """ Extract the last attribute name and determine the parent type from the path """
        if 'attr' in node.keys():
            functions.append((node.get("attr"), None))
        current_node = node
        last_attr = None
        parent_type = None
        # Traverse the attribute chain to the last attribute
        while current_node and current_node.get("type") == "Attribute":
            last_attr = current_node['attr']
            current_node = current_node.get("value")

        # Determine the direct parent
        if current_node and current_node.get("type") == "Name":
            parent_type = current_node['id']
        
        return last_attr or (current_node.get("id") if current_node else None), parent_type

    recurse(ast_json)
    functions = functions + attributes

    package_asname = [pair[1] for pair in packages if pair[1] is not None]

    for i, (func, parent) in enumerate(functions):
        if parent in package_asname:
            package_fullname = next((x for x, y in packages if y == parent), None)
            if package_fullname == package:
                functions[i] = (func, 'Module')
        elif parent == package:
            functions[i] = (func, 'Module')

    unique_dict = {}
    for pair in functions:
        if pair[0] not in unique_dict:
            unique_dict[pair[0]] = pair[1]

    functions = list(unique_dict.items())

    return functions, packages
