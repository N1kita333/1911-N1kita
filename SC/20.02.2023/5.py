import tkinter
import tkinter.messagebox

window = tkinter.Tk()

str_var = tkinter.StringVar()


def button_click():
    tkinter.messagebox.showinfo("Увага", "Сьогодні -"  + str_var.get())


label = tkinter.Label(window, text="Введiть день тижня:")
label.pack()

edit = tkinter.Entry(window, textvariable=str_var)
edit.pack()

button = tkinter.Button(window, text="гapaзд")
button.pack()

window.mainloop()
