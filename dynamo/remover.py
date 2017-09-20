import ast
import astunparse
from typing import List, Optional

def remove_annotations_from_file(file: str, output: str) -> None:
    with open(file, 'r') as f:
        source = f.read()
    removed = remove_annotations(source)
    with open(output, 'w') as f:
        f.write(removed)

def remove_annotations(source: str) -> str:
    return astunparse.unparse(remove_annotations_in_ast(ast.parse(source)))

def remove_annotations_in_ast(node: ast.AST) -> ast.AST:
    return Remover().visit(node)

class Remover(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> Optional[ast.AST]:
        self.visit(node.args)
        if node.returns is not None:
            node.returns = None
        return node

    def visit_arg(self, node: ast.arg) -> Optional[ast.AST]:
        if node.annotation is not None:
            node.annotation = None
        return node

    def visit_alias(self, node: ast.alias) -> Optional[ast.AST]:
        if node.name == 'typing':
            return None
        return node

    def visit_ImportFrom(self, node: ast.ImportFrom) -> Optional[ast.AST]:
        if node.module == 'typing':
            return None
        return node


    