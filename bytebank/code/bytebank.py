from datetime import date

class Employee:
    def __init__(self, name, date_of_birth, wage):
        self._name = name
        self._birth = date_of_birth
        self._wage = wage

    @property
    def name(self):
        return self._name
    @property
    def birth(self):
        return self._birth
    @property
    def wage(self):
        return self.wage
