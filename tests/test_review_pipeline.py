import ast

from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.reviewer import Reviewer



code = """
import math
import pandas

def calculate(self, value):
    if value > 5:
        return math.sqrt(value)

x = 10
print(x)
"""

tree = ast.parse(code)

analyzer = PythonASTAnalyzer()
ast_result = analyzer.analyze(tree)


reviewer = Reviewer()
findings = reviewer.review(ast_result)


print("AST RESULT:")
print(ast_result)

print("\n REVIEW FINDINGS:")
print(findings)

