from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.duplicate_functions import check_duplicate_functions


def test_duplicate_functions():

    code = """
def calculate_area(width, height):
    result = width * height
    print(result)
    return result


def calculate_size(width, height):
    result = width * height
    print(result)
    return result
"""

    parser = PythonParser()
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    findings = check_duplicate_functions(ast_result)

    print("FINDINGS:")

    for finding in findings:
        print(finding.to_dict())


if __name__ == "__main__":
    test_duplicate_functions()