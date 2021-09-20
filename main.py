"""
Project : Making a Windows Calculator App
@author : M.Raahim Rizwan 
Credit for this project's idea goes to this youtube's video:
https://youtu.be/QZPv1y2znZo
"""


# Importing the libraries
import tkinter as tk

# Constant Program Variables
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
LARGE_FONT_STYLE = ("Arial", 40, "bold")

# Colors
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
OFF_WHITE = "#F8F8FF"

# Creating the calculator class
class Calculator:
    def __init__(self):
        """
        Initializing the methods in the program.
        """
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.window.wm_iconbitmap("Assets/icon.ico")
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), ".":(4,1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1) 
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        """
        Adding the functionality to type from the keyboard.
        """
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        """
        Creates the special buttons for example C, = etc.
        """
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_square_root_button()


    def create_display_labels(self):
        """
        Creates the labels for the display.
        """
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        """
        Creates the frame for the output.
        """
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        """
        Adds the current expression to the string of value.
        """
        self.current_expression += str(value)
        self.update_label()


    def create_digit_buttons(self):
        """
        Creates the buttons.
        """
        for digit, grid_values in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,  command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_values[0], column=grid_values[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        """
        Appends the operator with the digit in the upper label and clears the lower label for the next entry.
        """
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()


    def create_operator_buttons(self):
        """
        Creates the operator buttons.
        """
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        """
        Clears the entire screen.
        """
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        """
        Creates the clear(C) button.
        """
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command= self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        """
        Adds the functionality to square a number.
        """
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        """
        Creates the square button.
        """
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)


    def square_root(self):
        """
        Adds the functionality to find the square root of a number.
        """
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_square_root_button(self):
        """
        Creates the square root button.
        """
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command=self.square_root)
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def evaluate(self):
        """
        Adds functionality to the buttons (operations).
        """
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Invalid"
        finally:
            self.update_label()
        

    def create_equal_button(self):
        """
        Creates the equals to (=) button.
        """
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,borderwidth=0, command= self.evaluate)
        button.grid(row=4, column=3, sticky=tk.NSEW, columnspan=2)



    def create_buttons_frame(self):
        """
        Creates the frame for the buttons.
        """
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        """
        Updates the total label.
        """
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol} ")
        self.total_label.config(text=expression)

    def update_label(self):
        """
        Updates the upper label.
        """
        self.label.config(text=self.current_expression[:11])


    def run(self):
        """
        Runs the program.
        """
        self.window.mainloop()

if __name__ == '__main__':
    # The execution of the code starts here.
    calculator = Calculator()
    calculator.run()


