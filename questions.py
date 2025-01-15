"""
Contains all classes for the different types of questions
"""

class Question():
    """
    klass
    """

    type_ = 'text'

    def __init__(self, text, answer):
        self._answer = answer
        self._text = text

    @classmethod
    def get_type(cls):
        """
        get_type funktionen
        """
        return cls.type_


    def get_text(self):
        """
        Returnan min fråga
        """
        return self._text

    def get_answer(self):
        """
        hämtar answer
        """

        return self._answer


class RadiobuttonQuestion(Question):
    """
    klass
    """

    type_ = "radiobutton"

    def __init__(self, text, answer, alternatives):
        super().__init__(text, answer)
        self._alternatives = alternatives

    def get_alternatives(self):
        """
        vissar alternativen
        """
        return self._alternatives


class CheckboxQuestion(Question):
    """
    klass
    """
    type_ = "checkbox"

    def __init__(self, text, answer, alternatives):
        super().__init__(text, answer)
        self._alternatives = alternatives

    def get_alternatives(self):
        """
        vissar alternativen
        """
        return self._alternatives

    def check_answer(self, respons):
        """
        kollar om frågan är rätt
        """
        if respons == self._alternatives:
            return True
