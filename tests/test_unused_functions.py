from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.unused_functions import check_unused_functions


def test_unused_functions():

    code = """
def calculate(x):
    return x * 2

def unused_function():
    print("Hello")

result = calculate(5)
print(result)
"""

    parser = PythonParser() # create the parser object
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    findings = check_unused_functions(ast_result)

    print("AST RESULT:")
    print(ast_result)

    print("\nFINDINGS:")
    print(findings)


if __name__ == "__main__":
    test_unused_functions()