from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer

code = """
import math
import pandas

x = 10
name = "Yazan"


class Calculator:

    def calculate(self, value):

        if value > 5:
            return math.sqrt(value)

        return value


for i in range(10):
    print(i)
"""


parser = PythonParser()

tree = parser.parse(code)
print("AST:")


analyzer = PythonASTAnalyzer()

result = analyzer.analyze(tree)

print("RESULT: ")
print(result)


