# this file will has the unused variables in the source code


def check_unused_variables(ast_result):

    findings = []

    variables = ast_result["variables"]
    name_usage = ast_result["name_usage"] # used things in the source code that come from AST analyzer

    used_names = { # get the used names from name_usage (from AST analyzer) because there are functions, imports, etc...
        usage["name"]
        for usage in name_usage
    }

    for variable in variables: # each variable that was assigned
        name = variable["name"] # get the variable name

        if name not in used_names:

            findings.append({
                "rule": "unused-variable",
                "message": f"Variable '{name}' is assigned but never used.",
                "line": variable["line"]
            })

    return findings



