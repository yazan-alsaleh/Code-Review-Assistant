from src.review_assistant.parser.parser_factory import ParserFactory
import ast

def test_python_parser():

    code = """
def add(a, b):
        return a + b
"""

    parser = ParserFactory.get_parser("python")


    tree = parser.parse(code)

    print(ast.dump(tree, indent=4))


if __name__ == "__main__":
    test_python_parser()

