# This class will is the main controller for all review rules.

from .rules.unused_imports import check_unused_imports
from .rules.unused_variables import check_unused_variables
from .rules.unused_functions import check_unused_functions


class Reviewer:

    def __init__(self):

        self.rules = [ # a list with functions, then we will go through the list one function at a time.
            check_unused_imports,
            check_unused_variables,
            check_unused_functions
        ]

    def review(self, ast_result): # This method receives the result from your AST analyzer.
    # The reviewer takes the AST analyzer information and runs your rules against it.

        findings = [] # this array will store all problems in the source code

        for rule in self.rules: # Go through every review rule that I have registered (each iteration will check a rule).
            
            findings.extend(rule(ast_result)) 
            # 1- rule contains a function, you're calling that function, example: check_unused_imports(ast_result)
            # 2- extend means add all the items from another list into this list.
            # Because in the check_unused_imports for example we are already returning array / list and so other rules.
        return findings


        

