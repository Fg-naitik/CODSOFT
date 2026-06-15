import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main Window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x550")
root.resizable(False, False)

# Display
entry = tk.Entry(root, font=("Arial", 24), bd=10, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button Layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+'],
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 18),
            command=lambda x=btn: click(x),
            width=5,
            height=2
        ).pack(side="left", expand=True, fill="both")

# Bottom Buttons
bottom = tk.Frame(root)
bottom.pack(expand=True, fill="both")

tk.Button(
    bottom,
    text="C",
    font=("Arial", 18),
    command=clear,
    width=5,
    height=2
).pack(side="left", expand=True, fill="both")

tk.Button(
    bottom,
    text="=",
    font=("Arial", 18),
    command=calculate,
    width=10,
    height=2
).pack(side="left", expand=True, fill="both")

root.mainloop()