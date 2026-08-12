# This is the javascript specific parser, it will take javascript source code and converts it into python AST


from .base_parser import BaseParser


class JavaScriptParser(BaseParser):

    def parse(self, code):

        raise NotImplementedError("JavaScript parser is not implemented yet.")


