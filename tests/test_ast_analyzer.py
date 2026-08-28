from src.review_assistant.parser.python_parser import PythonParser
from src.review_assistant.analyzers.python_ast_analyzer import PythonASTAnalyzer
from src.review_assistant.rules.security import check_sql_injection


def test_hardcoded_secrets():

    code = """
import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

user_id = input("Enter ID: ")

# Should be detected
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# Should be detected
cursor.execute("SELECT * FROM users WHERE id = " + user_id)

# Should NOT be detected
cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_id,)
)
"""

    parser = PythonParser()
    tree = parser.parse(code)

    analyzer = PythonASTAnalyzer()
    result = analyzer.analyze(tree)
    print("FUNCTION CALLS:")
    print(result.get("function_calls"))
    findings = check_sql_injection(result)

    print("FINDINGS:")

    for finding in findings:
        print(finding)

    
    


if __name__ == "__main__":
    test_hardcoded_secrets()
