# This rule about long functions

from ..finding import Finding


MAX_FUNCTION_LINES = 50


def check_long_functions(ast_result):

    findings = []

    for function in ast_result["functions"]: # for each function in the tree

        function_name = function["name"] # Get the function name

        start_line = function["line"] # Get the start line of the function

        end_line = function["end_line"] # Get the end line of the function


        function_length = end_line - start_line + 1 # Calculate the function length 
        # +1 here because if the start and the end at the same line it will be 0 which is not correct its 1

        if function_length > MAX_FUNCTION_LINES: # if its a big function
            findings.append(
                Finding(
                    rule = "long-function",
                    message = (
                        f"Function '{function_name}' is too long "
                        f"({function_length} lines)."
                    ),
                    line = start_line,
                    severity = "warning",
                    category = "maintainability",
                )
            )


    return findings


