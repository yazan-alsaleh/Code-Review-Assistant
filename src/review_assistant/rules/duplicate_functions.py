# This rule about duplicated functions 

from ..finding import Finding


def check_duplicate_functions(ast_result):


    findings = []

    functions = ast_result["functions"]

    for i in range(len(functions)): # first pointer
        for j in range(i + 1, len(functions)): # second pointer 
            first = functions[i] # get the first function
            second = functions[j] # get the second function

            if first.get("body") == second.get("body"): # they are similar 
                findings.append(
                    Finding(
                        rule = "duplicate-function",
                        message = (
                            f"Function '{second['name']}' duplicates "
                            f"function '{first['name']}'."
                        ),
                        line = second["line"],
                        severity = "warning",
                        category = "quality"
                    )
                )


    return findings


