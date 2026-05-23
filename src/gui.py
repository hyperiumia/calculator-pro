"""GUI for Calculator Pro using CustomTkinter."""

import customtkinter as ctk
from src.config import THEMES, FONT_DISPLAY, FONT_BUTTON, FONT_HISTORY, FONT_SMALL
from src.engine import CalculatorEngine


class CalculatorGUI:
    """Main calculator window with basic and scientific modes."""

    def __init__(self):
        self.engine = CalculatorEngine()
        self.theme = "dark"
        self.scientific_mode = False
        self.colors = THEMES[self.theme]

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Calculator Pro v1.0.0")
        self.root.geometry("400x620")
        self.root.resizable(False, False)
        self.root.configure(fg_color=self.colors["bg"])

        self._build_ui()
        self._bind_keyboard()
        self._apply_theme()

    def _build_ui(self):
        """Build all UI components."""
        self.display_frame = ctk.CTkFrame(self.root, fg_color=self.colors["display_bg"], corner_radius=10)
        self.display_frame.pack(fill="x", padx=10, pady=(10, 5))

        self.expression_label = ctk.CTkLabel(
            self.display_frame, text="", font=FONT_SMALL,
            text_color=self.colors["history_fg"], anchor="e",
        )
        self.expression_label.pack(fill="x", padx=15, pady=(10, 0))

        self.display = ctk.CTkLabel(
            self.display_frame, text="0", font=FONT_DISPLAY,
            text_color=self.colors["display_fg"], anchor="e",
        )
        self.display.pack(fill="x", padx=15, pady=(0, 15))

        self.top_bar = ctk.CTkFrame(self.root, fg_color="transparent")
        self.top_bar.pack(fill="x", padx=10, pady=2)

        self.theme_btn = ctk.CTkButton(
            self.top_bar, text="Light" if self.theme == "dark" else "Dark",
            width=60, height=28, font=("Segoe UI", 11),
            fg_color=self.colors["btn_function"],
            hover_color=self.colors["btn_function_hover"],
            command=self._toggle_theme,
        )
        self.theme_btn.pack(side="left")

        self.sci_btn = ctk.CTkButton(
            self.top_bar, text="Scientific", width=80, height=28,
            font=("Segoe UI", 11),
            fg_color=self.colors["btn_function"],
            hover_color=self.colors["btn_function_hover"],
            command=self._toggle_scientific,
        )
        self.sci_btn.pack(side="left", padx=5)

        self.mem_label = ctk.CTkLabel(
            self.top_bar, text="", font=("Segoe UI", 10),
            text_color=self.colors["history_fg"],
        )
        self.mem_label.pack(side="right")

        self.sci_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.sci_frame.pack(fill="x", padx=10, pady=2)

        self._build_scientific_buttons()

        self.main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self._build_main_buttons()

        self.history_frame = ctk.CTkFrame(self.root, fg_color=self.colors["history_bg"], corner_radius=10, height=100)
        self.history_frame.pack(fill="x", padx=10, pady=(5, 10))

        self.history_label = ctk.CTkLabel(
            self.history_frame, text="History", font=("Segoe UI", 12, "bold"),
            text_color=self.colors["fg"], anchor="w",
        )
        self.history_label.pack(fill="x", padx=10, pady=(5, 0))

        self.history_text = ctk.CTkTextbox(
            self.history_frame, font=FONT_HISTORY, height=70,
            fg_color=self.colors["history_bg"],
            text_color=self.colors["history_fg"],
        )
        self.history_text.pack(fill="x", padx=10, pady=(0, 5))

    def _build_scientific_buttons(self):
        """Build scientific function buttons (hidden by default)."""
        sci_buttons = [
            ("sin", "cos", "tan", "π", "e"),
            ("asin", "acos", "atan", "x²", "x³"),
            ("log", "ln", "√", "n!", "1/x"),
            ("10^x", "(", ")", "^", "Ans"),
        ]

        self.sci_btn_widgets = []
        for row_idx, row in enumerate(sci_buttons):
            row_frame = ctk.CTkFrame(self.sci_frame, fg_color="transparent")
            row_frame.pack(fill="x", pady=1)
            for text in row:
                btn = ctk.CTkButton(
                    row_frame, text=text, font=("Segoe UI", 13),
                    height=35, corner_radius=8,
                    fg_color=self.colors["btn_function"],
                    hover_color=self.colors["btn_function_hover"],
                    text_color=self.colors["fg"],
                    command=lambda t=text: self._on_sci_button(t),
                )
                btn.pack(side="left", expand=True, fill="x", padx=1)
                self.sci_btn_widgets.append(btn)

    def _build_main_buttons(self):
        """Build main calculator buttons."""
        buttons = [
            [("MC", "mem"), ("MR", "mem"), ("M+", "mem"), ("M-", "mem"), ("C", "clear"), ("⌫", "clear")],
            [("7", "num"), ("8", "num"), ("9", "num"), ("÷", "op"), ("%", "func"), ("+/-", "func")],
            [("4", "num"), ("5", "num"), ("6", "num"), ("x", "op"), ("(", "func"), (")", "func")],
            [("1", "num"), ("2", "num"), ("3", "num"), ("-", "op"), (".", "num"), ("", "")],
            [("0", "num"), ("", ""), ("", ""), ("+", "op"), ("", ""), ("=", "equal")],
        ]

        for row_idx, row in enumerate(buttons):
            row_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
            row_frame.pack(fill="both", expand=True, pady=1)
            for text, btn_type in row:
                if not text:
                    spacer = ctk.CTkLabel(row_frame, text="", width=55)
                    spacer.pack(side="left", expand=True, fill="both", padx=1)
                    continue

                color_map = {
                    "num": (self.colors["btn_number"], self.colors["btn_number_hover"]),
                    "op": (self.colors["btn_operator"], self.colors["btn_operator_hover"]),
                    "func": (self.colors["btn_function"], self.colors["btn_function_hover"]),
                    "equal": (self.colors["btn_equal"], self.colors["btn_equal_hover"]),
                    "clear": (self.colors["btn_clear"], self.colors["btn_clear_hover"]),
                    "mem": (self.colors["btn_function"], self.colors["btn_function_hover"]),
                }
                fg, hover = color_map.get(btn_type, (self.colors["btn_number"], self.colors["btn_number_hover"]))

                font = ("Segoe UI", 14) if btn_type == "mem" else FONT_BUTTON

                btn = ctk.CTkButton(
                    row_frame, text=text, font=font,
                    height=55, corner_radius=8,
                    fg_color=fg, hover_color=hover,
                    text_color=self.colors["fg"],
                    command=lambda t=text: self._on_button(t),
                )
                btn.pack(side="left", expand=True, fill="both", padx=1)

    def _on_button(self, text: str):
        """Handle main button clicks."""
        if text == "C":
            self.engine.clear()
        elif text == "⌫":
            self.engine.backspace()
        elif text == "=":
            self.engine.calculate()
            self._update_history()
        elif text == "+/-":
            self.engine.toggle_sign()
        elif text == "%":
            self.engine.percent()
        elif text == "MC":
            self.engine.memory_clear()
        elif text == "MR":
            self.engine.memory_recall()
        elif text == "M+":
            self.engine.memory_add()
        elif text == "M-":
            self.engine.memory_subtract()
        else:
            self.engine.append(text)

        self._update_display()

    def _on_sci_button(self, text: str):
        """Handle scientific button clicks."""
        if text in ("sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "√", "x²", "x³", "1/x", "n!", "10^x"):
            self.engine.apply_function(text)
            self._update_history()
        elif text == "π":
            self.engine.append("pi")
        elif text == "e":
            self.engine.append("e")
        elif text == "^":
            self.engine.append("^")
        elif text == "Ans":
            self.engine.append("Ans")
        elif text in ("(", ")"):
            self.engine.append(text)

        self._update_display()

    def _update_display(self):
        """Update the display with current expression."""
        expr = self.engine.expression if self.engine.expression else "0"
        if len(expr) > 25:
            self.display.configure(font=("Segoe UI", 24, "bold"))
        else:
            self.display.configure(font=FONT_DISPLAY)
        self.display.configure(text=expr)
        self.mem_label.configure(text=f"M: {self.engine.memory}" if self.engine.memory != 0 else "")

    def _update_history(self):
        """Update history panel."""
        self.history_text.configure(state="normal")
        self.history_text.delete("1.0", "end")
        for item in self.engine.history[-8:]:
            if item.error:
                self.history_text.insert("end", f"{item.expression} = {item.result}\n")
            else:
                self.history_text.insert("end", f"{item.expression} = {item.result}\n")
        self.history_text.configure(state="disabled")

    def _toggle_theme(self):
        """Switch between dark and light themes."""
        self.theme = "light" if self.theme == "dark" else "dark"
        self.colors = THEMES[self.theme]
        ctk.set_appearance_mode(self.theme)
        self.theme_btn.configure(text="Light" if self.theme == "dark" else "Dark")
        self._apply_theme()

    def _apply_theme(self):
        """Apply current theme colors to all widgets."""
        self.root.configure(fg_color=self.colors["bg"])
        self.display_frame.configure(fg_color=self.colors["display_bg"])
        self.display.configure(text_color=self.colors["display_fg"])
        self.expression_label.configure(text_color=self.colors["history_fg"])
        self.history_frame.configure(fg_color=self.colors["history_bg"])
        self.history_text.configure(fg_color=self.colors["history_bg"], text_color=self.colors["history_fg"])
        self.mem_label.configure(text_color=self.colors["history_fg"])

    def _toggle_scientific(self):
        """Toggle scientific mode visibility."""
        self.scientific_mode = not self.scientific_mode
        if self.scientific_mode:
            self.sci_frame.pack(fill="x", padx=10, pady=2, before=self.main_frame)
            self.root.geometry("400x850")
            self.sci_btn.configure(text="Basic")
        else:
            self.sci_frame.pack_forget()
            self.root.geometry("400x620")
            self.sci_btn.configure(text="Scientific")

    def _bind_keyboard(self):
        """Bind keyboard shortcuts."""
        self.root.bind("<Key>", self._on_key)

    def _on_key(self, event):
        """Handle keyboard input."""
        key = event.char
        keysym = event.keysym

        if key in "0123456789.+-":
            self.engine.append(key)
        elif key == "*":
            self.engine.append("x")
        elif key == "/":
            self.engine.append("÷")
        elif key == "(":
            self.engine.append("(")
        elif key == ")":
            self.engine.append(")")
        elif keysym == "Return" or key == "=":
            self.engine.calculate()
            self._update_history()
        elif keysym == "BackSpace":
            self.engine.backspace()
        elif keysym == "Escape":
            self.engine.clear()
        elif key == "%":
            self.engine.percent()

        self._update_display()

    def run(self):
        self.root.mainloop()
