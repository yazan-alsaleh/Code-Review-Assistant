# this file will has the review rules 




def check_unused_imports(ast_result):

    findings = []

    imports = ast_result["imports"] # get the imports array from ast analyzer
    name_usage = ast_result["name_usage"] # get the used names array for ast analyzer

    used_names = set()

    for usage in name_usage:

        used_names.add(usage["name"]) # get the name of the imported library and added it to the set

    for imported in imports:

        name = imported["name"] # get the name of the imported library

        if name not in used_names:
            findings.append({
                "rule": "unused-import",
                "line": imported["line"],
                "message": f"'{name}' is imported but never used."
            })

    return findings
    




