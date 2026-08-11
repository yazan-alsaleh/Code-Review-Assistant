# The goal of this file is to check things like: is code provided, is the code string, is it empty, 


class Validator:


    def __init__(self, supported_languages = None, max_code_length = 10000):

        # supported_languages (list): Languages supported by the system.
        # max_code_length (int): Maximum number of characters allowed.


        # If the user doesn't provide a list of languages, use this default list.
        if supported_languages is None:
            supported_languages = [
                "Python",
                "JavaScript",
                "Java",
                "C++",
                "C"
            ]

        self.supported_languages = supported_languages
        self.max_code_length = max_code_length


    # Validate the submitted code. It will return dictionary that has validation result
    def validate(self, code, language):
        # code --> source code
        # language --> Detected language


        if code is None:
            return {
                "valid": False,
                "error": "Code cannot be None"
            }

        if not isinstance(code, str): # this will take the code and check if its type is string
            return {
                "valid": False,
                "error": "Code must be a string"
            }

        if not code.strip(): # if the code has only whitespace (means its empty)
            return {
                "valid": False,
                "error": "Code cannot be emtpy"
            }


        if len(code) > self.max_code_length:
            return {
                "valid": False,
                "error": "Code it too long"
            }

        if language not in self.supported_languages:
            return {
                "valid": False,
                "error": f"Unsupported language: {language}"
            }

        # Everything is valid
        return {
            "valid": True,
            "error": None
        }



