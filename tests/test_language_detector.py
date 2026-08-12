# from src.review_assistant.language_detector import LanguageDetector
from src.review_assistant.validator import Validator
# def test_python():

#     code = """
#         def hello():
#             print("Hello")
# """

#     detector = LanguageDetector()

#     assert detector.detect(code) == "Python"

# def test_javascript():
#     code = """
# const name = "Yazan";
# console.log(name);
# """

#     detector = LanguageDetector()

#     assert detector.detect(code) == "JavaScript"

def test_valid_code():

    code = """
        def hello():
            print("Hello")
    """

    language = "Python"

    validator = Validator()

    result = validator.validate(code, language)
    print(result)


if __name__ == "__main__":
    test_valid_code()
