import tkinter as tk
from tkinter import messagebox
import math

def perform_selected_operation():
    op = operation_var.get()

    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "Add":
            result = f"{num1} + {num2} = {num1 + num2}"
        elif op == "Subtract":
            result = f"{num1} - {num2} = {num1 - num2}"
        elif op == "Multiply":
            result = f"{num1} * {num2} = {num1 * num2}"
        elif op == "Divide":
            if num2 == 0:
                result = "Cannot divide by zero."
            else:
                result = f"{num1} / {num2} = {num1 / num2}"
        elif op == "Square root (num1)":
            if num1 < 0:
                result = "Square root of negative number not allowed."
            else:
                result = f"√{num1} = {math.sqrt(num1)}"
        elif op == "Square root (num2)":
            if num2 < 0:
                result = "Square root of negative number not allowed."
            else:
                result = f"√{num2} = {math.sqrt(num2)}"
        else:
            result = "Please select an operation."

        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def evaluate_expression():
    expr = expr_entry.get()
    try:
        result = eval(expr, {"__builtins__": None}, vars(math))
        expr_result_label.config(text=f"Expression Result: {result}")
    except Exception as e:
        messagebox.showerror("Evaluation Error", f"Invalid expression.\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Math Operations with Expression Evaluator")
root.geometry("500x550")

# Section 1: Operations on Two Numbers
tk.Label(root, text="Enter First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Select Operation:").pack(pady=5)
operation_var = tk.StringVar(root)
operation_var.set("Add")

operations = [
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "Square root (num1)",
    "Square root (num2)"
]

op_menu = tk.OptionMenu(root, operation_var, *operations)
op_menu.pack()

tk.Button(root, text="Calculate", command=perform_selected_operation).pack(pady=10)
result_label = tk.Label(root, text="", fg="blue", wraplength=450, justify="left")
result_label.pack()

# Section 2: Expression Evaluation
tk.Label(root, text="-------------------------------").pack(pady=10)
tk.Label(root, text="Evaluate Math Expression (e.g., 2+3*math.sqrt(4))").pack()
expr_entry = tk.Entry(root, width=50)
expr_entry.pack()

tk.Button(root, text="Evaluate Expression", command=evaluate_expression).pack(pady=5)
expr_result_label = tk.Label(root, text="", fg="green", wraplength=450, justify="left")
expr_result_label.pack()

root.mainloop()
