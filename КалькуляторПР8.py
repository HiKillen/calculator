import tkinter as tk

def button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Створення вікна
root = tk.Tk()
root.title("Калькулятор")

# Створення і розміщення елементів у вікні
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=3, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Кнопка "Рівно"
equal_button = tk.Button(root, text='=', width=5, height=3, command=calculate)
equal_button.grid(row=4, column=2)

# Запуск головного циклу подій
root.mainloop()
