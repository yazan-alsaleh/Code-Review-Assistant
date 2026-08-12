from src.review_assistant.rules import check_unused_imports

ast_result = {
     "imports": [
        {
            "name": "math",
            "line": 2
        },
        {
            "name": "pandas",
            "line": 3
        }
    ],
    "name_usage": [
        {
            "name": "print",
            "line": 10
        }
    ]
}

findings = check_unused_imports(ast_result)

print(findings)


