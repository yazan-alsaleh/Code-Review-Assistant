# This class will is the main controller for all review rules.

from .rules.unused_imports import check_unused_imports
from .rules.unused_variables import check_unused_variables


class Reviewer:

    def review(self, ast_result):

        findings = [] # this array will store all problems in the code

        findings.extend(check_unused_imports(ast_result)) # extend means Add all the items from another list 
        #into this list. Because in the check_unused_imports we are already returning array / list and so other rules.

        findings.extend(check_unused_variables(ast_result)) # to check unused variables

        return findings



