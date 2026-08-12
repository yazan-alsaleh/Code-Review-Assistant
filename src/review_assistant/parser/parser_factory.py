# The factory will decide which parser should I use?

from .python_parser import PythonParser
from .java_parser import JavaParser
from .javascript_parser import JavaScriptParser


# Now the rest of the application doesn't need to know about individual parser classes.
class ParserFactory:


    @staticmethod 
    def get_parser(language):

        if language == "python":
            return PythonParser()
        elif language == "java":
            return JavaParser()
        elif language == "javascript":
            return JavaScriptParser()
        else:
            raise ValueError(f"Unsupported language: {language}")



