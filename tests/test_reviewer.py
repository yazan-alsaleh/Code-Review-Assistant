from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.reviewer import Reviewer


def test_reviewer():

    code = """
import math

def calculate(x):
    return x * 2

def unused_function():
    print("Hello")

unused_variable = 100

result = calculate(5)

print(result)
"""

    parser = PythonParser()
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    reviewer = Reviewer()

    findings = reviewer.review(ast_result)

    print("AST RESULT:")
    print(ast_result)

    print("\nFINDINGS:")

    for finding in findings:
        print(finding)


if __name__ == "__main__":
    test_reviewer()