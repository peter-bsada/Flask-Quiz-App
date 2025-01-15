#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""

from questions import Question, RadiobuttonQuestion, CheckboxQuestion

class QuestionManager():
    """
    Manages all questions
    """

    def __init__(self):
        self._points = 0
        self._quest_count = 0
        self.list = []
        self.empty_quest()

    def get_score(self):
        """
        return mina points
        """
        return self._points

    @staticmethod
    def get_max_score():
        """
        return min max_score
        """
        max_score = 11
        return max_score

    def has_next(self):
        """
        går till nästa fråga
        """
        if len(self.list) > self._quest_count:
            return True
        return False

    def get_next(self):
        """
        Kollar vilken fråga man är på
        """
        return self.list[self._quest_count]

    def get_quest_count(self):
        """
        räknar antalet frågor
        """
        return self._quest_count

    def empty_quest(self):
        """
        Mina frågor
        """
        list1 = Question("Hej! Vad heter jag?", "peter")
        list2 = Question("Hur gammmal är jag?", "19")
        list3 = Question("Vilken universitet gå jag i?", "bth")
        list5 = RadiobuttonQuestion("vart kommer jag ifrån?", "stockholm",
                                    ["stockholm", "Malmö", "Blekinge",
                                     "göteborg"])
        list6 = RadiobuttonQuestion("Vilken kurs gillar jag mest?", "design",
                                    ["php", "javascript", "python", "design"])
        list4 = RadiobuttonQuestion("Vad gillar jag mest?", "kebab",
                                    ["pizza", "kebab", "salad", "sushi"])
        list7 = CheckboxQuestion("Vart kommer jag ifrån?",
                                 ["Syrien", "Egypten"], ["Egypten", "Syrien",
                                                         "Sverige", "Italien"])
        list8 = CheckboxQuestion("Vilka 2 kurser har jag nu?",
                                 ["oopython", "databas"], ["databas", "php",
                                                           "oopython",
                                                           "python"])
        list9 = CheckboxQuestion("Hur många år ska jag plugga i bth?",
                                 ["3"], ["1", "2", "3", "5"])
        self.list.append(list1)
        self.list.append(list2)
        self.list.append(list3)
        self.list.append(list4)
        self.list.append(list5)
        self.list.append(list6)
        self.list.append(list7)
        self.list.append(list8)
        self.list.append(list9)



    def read_session(self, session):
        """
        Read current score and current quest number from session
        """
        self._points = session.get("points", 0)
        self._quest_count = session.get("quest_count", 0)

    def write_session(self, session):
        """
        Write current score and quest number to session
        """
        session["points"] = self._points
        session["quest_count"] = self._quest_count

    def reset(self):
        """
        Reset score and quest number to 0
        """
        self._quest_count = 0
        self._points = 0

    def correct_answer(self, form):
        """
        plusar på alla poäng
        """
        if form.get("answer") == self.get_next().get_answer():
            self._points += 1
        for a in self.get_next().get_answer():
            if a in form.getlist("answer"):
                self._points += 1
        self._quest_count += 1
