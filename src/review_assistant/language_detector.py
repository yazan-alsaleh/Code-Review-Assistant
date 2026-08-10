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

        



        