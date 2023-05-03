import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create entry widget for displaying the result
        self.result = tk.Entry(self.master, width=20, font=("Arial", 16))
        self.result.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "=", "(", ")", "%"
        ]

        # Define button click events
        self.commands = {
            "C": self.clear,
            "=": self.calculate,
            "%": self.percent
        }

        # Create button grid
        self.row = 1
        self.col = 0
        for button in self.buttons:
            tk.Button(
                self.master, text=button, width=5, height=2,
                command=lambda x=button: self.button_click(x)
            ).grid(row=self.row, column=self.col, padx=5, pady=5)

            self.col += 1
            if self.col > 3:
                self.col = 0
                self.row += 1

        self.equation = ""

    def button_click(self, button):
        if button in self.commands:
            self.commands[button]()
        else:
            self.equation += str(button)
            self.result.delete(0, tk.END)
            self.result.insert(0, self.equation)

    def clear(self):
        self.equation = ""
        self.result.delete(0, tk.END)

    def calculate(self):
        try:
            self.equation = str(eval(self.equation))
            self.result.delete(0, tk.END)
            self.result.insert(0, self.equation)
        except:
            self.result.delete(0, tk.END)
            self.result.insert(0, "Error")

    def percent(self):
        try:
            self.equation = str(eval(self.equation + "/100"))
            self.result.delete(0, tk.END)
            self.result.insert(0, self.equation)
        except:
            self.result.delete(0, tk.END)
            self.result.insert(0, "Error")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
