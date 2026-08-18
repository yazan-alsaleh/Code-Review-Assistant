# This file is about the security of the code

from ..finding import Finding

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



    for call in ast_result.get("function_calls", []): # for each function call from in the code

        name = call["name"] # get the function name

        if name in dangerous_functions: # if the function in the dangerous functions type
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


