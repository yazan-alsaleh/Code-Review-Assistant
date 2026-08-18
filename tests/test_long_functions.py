from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.long_functions import check_long_functions


def test_long_function():

    code = """
def short_function():
    return 10


def long_function():
""" + "\n".join(["    x = 10"] * 55) + """
    return x
"""

    parser = PythonParser()
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    print("AST RESULT:")
    print(ast_result)

    findings = check_long_functions(ast_result)

    print("\nFINDINGS:")

    for finding in findings:
        print(finding)


if __name__ == "__main__":
    test_long_function()