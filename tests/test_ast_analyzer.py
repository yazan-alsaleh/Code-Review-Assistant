from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.security import check_hardcoded_secrets


def test_hardcoded_secrets():

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
    result = analyzer.analyze(tree)

    findings = check_hardcoded_secrets(result)

    print("FINDINGS:")

    for finding in findings:
        print(finding)


if __name__ == "__main__":
    test_hardcoded_secrets()
