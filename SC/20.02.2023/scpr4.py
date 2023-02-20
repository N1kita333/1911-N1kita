import tkinter

window = tkinter.Tk()
window.title('Bпpава 1')
window.geometry('400x300')
button1 = tkinter.Button(window, text='blue',
                         width=10, height=1,
                         bg='blue', fg='yellow', font='Arial 14')

button1.pack()
button2 = tkinter.Button(window, text='yellow',
                         width=10, height=1,
                         bg='yellow', fg='blue', font='Arial 14')

button2.pack()
button3 = tkinter.Button(window, text='green',
                         width=10, height=1,
                         bg='green', fg='black', font='Arial 14')

button3.pack()
button4 = tkinter.Button(window, text='purple',
                         width=10, height=1,
                         bg='purple', fg='black', font='Arial 14')

button4.pack()
window.mainloop()
