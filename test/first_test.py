import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    '''1.Тест для метода сложения:
    # - Вводим числа 5 и 10, должны получить в результате 15'''
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(10, 5) == 15

    '''2. Тест для метода вычитания:
    # - Вводим числа 20 и 5, должны получить в результате 15'''
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(20, 5) == 15

    '''3. Тест для метода умножения:
    # - Вводим числа 7 и 3, должны получить в результате 21'''
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(7, 3) == 21

    '''4. Тест для метода деления:
    # - Вводим числа 30 и 6, должны получить в результате 5.0 (потому что это будет вещественное число)'''
    def test_division_calculate_correctly(self):
        assert self.calc.division(30, 6) == 5.0
