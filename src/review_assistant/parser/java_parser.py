# This is the java specific parser, it will take java source code and converts it into python AST


from .base_parser import BaseParser


class JavaParser(BaseParser):

    def parse(self, code):

        raise NotImplementedError("Java parser is not implemented yet.")



