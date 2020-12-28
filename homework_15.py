import tkinter as tk
from tkinter import messagebox


def add_value(value):
    digit = calc.get()

    if digit[0] == '0' and value != '.' and len(digit) == 1:
        digit = digit[1:]

    if value == '.' and digit[-1] == '.':
        digit = digit[:-1]

    calc.delete(0, tk.END)
    calc.insert(0, digit+value)


def add_operation(operation):
    if operation == 'x\u00b2':
        operation = '**'

    value = calc.get()

    if value[-2:] == 'x\u00b2':
        value = value[:-2]

    elif value[-1] in "+-/*":
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value or '**' in value:
        calculate()
        value = calc.get()

    calc.delete(0, tk.END)
    calc.insert(0, value+operation)


def add_clear(operation):
    if operation == 'c':
        calc.delete(0, tk.END)
        calc.insert(0, '0')
    else:
        value = calc.get()

        if len(value) > 1:
            calc.delete(0, tk.END)
            calc.insert(0, value[:-1])
        else:
            calc.delete(0, tk.END)
            calc.insert(0, '0')


def make_value_button(value):
    return tk.Button(text=value, bd=5, font=("Arial", 14), command=lambda: add_value(value))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 14), fg="red",
                     command=lambda: add_operation(operation))


def make_equally_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 14), fg="red",
                     command=lambda: calculate())


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 14), fg="red",
                     command=lambda: add_clear(operation))


def calculate():
    value = calc.get()
    if value[-1] in "+-/*":
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, round(eval(value), 4))
    except (NameError, SyntaxError):
        messagebox.showinfo('Attention', 'You only need to enter numbers')
        calc.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo('Attention', 'You cannot divide by zero')
        calc.insert(0, '0')


def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_value(event.char)
    elif event.char in "+-/*":
        add_operation(event.char)
    elif event.char in '=' or '\r':
        calculate()


def buttons_generator(buttons):
    for button in buttons:
        yield button


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x270+200+200")
root["bg"] = "orange"
root.bind('<Key>', press_key)
calc = tk.Entry(root, justify=tk.RIGHT, font=("Arial", 14), width=20)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=5, stick="we", padx=5)

VALUE_BUTTONS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '00', '0', '.']
CLEAR_BUTTONS = ['\u2190', 'c']
OPERATION_BUTTONS = ['+', '-', '/', '*', 'x\u00b2']
EQUAL_BUTTON = ['=']

value_buttons_generator = buttons_generator(VALUE_BUTTONS)
special_buttons_generator = buttons_generator(
    CLEAR_BUTTONS + OPERATION_BUTTONS + EQUAL_BUTTON)


for row in range(1, 5):
    for col in range(5):
        if 0 <= col <= 2:
            btn = value_buttons_generator.__next__()
            make_value_button(btn).grid(
                row=row, column=col, stick="wens", padx=5, pady=5)
        else:
            btn = special_buttons_generator.__next__()
            if btn in CLEAR_BUTTONS:
                make_clear_button(btn).grid(
                    row=row, column=col, stick="wens", padx=5, pady=5)
            elif btn in OPERATION_BUTTONS:
                make_operation_button(btn).grid(
                    row=row, column=col, stick="wens", padx=5, pady=5)
            else:
                make_equally_button(btn).grid(
                    row=row, column=col, stick="wens", padx=5, pady=5)

for column in range(5):
    root.grid_columnconfigure(column, minsize=60)

for row in range(1, 5):
    root.rowconfigure(row, minsize=60)

root.mainloop()

