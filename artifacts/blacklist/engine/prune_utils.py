import ast


class RemoveExprTransformer(ast.NodeTransformer):
    def visit_Expr(self, node):
        # Return None to remove the node
        return None
