# This is the python specific parser, it will take python source code and converts it into python AST
# See notes for more information about Abstract Syntax Tree (AST).

import ast

from .base_parser import BaseParser



class PythonParser(BaseParser):

    def parse(self, code):

        try:

            tree = ast.parse(code) # build the AST tree

            return tree

        except SyntaxError as e:
            raise ValueError(f"Unable to parse Python code {e}")



