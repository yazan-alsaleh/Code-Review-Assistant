from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.reviewer import Reviewer

def test_complexity_code():

    code = """
import os

def test():
    eval("print('hello')")
    exec("x = 10")
    os.system("dir")
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




