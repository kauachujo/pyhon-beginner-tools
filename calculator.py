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
frame.grid(row=1, column=0, pady=20)

bt0 = tk.Button(frame, text='0', width=2, height=1, font=('Arial', 20))
bt1 = tk.Button(frame, text='1', width=2, height=1, font=('Arial', 20))
bt2 = tk.Button(frame, text='2', width=2, height=1, font=('Arial', 20))
bt3 = tk.Button(frame, text='3', width=2, height=1, font=('Arial', 20))
bt4 = tk.Button(frame, text='4', width=2, height=1, font=('Arial', 20))
bt5 = tk.Button(frame, text='5', width=2, height=1, font=('Arial', 20))
bt6 = tk.Button(frame, text='6', width=2, height=1, font=('Arial', 20))
bt7 = tk.Button(frame, text='7', width=2, height=1, font=('Arial', 20))
bt8 = tk.Button(frame, text='8', width=2, height=1, font=('Arial', 20))
bt9 = tk.Button(frame, text='9', width=2, height=1, font=('Arial', 20))
btA = tk.Button(frame, text='+', width=2, height=1, font=('Arial', 20))
btS = tk.Button(frame, text='-', width=2, height=1, font=('Arial', 20))
btM = tk.Button(frame, text='/', width=2, height=1, font=('Arial', 20))
btD = tk.Button(frame, text='x', width=2, height=1, font=('Arial', 20))
btI = tk.Button(frame, text='=', width=2, height=1, font=('Arial', 20))

bt0.grid(row=4, column=2, padx=8, pady=8)
bt1.grid(row=1, column=1, padx=8, pady=8)
bt2.grid(row=1, column=2, padx=8, pady=8)
bt3.grid(row=1, column=3, padx=8, pady=8)
bt4.grid(row=2, column=1, padx=8, pady=8)
bt5.grid(row=2, column=2, padx=8, pady=8)
bt6.grid(row=2, column=3, padx=8, pady=8)
bt7.grid(row=3, column=1, padx=8, pady=8)
bt8.grid(row=3, column=2, padx=8, pady=8)
bt9.grid(row=3, column=3, padx=8, pady=8)
btA.grid(row=1, column=4, padx=8, pady=8)
btS.grid(row=2, column=4, padx=8, pady=8)
btM.grid(row=3, column=4, padx=8, pady=8)
btD.grid(row=4, column=1, padx=8, pady=8)
btI.grid(row=4, column=3, padx=8, pady=8)


window.mainloop()