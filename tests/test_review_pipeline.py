import ast
from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.reviewer import Reviewer


def test_complexity_code():

    code = """
import math

unused_variable = 10

def unused_function():
    pass

def calculate(x, y):
    if x > 0:
        if y > 0:
            if x > y:
                print("A")
            else:
                print("B")
        else:
            print("C")
    else:
        print("D")

    for i in range(x):
        print(i)

    while y > 0:
        y -= 1

    return x + y
"""


    parser = PythonParser()
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    print("AST RESULT:")
    print(ast_result)

    reviewer = Reviewer()

    findings = reviewer.review(ast_result)

    print("\nFINDINGS:")

    for finding in findings:
        print(finding)


if __name__ == "__main__":
    test_complexity_code()


