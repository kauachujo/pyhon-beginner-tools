import tkinter as tk

# JANELA
window = tk.Tk()
window.title('Calculator')
window.geometry('300x400')

# ENTRADA

window.grid_columnconfigure(0, weight=1)
entry = tk.Entry(window, width=15 , font=('Arial', 20))
entry.grid(row=0, column=0, sticky='', pady=10)

# BOTÕES

frame = tk.Frame(window)
frame.grid(row=1, column=0, pady=5)

symbol_list = [
    'C', '+', '-', '⌫',
    '9', '8', '7', '×',
    '6', '5', '4', '÷',
    '3', '2', '1', '=',
    None, '0', None, None
]

button_list = []
row = 1
column = 1

def on_button_click(symbol):
    if symbol.isdigit():
        entry.insert(tk.END, symbol)

    elif symbol == 'C':
        entry.delete(0, tk.END)

    elif symbol == '⌫':
        text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, text[:-1])
    
    elif symbol == '=':
        expression = entry.get().replace('×', '*')
        expression = expression.replace('÷', '/')
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    else:
        entry.insert(tk.END, symbol)


for i, symbol in enumerate(symbol_list):
    if symbol != None:
        button = tk.Button(frame, text=symbol, width=2, height=1, font=('Arial', 20),
                           command=lambda s=symbol: on_button_click(s))
        button.grid(row=row, column=column, padx=5, pady=5)
        button_list.append(button)

    column += 1
    if column > 4:
        column = 1
        row += 1

for i, button in enumerate(button_list):
    grid = button.grid_info()
    if grid['row'] == 1 or grid['column'] == 4:
        button.config(bg='orange')
    
print(button_list)
window.mainloop()