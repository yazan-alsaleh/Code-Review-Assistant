# The goal is to detect functions that are becoming too complicated to understand or maintain.


from ..finding import Finding


def check_complexity(ast_result):

    findings = []

    for function in ast_result["functions"]: # loop throug each function in the AST tree

        complexity = function["complexity"] # get the complexity for each function

        if complexity > 5:

            findings.append(
                Finding(
                    rule="complexity",
                    message=(
                        f"Function '{function['name']}' "
                        f"has high complexity ({complexity})."
                    ),
                    line=function["line"],
                    severity="warning",
                    category="maintainability"
                )
            )

    return findings




