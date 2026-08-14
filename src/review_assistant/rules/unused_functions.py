# this file will has the unused functions in the source code



def check_unused_functions(ast_result):

    findings = []

    functions = ast_result["functions"]
    name_usage = ast_result["name_usage"]


    used_names = {
        usage["name"]
        for usage in name_usage
    }


    print("FUNCTIONS:", functions)
    print("USED NAMES:", used_names)


    for my_function in functions:
        name = my_function["name"]

        print("CHECKING:", name)
        print("IS USED:", name in used_names)

        if name not in used_names:

            findings.append({
                "rule": "unused-function",
                "message": f"Function '{name}' is defined but never used.",
                "line": my_function["line"]
            })

    return findings



