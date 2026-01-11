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
    'C', None, None, '⌫',
    '9', '8', '7', '+',
    '6', '5', '4', '-',
    '3', '2', '1', 'x',
    None, '0', None, '/'
]

button_list = []

row = 1
column = 1

for i, symbol in enumerate(symbol_list):
    if symbol != None:
        button = tk.Button(frame, text=symbol, width=2, height=1, font=('Arial', 20))
        button.grid(row=row, column=column, padx=5, pady=5)
        print(symbol, row, column)
        button_list.append(button)

    column += 1
    if column > 4:
        column = 1
        row += 1
    


#bt0 = tk.Button(frame, text='0', width=2, height=1, font=('Arial', 20))
#bt0.grid(row=4, column=2, padx=8, pady=8)



window.mainloop()