from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.reviewer import Reviewer


def test_reviewer():

    code = """
API_KEY = "123456"
password = "myPassword"
name = "Yazan"
age = 22
API_KEY_2 = get_api_key()
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
        print(finding.to_dict())


if __name__ == "__main__":
    test_reviewer()