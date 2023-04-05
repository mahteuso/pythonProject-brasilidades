from bytebank.code.bytebank import Employee
import pytest
from pytest import mark


class TestClass:
    def test_when_birth_receive_13_03_1981_must_return_42(self):
        enter = '13/03/1981'  # given - context
        expected = 42

        employee_test = Employee('Mateus Laranjeira', enter, 1000)
        result = employee_test.age()  # When/action

        assert result == expected  # Then/upshot

    def test_when_name_receive_mateus_laranjeira_must_return_laranjeira(self):
        enter = 'Mateus Silva Laranjeira'  # given
        expected = "Laranjeira"

        employee_test = Employee(enter, 1981, 1000)  # When
        result = employee_test.last_name()

        assert expected == result  # Then

    def test_when_employee_recieve_10k_must_return_minus_ten_percent(self):
        enter = 100000  # Given
        expected = 90000

        employee_test = Employee("Mateus Laranjeira", '13/03/1091', enter)
        result = employee_test.decrease_wage()  # When

        assert expected == result  # Then

    @mark.bonus_calculate
    def test_wen_employee_receive_minus_than_10k_must_return_bonus(self):
        enter = 1000  # Given
        expected = 100

        employee_test = Employee("Mateus Laranjeira", '13/03/1981', enter)
        result = employee_test.bonus_calculate()  # When

        assert expected == result  # Then

    @mark.bonus_calculate
    def test_when_salary_is_more_then_10k_must_return_exception(self):
        with pytest.raises(Exception):

            enter = 11000  # Given

            employee_test = Employee('Mateus Laranjeira', "13/03/1981", enter)
            result = employee_test.bonus_calculate()  # When

            assert result  # Then
