from src.review_assistant.reviewer import Reviewer


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


reviewer = Reviewer()


findings = reviewer.review(ast_result)
print(findings)


