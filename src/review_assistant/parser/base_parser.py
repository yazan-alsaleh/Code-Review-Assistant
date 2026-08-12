# This file defines what every parser must be able to do.
# Any parser in my system must have a parse() method.


from abc import ABC, abstractmethod
# ABC means Abstract Base Class.
# abstractmethod means: "Every class that inherits from this class must implement this method."



class BaseParser(ABC): # ABC here means BaseParser is an abstract class (means It isn't really meant to be used directly and must be inherited by other classes)

    @abstractmethod # means any child class MUST provide its own implementation of this method.
    def parse(self, code):
        pass # actual implementation will be provided by the child class.


