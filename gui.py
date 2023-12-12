import tkinter as tk

# define the calculator class
class SimpleCalc:
    def __init__(self):
        self.result = 0
        self.current = ""
        self.operation = None
        self.use_last_result = False
        self.new_calculation = False

    def add(self, num):
        if self.new_calculation:
            self.current = ""
            self.new_calculation = False
        self.current += str(num)

    def set_operation(self, op):
        if self.current:
            self.result = float(self.current)
            self.current = ""
            self.operation = op
            self.use_last_result = True

    def calculate(self):
        if self.operation is not None and self.current:
            if self.operation == "+":
                self.result += float(self.current)
            elif self.operation == "-":
                self.result -= float(self.current)
            elif self.operation == "*":
                self.result *= float(self.current)
            elif self.operation == "/":
                self.result /= float(self.current)
            self.current = str(self.result)
            self.use_last_result = True
            self.new_calculation = True

    def clear_entry(self):
        self.current = ""

    def backspace(self):
        if self.current:
            self.current = self.current[:-1]

# GUI
class CalculatorApp:
    def __init__(self, master):
        self.calc = SimpleCalc()

        self.result_display = tk.Entry(master, font=('Arial', 24), justify='right', bd=10)
        self.result_display.grid(row=0, column=0, columnspan=4, sticky='nsew')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'Clear', 'AC'
        ]

        row = 1
        col = 0

        for button_text in buttons:
            tk.Button(master, text=button_text, font=('Arial', 18), width=5, command=lambda text=button_text: self.button_click(text)).grid(row=row, column=col, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, text):
        if text == '=':
            self.calc.calculate()
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, self.calc.current)
        elif text == 'Clear':
            self.calc.backspace()
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, self.calc.current)
        elif text == 'AC':
            self.calc = SimpleCalc()
            self.result_display.delete(0, tk.END)
        else:
            if text in '0123456789.':
                self.calc.add(text)
                self.result_display.insert(tk.END, text)
            else:
                self.calc.set_operation(text)
                self.result_display.insert(tk.END, text)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Simple Calculator")
    app = CalculatorApp(root)

    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
