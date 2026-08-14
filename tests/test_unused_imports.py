from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.unused_imports import check_unused_imports


def test_unused_imports():

    code = """
import math
import pandas 
print(math.sqrt(4))
"""

    parser = PythonParser() # create the parser object
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    findings = check_unused_imports(ast_result)

    print("AST RESULT:")
    print(ast_result)

    print("\nFINDINGS:")
    print(findings)


if __name__ == "__main__":
    test_unused_imports()