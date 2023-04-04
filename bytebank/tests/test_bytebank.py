from bytebank.code.bytebank import Employee
class TestClass:
    def test_when_birth_receive_13_03_1981_must_return_42(self):

        enter = '13/03/1981' # given - context
        expected = 42

        employee_test = Employee('Mateus', enter, 1000)
        result = employee_test.age() # When/action

        assert result == expected # Then/upshot
