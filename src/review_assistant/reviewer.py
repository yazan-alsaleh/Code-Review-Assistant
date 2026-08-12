# This class will is the main controller for all review rules.

from .rules import check_unused_imports


class Reviewer:

    def review(self, ast_result):

        findings = [] # this array will store all problems in the code

        findings.extend(check_unused_imports(ast_result)) # extend means Add all the items from another list into this list. Because in the check_unused_imports we are already returning array / list and so other rules.

        return findings



