from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.complexity import check_complexity

def test_complexity_code():

    code = """
def calculate(x, y):

    if x > 10:
        print(x)

    if y > 20:
        print(y)

    for i in range(x):
        print(i)

    while x > 0:
        x -= 1
"""


    parser = PythonParser()

    tree = parser.parse(code)
    print("AST:")


    analyzer = PythonASTAnalyzer()
    ast_result = analyzer.analyze(tree)

    findings = check_complexity(ast_result)

    print("AST RESULT:")
    print(ast_result)

    print("\nFINDINGS:")

    for finding in findings:
        print(finding)


if __name__ == "__main__":
    test_complexity_code()




