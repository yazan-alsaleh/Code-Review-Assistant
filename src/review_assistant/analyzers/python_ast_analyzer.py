# This file takes that AST and extracts useful information from it
# Look through the Python AST and tell me what is inside the code. So it will return the functions, classes, loops...

import ast # We need ast because you're going to work with AST node types like: ast.Import, ast.ClassDef
# These represent different pieces of Python code.



def calculate_complexity(function_node): # function_node: AST node representing a function.

        # Every function starts with a complexity of 1.
        # Because even a function with no decisions has one basic execution path.
        complexity = 1 

        for node in ast.walk(function_node): # go through all nodes inside the function

            # If the AST node has any of thses:
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1 # Increase complexity by one 

            elif isinstance(node, ast.BoolOp): # BoolOp means: (and) or (or)
                complexity += len(node.values) - 1 # if there are 2 values, we will do values - 1 to add one complexity not 2

        return complexity


class PythonASTAnalyzer: # This class will be responsible for analyzing a Python AST.

    def analyze(self, tree):
        # tree is the AST returned by the parser

        # This dictionary is where we will store everything we discover.
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
                "parameters": [arg.arg for arg in node.args.args],
                "complexity": calculate_complexity(node),
                "body": self._normalize_function_body(node) 
                # _normalize_function_body --> processes the function body into a consistent format.
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
            elif isinstance(node, (ast.For)):
                result["loops"].append({
                    "type": "For",
                    "line": node.lineno,
                    "target": ast.unparse(node.target),
                    "iterable": ast.unparse(node.iter)
                })



            elif isinstance(node, (ast.While)):
                result["loops"].append({
                    "type": "While",
                    "line": node.lineno,
                    "condition": ast.unparse(node.test)
                })
            
            

            elif isinstance(node, ast.If):
                result["conditions"].append({
                    "type": "if",
                    "line": node.lineno,
                    "condition": ast.unparse(node.test), # will give you the condition 
                })




            # for modules that are accessed using .
            elif isinstance(node, ast.Call):
                result["function_calls"].append({
                    "name": self._get_call_name(node.func),
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


    def _normalize_function_body(self, node):

        body = [] # Creates an empty list to store the function's statement / content

        for statement in node.body:
            # Loops through every statement inside the function
            body.append(ast.dump(statement, annotate_fields = False))
            # 1- Python's AST stores a statement as a structured object
            # 2- ast.dump() converts that object into text
            # 3- append() puts that text into the body list.



    def _get_call_name(self, node):

            # Case 1: Simple function: print(), eval(), exec()
            if isinstance(node, ast.Name):
                return node.id

            # Case 2: Function with dot: os.system(), subprocess.run(), math is value and sqrt is attribute
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    return f"{node.value.id}.{node.attr}"

                return node.attr # If the call is an attribute but is more complex, it returns just the last part.

            return None

    
