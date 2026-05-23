"""Calculator engine with basic and scientific operations."""

import math
from dataclasses import dataclass


@dataclass
class CalculationResult:
    expression: str
    result: str
    error: bool = False


class CalculatorEngine:
    """Core calculator logic separated from UI."""

    def __init__(self):
        self.expression = ""
        self.history: list[CalculationResult] = []
        self.memory: float = 0.0
        self.last_result: str = ""

    def clear(self):
        self.expression = ""

    def backspace(self):
        self.expression = self.expression[:-1]

    def append(self, text: str):
        self.expression += text

    def set_expression(self, expr: str):
        self.expression = expr

    def toggle_sign(self):
        if self.expression:
            try:
                value = float(self.expression)
                self.expression = str(-value)
                if self.expression.endswith(".0"):
                    self.expression = self.expression[:-2]
            except ValueError:
                pass

    def percent(self):
        try:
            value = float(self.expression)
            self.expression = str(value / 100)
            if self.expression.endswith(".0"):
                self.expression = self.expression[:-2]
        except ValueError:
            pass

    def _prepare_expression(self, expr: str) -> str:
        """Prepare expression for evaluation."""
        expr = expr.replace("x", "*")
        expr = expr.replace("÷", "/")
        expr = expr.replace("^", "**")
        expr = expr.replace("pi", str(math.pi))
        expr = expr.replace("e", str(math.e))
        expr = expr.replace("Ans", self.last_result if self.last_result else "0")
        return expr

    def calculate(self) -> CalculationResult:
        """Evaluate the current expression."""
        if not self.expression:
            return CalculationResult("", "")

        original = self.expression
        prepared = self._prepare_expression(original)

        try:
            result = eval(prepared, {"__builtins__": {}}, {
                "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "asin": math.asin, "acos": math.acos, "atan": math.atan,
                "log": math.log10, "ln": math.log, "sqrt": math.sqrt,
                "abs": abs, "pi": math.pi, "e": math.e,
                "pow": pow, "factorial": math.factorial,
            })

            if isinstance(result, float):
                if result == int(result) and abs(result) < 1e15:
                    result_str = str(int(result))
                else:
                    result_str = f"{result:.10g}"
            else:
                result_str = str(result)

            calc_result = CalculationResult(original, result_str)
            self.history.append(calc_result)
            if len(self.history) > 50:
                self.history = self.history[-50:]
            self.last_result = result_str
            self.expression = result_str
            return calc_result

        except ZeroDivisionError:
            error_result = CalculationResult(original, "Error: Division by zero", error=True)
            self.history.append(error_result)
            self.expression = ""
            return error_result
        except (ValueError, SyntaxError, TypeError, NameError) as e:
            error_result = CalculationResult(original, f"Error: {e}", error=True)
            self.history.append(error_result)
            self.expression = ""
            return error_result

    def memory_add(self):
        try:
            self.memory += float(self.expression)
        except ValueError:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(self.expression)
        except ValueError:
            pass

    def memory_recall(self):
        if self.memory == int(self.memory):
            self.expression = str(int(self.memory))
        else:
            self.expression = str(self.memory)

    def memory_clear(self):
        self.memory = 0.0

    def apply_function(self, func_name: str) -> CalculationResult:
        """Apply a scientific function to the current expression."""
        try:
            value = float(self.expression)
        except ValueError:
            return CalculationResult(self.expression, "Error: Invalid input", error=True)

        funcs = {
            "sin": (math.sin, "sin"),
            "cos": (math.cos, "cos"),
            "tan": (math.tan, "tan"),
            "asin": (math.asin, "asin"),
            "acos": (math.acos, "acos"),
            "atan": (math.atan, "atan"),
            "log": (math.log10, "log"),
            "ln": (math.log, "ln"),
            "sqrt": (math.sqrt, "√"),
            "x²": (lambda x: x**2, "²"),
            "x³": (lambda x: x**3, "³"),
            "1/x": (lambda x: 1/x, "1/"),
            "n!": (lambda x: math.factorial(int(x)), "!"),
            "10^x": (lambda x: 10**x, "10^"),
        }

        if func_name not in funcs:
            return CalculationResult(self.expression, "Error: Unknown function", error=True)

        func, display_name = funcs[func_name]

        try:
            result = func(value)
            if isinstance(result, float) and result == int(result) and abs(result) < 1e15:
                result_str = str(int(result))
            else:
                result_str = f"{result:.10g}"

            expr = f"{display_name}({self.expression})"
            calc_result = CalculationResult(expr, result_str)
            self.history.append(calc_result)
            self.last_result = result_str
            self.expression = result_str
            return calc_result

        except (ValueError, OverflowError) as e:
            error_result = CalculationResult(f"{display_name}({self.expression})", f"Error: {e}", error=True)
            self.history.append(error_result)
            self.expression = ""
            return error_result
