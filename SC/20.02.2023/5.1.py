import tkinter
import tkinter.messagebox

window = tkinter.Tk()
str_var = tkinter.StringVar()


def button_click():
    tkinter.messagebox.showinfo("Увагa!", "Cьогоднi - " + str_var.get())


label = tkinter.Label(window, text="Введіть день Тижня:")
label.pack()
edit = tkinter.Entry(window, textvariable=str_var)
edit.pack()
button = tkinter.Button(window, text="Гapaзд", command=button_click)
button.pack()
window.mainloop()
