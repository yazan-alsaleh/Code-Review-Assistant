from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.unused_variables import check_unused_variables


def test_unused_variables():

    code = """
x = 10
y = 20

print(x)
"""

    parser = PythonParser()
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    findings = check_unused_variables(ast_result)

    print("AST RESULT:")
    print(ast_result)

    print("\nFINDINGS:")
    print(findings)


if __name__ == "__main__":
    test_unused_variables()