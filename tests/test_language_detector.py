from src.review_assistant.language_detector import LanguageDetector

def test_python():

    code = """
        def hello():
            print("Hello")
"""

    detector = LanguageDetector()

    assert detector.detect(code) == "Python"

def test_javascript():
    code = """
const name = "Yazan";
console.log(name);
"""

    detector = LanguageDetector()

    assert detector.detect(code) == "JavaScript"

