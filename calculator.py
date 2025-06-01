import tkinter as tk
from tkinter import messagebox
import math

# --- GUI SETUP ---
root = tk.Tk()
root.title("Calculator")
root.geometry("360x500")
root.config(bg="#f8c8dc")  # pastel pink background

# Custom Font
FONT = ("Helvetica", 18)
BTN_FONT = ("Helvetica", 16)

# Entry Field
entry = tk.Entry(root, font=FONT, bd=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=10, padx=10)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 14), bg="#f8c8dc", fg="#7f5af0")
result_label.grid(row=1, column=0, columnspan=4, pady=(0, 10))


# --- FUNCTIONALITY ---

def press(key):
    entry.insert(tk.END, key)

def clear_entry():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")

def calculate():
    expr = entry.get()
    try:
        result = eval(expr)
        result_label.config(text=f"Result: {result}")
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        result_label.config(text="Error")
        messagebox.showerror("Error", "Invalid Expression")
        entry.delete(0, tk.END)

def advanced_operation(op):
    try:
        val = float(entry.get())
        if op == "sqrt":
            result = math.sqrt(val)
        elif op == "pow2":
            result = math.pow(val, 2)
        else:
            raise ValueError("Unsupported op")

        result_label.config(text=f"Result: {result}")
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        result_label.config(text="Error")
        messagebox.showerror("Error", "Invalid Input")


# --- BUTTONS ---
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('/', 5, 3),
    ('sqrt', 6, 0), ('^2', 6, 1), ('=', 6, 2, 2)
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1

    if text == '=':
        cmd = calculate
    elif text == 'C':
        cmd = clear_entry
    elif text == 'sqrt':
        cmd = lambda: advanced_operation("sqrt")
    elif text == '^2':
        cmd = lambda: advanced_operation("pow2")
    else:
        cmd = lambda t=text: press(t)

    button = tk.Button(root, text=text, font=BTN_FONT, bg="#eac6f8", fg="#3c2a4d",
                       width=6*colspan, height=2, command=cmd)
    button.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4, sticky="nsew")

# Configure grid weight for responsive resizing
for i in range(7):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()
