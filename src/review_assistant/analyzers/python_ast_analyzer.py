# This file takes that AST and extracts useful information from it
# Look through the Python AST and tell me what is inside the code. So it will return the functions, classes, loops...

import ast # We need ast because you're going to work with AST node types like: ast.Import, ast.ClassDef
# These represent different pieces of Python code.


class PythonASTAnalyzer: # This class will be responsible for analyzing a Python AST.

    def analyze(self, tree):
        # tree is the AST returned by the parser

        # This is where we will store everything we discover.
        result = {
            "functions": [],
            "classes": [],
            "imports": [],
            "variables": [],
            "loops": [],
            "conditions": [],
            "function_calls": [],
            "name_usage": [] # used variables and modules 
        }


        # For every piece of the Python code represented in this AST, check what type of node it is.
        for node in ast.walk(tree): # ast.walk() goes through every node in the AST.

            if isinstance(node, ast.FunctionDef):
                result["functions"].append({ # store the function name in the functions array
                "name": node.name,
                "line": node.lineno,
                "end_line": node.end_lineno,
                "parameters": [arg.arg for arg in node.args.args]
                }) 




            elif isinstance(node, ast.ClassDef):
                result["classes"].append({
                    "name": node.name,
                    "line": node.lineno,
                    "end_line": node.end_lineno
                })




            # for code like this: import x
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    result["imports"].append({
                        "name": alias.name,
                        "line": node.lineno
                    })




            # To handel code like this: from math import sqrt. it will store both math and sqrt
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    result["imports"].append(f"{node.module}.{alias.name}")




            # for assignments syntax
            elif isinstance(node, ast.Assign):
                # looks at the thing being assigned.
                for target in node.targets:
                    if isinstance(target, ast.Name): # target is the variable (x)
                        result["variables"].append({  # target.id gives (x) and store it
                            "name": target.id,
                            "line": node.lineno,
                        })




            # Either loops
            elif isinstance(node, (ast.For, ast.While)):
                result["loops"].append({
                    "type": type(node).__name__,
                    "line": node.lineno,
                    "target": ast.unparse(node.target),
                    "iterable": ast.unparse(node.iter)
                })


            

            elif isinstance(node, ast.If):
                result["conditions"].append({
                    "type": "if",
                    "line": node.lineno,
                    "condition": ast.unparse(node.test), # will give you the condition 
                })





            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    result["function_calls"].append({
                        "name": node.func.id, # id gives the function name
                        "line": node.lineno
                    })



                # for modules that are accessed using .
                elif isinstance(node.func, ast.Attribute):
                    result["function_calls"].append({
                        "name": node.func.attr,
                        "line": node.lineno
                    })



            elif isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Load): # because we want the used part we use node.ctx (context)
                    # it tells python is this name being used/read, or is it being assigned to?
                    # for detecting unused imports, we care about actually used so use Load
                    result["name_usage"].append({
                        "name": node.id,
                        "line": node.lineno
                    })

        return result

