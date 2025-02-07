import tkinter as tk

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        result.set("Error")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Buttons for operations
add_button = tk.Button(root, text="+", command=add, width=10)
add_button.grid(row=2, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="-", command=subtract, width=10)
subtract_button.grid(row=2, column=1, padx=5, pady=5)

# Result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
