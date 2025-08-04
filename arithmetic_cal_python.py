import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Invalid Operation", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Main window
root = tk.Tk()
root.title("🔢 Simple Calculator")
root.geometry("350x320")
root.configure(bg="#F0F8FF")

# Heading
tk.Label(root, text="Simple Calculator", font=("Helvetica", 18, "bold"), bg="#F0F8FF", fg="#333").pack(pady=15)

# Entry fields
entry1 = tk.Entry(root, font=("Helvetica", 14), width=15, justify="center")
entry1.pack(pady=5)

entry2 = tk.Entry(root, font=("Helvetica", 14), width=15, justify="center")
entry2.pack(pady=5)

# Operation selection
operation_var = tk.StringVar()
operation_var.set("+")

operations_frame = tk.Frame(root, bg="#F0F8FF")
operations_frame.pack(pady=10)

for op in ["+", "-", "*", "/"]:
    tk.Radiobutton(operations_frame, text=op, variable=operation_var, value=op,
                   font=("Helvetica", 12), bg="#F0F8FF").pack(side=tk.LEFT, padx=10)

# Calculate button
tk.Button(root, text="Calculate", command=calculate,
          font=("Helvetica", 13), bg="#4CAF50", fg="white", width=15).pack(pady=15)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 14), bg="#F0F8FF", fg="#000")
result_label.pack(pady=10)

# Run the app
root.mainloop()
