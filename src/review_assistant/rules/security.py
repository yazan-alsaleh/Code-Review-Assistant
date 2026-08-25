# This file is about the security of the code

from ..finding import Finding
import ast




def check_security(ast_result):

    findings = []


    # eval() and exec() takes a string and executes it as Python code
    # os.system() runs command on the OS
    dangerous_functions = {
        "eval": "Use of eval() can lead to arbitrary code execution.",
        "exec": "Use of exec() can lead to arbitrary code execution.",
        "system": "Use of os.system() can lead to command injection.",
        "subprocess.call": "Use of subprocess.call() can lead to command injection.",
        "subprocess.run": "Use of subprocess.run() may be dangerous when used with shell = True."
    }

    print("FUNCTION CALLS:", ast_result["function_calls"])


    for call in ast_result.get("function_calls", []): # for each function call from in the code

        name = call["name"] # get the function name

        if name == "subprocess.run": # If the function is subprocess.run, check whether it uses shell=True. Only then report it.
        # The reason is that subprocess.run() itself isn't necessarily dangerous. shell=True is the important condition we're checking.
            if call.get("shell") is True:
                findings.append(
                    Finding(
                        rule = "security-dangerous-call",
                        message = "Use of subprocess.run() with shell = True can lead to command injection",
                        line = call["line"],
                        severity = "error",
                        category = "security"
                    )
                )

        elif name in dangerous_functions: # if the function in the dangerous functions type
            findings.append(
                Finding(
                    rule = "security-dangerous-call",
                    message = dangerous_functions[name],
                    line = call["line"],
                    severity = "error",
                    category = "security"
                )
            )


    return findings


def check_hardcoded_secrets(ast_result):

    findings = []

    secret_keywords = [ # words / variables that might have a secret value
        "password",
        "passwd",
        "pwd",
        "secret",
        "api_key",
        "apikey",
        "token",
        "access_token",
        "auth_token",
        "private_key",
        "client_secret"
    ]


    for variable in ast_result["variables"]: # for each variable in the code
        name = variable["name"] # get the variable name

        for keyword in secret_keywords: # for each keyword in secret_keywords

            if keyword in name.lower(): # to check if they match. in used to check whether one string exists inside another string.
                # so even if part of the keyword exits in name it will be detected like: "password" and "user_password"

                if isinstance(variable.get("value"), str):

                    findings.append(
                        Finding(
                            rule = "security-hardcoded-secret",
                            message = f"Possible hardcoded secret found in variable '{name}'",
                            line = variable["line"],
                            severity = "error",
                            category = "security" 
                        )
                    )

    return findings


def check_sql_injection(ast_result):

    findings = []

    sql_methods = ["execute", "executemany"]
    # Those are Python methods used to send SQL queries to a database


    for call in ast_result.get("function_calls", []):
        if call["name"] in sql_methods:

            node = call["node"]

            if not node.args:
                continue

            query = node.args[0] # means the first argument passed to execute(), which should normally be the SQL query.

        # For the f string like: cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        if isinstance(query, ast.JoinedStr):
            findings.append(
                Finding(
                    rule = "security-sql-injection",
                    message = "Possible SQL injection detected: SQL query executed dynamically",
                    line = call["line"],
                    severity = "error",
                    category = "security"
                )
            )

        # ast.BinOp + ast.Add = string concatenation like: cursor.execute("SELECT * FROM users WHERE id = " + user_id)
        elif isinstance(query, ast.BinOp) and isinstance(query.op, ast.Add):
            findings.append(
                Finding(
                    rule = "security-sql-injection",
                    message = "Possible SQL injection: SQL query is built using string concatenation",
                    line = call["line"],
                    severity = "error",
                    category = "security"
                )
            )



    return findings


