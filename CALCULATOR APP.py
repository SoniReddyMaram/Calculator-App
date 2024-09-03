import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main application window
root = tk.Tk()
root.title("Simple Calculator")

# Number entry fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Operation selection
operation_var = tk.StringVar(root)
operation_var.set('+')  # Set default value

label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

dropdown_operation = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
dropdown_operation.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=perform_calculation)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result display
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()

