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
        return self._wage

    def age(self):
        date_birth = self.birth.split('/')
        year_birth = date_birth[-1]
        actual_year = date.today().year
        return actual_year - int(year_birth)

    def bonus_calculate(self):
        value = self.wage * 0.1
        if value > 1000:
            value = 0
        return value

    def __str__(self):
        return f'Employee: {self.name}\n' \
               f'Age: {self.age()}\n' \
               f'Wage: {self.wage}'