import ast
import astunparse
from typing import List, Optional

def compile(file: str, output: str) -> None:
    with open(file, 'r') as f:
        source = f.read()
    compiled = compile_source(source)
    with open(output, 'w') as f:
        f.write(compiled)

def compile_source(source: str) -> str:
    return astunparse.unparse(compile_ast(ast.parse(source)))

def compile_ast(node: ast.AST) -> ast.AST:
    return Compiler().visit(node)

class Compiler(ast.NodeTransformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> Optional[ast.AST]:
        self.visit(node.args)
        for child in node.body:
            self.visit(child)
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
        if node.module == 'typing' or node.module == 'mypy_extensions':
            return None
        return node

    def visit_Assign(self, node: ast.Assign) -> Optional[ast.AST]:
        if isinstance(node.targets[0], ast.Name) and isinstance(node.value, ast.Call) and \
           isinstance(node.value.func, ast.Name) and node.value.func.id == 'TypedDict':
            return ast.parse('class %s: pass' % node.targets[0].id)
        return node

    def visit_AnnAssign(self, node: ast.AnnAssign) -> Optional[ast.AST]:
        return None

    def visit_JoinedStr(self, node: ast.JoinedStr) -> Optional[ast.AST]:
        elements = []
        for value in node.values:
            if isinstance(value, ast.FormattedValue):
                elements.append(ast.Call(ast.Name('str'), [value.value], []))
            elif isinstance(value, ast.Str):
                elements.append(value)
            else:
                elements.append(ast.Call(ast.Name('str'), [value]))
        return ast.Call(
            ast.Attribute(
                ast.Str(''),
                'join'), [
                ast.List(elements)], [])

