from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer

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

result = analyzer.analyze(tree)

print("RESULT: ")
print(result)


