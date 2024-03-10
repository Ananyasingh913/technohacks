import tkinter as tk

def calculate():
    result = eval(entry.get())
    output_window = tk.Toplevel(root)
    output_window.title("Result")
    result_label = tk.Label(output_window, text=f"Result: {result}")
    result_label.pack()

def append_to_entry(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, command=lambda b=button: append_to_entry(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Calculate", width=20, command=calculate).grid(row=row, column=0, columnspan=4)

root.mainloop()
