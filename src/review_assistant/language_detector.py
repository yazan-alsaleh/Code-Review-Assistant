# This fill will be responsible for detecting what language it is dealing with.
# It should return the detected programming language

import re

class LanguageDetector:

    def detect(self, code):

        # code will be the input 

        if self._is_python(code):
            return "Python"

        if self._is_javascript(code):
            return "JavaScript"

        if self._is_java(code):
            return "Java"

        if self._is_cpp(code):
            return "C++"
        if self._is_c(code):
            return "C"

        # else
        return "Unknown"


    def _is_python(self, code):

        # patterns in python like: def, import, from....
        patterns = [
            r"\bdef\s+\w+\s*\(",
            r"\bimport\s+\w+",
            r"\bfrom\s+\w+\s+import\b",
            r"\bprint\s*\(",
            r"\bif\s+__name__\s*==\s*[\"']__main__[\"']"
        ]

        return any(re.search(patterns, code) for pattern in patterns)
        # Means: Search the code for each pattern. If at least one pattern is found, return True.

    
    def _is_java(self, code):

        patterns = [
            r"\bpublic\s+class\s+\w+",
            r"\bprivate\s+\w+\s+\w+",
            r"\bSystem\.out\.println\s*\(",
            r"\bpublic\s+static\s+void\s+main\b"
        ]

        return any(re.search(pattern, code) for pattern in patterns)


    def _is_javascript(self, code):

        patterns = [
            r"\bconst\s+\w+\s*=",
            r"\blet\s+\w+\s*=",
            r"\bvar\s+\w+\s*=",
            r"\bconsole\.log\s*\(",
            r"=>"
        ]

        return any(re.search(pattern, code) for pattern in patterns)


    def _is_cpp(self, code):

        patterns = [
            r"#include\s*<iostream>",
            r"#include\s*<vector>",
            r"\bstd::",
            r"\bcout\s*<<",
            r"\bcin\s*>>"
        ]

        return any(re.search(pattern, code) for pattern in patterns)

    def _is_c(self, code):
        patterns = [
            r"#include\s*<stdio\.h>",
            r"#include\s*<stdlib\.h>",
            r"\bprintf\s*\(",
            r"\bscanf\s*\("
        ]

        return any(re.search(pattern, code) for pattern in patterns)
    
        