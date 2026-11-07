import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            state="readonly",
            width=16,
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)
        self._show("0")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("−", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("^", 5, 0), ("%", 5, 1),
        ]

        for label, row, column in buttons:
            tk.Button(
                root,
                text=label,
                font=("Arial", 18),
                width=5,
                height=2,
                command=lambda value=label: self.press(value),
            ).grid(row=row, column=column, padx=3, pady=3)

    def _show(self, text):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, text)
        self.display.config(state="readonly")

    def press(self, value):
        if value == "C":
            self.expression = ""
            self._show("0")
        elif value == "=":
            try:
                expression = (
                    self.expression
                    .replace("÷", "/")
                    .replace("×", "*")
                    .replace("−", "-")
                    .replace("^", "**")
                )
                result = eval(expression, {"__builtins__": {}}, {})
                self.expression = str(result)
                self._show(self.expression)
            except (SyntaxError, ZeroDivisionError, TypeError, OverflowError):
                self.expression = ""
                self._show("Error")
        else:
            self.expression += value
            self._show(self.expression)


root = tk.Tk()
Calculator(root)
root.mainloop()
