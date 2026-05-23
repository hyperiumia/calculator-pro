"""Tests for calculator engine."""

import pytest
import math
from src.engine import CalculatorEngine


class TestCalculatorEngine:

    def setup_method(self):
        self.engine = CalculatorEngine()

    def test_initial_state(self):
        assert self.engine.expression == ""
        assert self.engine.last_result == ""
        assert self.engine.memory == 0.0

    def test_append(self):
        self.engine.append("2")
        self.engine.append("+")
        self.engine.append("3")
        assert self.engine.expression == "2+3"

    def test_clear(self):
        self.engine.append("123")
        self.engine.clear()
        assert self.engine.expression == ""

    def test_backspace(self):
        self.engine.append("123")
        self.engine.backspace()
        assert self.engine.expression == "12"

    def test_basic_addition(self):
        self.engine.set_expression("2+3")
        result = self.engine.calculate()
        assert result.result == "5"
        assert result.error is False

    def test_basic_subtraction(self):
        self.engine.set_expression("10-4")
        result = self.engine.calculate()
        assert result.result == "6"

    def test_basic_multiplication(self):
        self.engine.set_expression("3x7")
        result = self.engine.calculate()
        assert result.result == "21"

    def test_basic_division(self):
        self.engine.set_expression("15÷3")
        result = self.engine.calculate()
        assert result.result == "5"

    def test_decimal_result(self):
        self.engine.set_expression("10÷3")
        result = self.engine.calculate()
        assert "3.333" in result.result

    def test_division_by_zero(self):
        self.engine.set_expression("5÷0")
        result = self.engine.calculate()
        assert result.error is True

    def test_parentheses(self):
        self.engine.set_expression("(2+3)x4")
        result = self.engine.calculate()
        assert result.result == "20"

    def test_complex_expression(self):
        self.engine.set_expression("2+3x4")
        result = self.engine.calculate()
        assert result.result == "14"

    def test_power(self):
        self.engine.set_expression("2^10")
        result = self.engine.calculate()
        assert result.result == "1024"

    def test_toggle_sign(self):
        self.engine.set_expression("42")
        self.engine.toggle_sign()
        assert self.engine.expression == "-42"

    def test_percent(self):
        self.engine.set_expression("50")
        self.engine.percent()
        assert self.engine.expression == "0.5"

    def test_history_tracking(self):
        self.engine.set_expression("2+3")
        self.engine.calculate()
        self.engine.set_expression("5x5")
        self.engine.calculate()
        assert len(self.engine.history) == 2
        assert self.engine.history[0].result == "5"
        assert self.engine.history[1].result == "25"

    def test_memory_add(self):
        self.engine.set_expression("10")
        self.engine.memory_add()
        assert self.engine.memory == 10.0

    def test_memory_subtract(self):
        self.engine.set_expression("3")
        self.engine.memory_add()
        self.engine.set_expression("1")
        self.engine.memory_subtract()
        assert self.engine.memory == 2.0

    def test_memory_recall(self):
        self.engine.memory = 42.0
        self.engine.memory_recall()
        assert self.engine.expression == "42"

    def test_memory_clear(self):
        self.engine.memory = 100.0
        self.engine.memory_clear()
        assert self.engine.memory == 0.0

    def test_scientific_sin(self):
        self.engine.set_expression("90")
        result = self.engine.apply_function("sin")
        assert "0.89" in result.result

    def test_scientific_sqrt(self):
        self.engine.set_expression("144")
        result = self.engine.apply_function("sqrt")
        assert result.result == "12"

    def test_scientific_square(self):
        self.engine.set_expression("7")
        result = self.engine.apply_function("x²")
        assert result.result == "49"

    def test_scientific_factorial(self):
        self.engine.set_expression("5")
        result = self.engine.apply_function("n!")
        assert result.result == "120"

    def test_scientific_log(self):
        self.engine.set_expression("100")
        result = self.engine.apply_function("log")
        assert result.result == "2"

    def test_scientific_reciprocal(self):
        self.engine.set_expression("4")
        result = self.engine.apply_function("1/x")
        assert result.result == "0.25"

    def test_pi_constant(self):
        self.engine.set_expression("pi")
        result = self.engine.calculate()
        assert "3.14159" in result.result

    def test_ans_reference(self):
        self.engine.set_expression("10+5")
        self.engine.calculate()
        self.engine.set_expression("Ans+10")
        result = self.engine.calculate()
        assert result.result == "25"
