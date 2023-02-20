import tkinter
import tkinter.messagebox


def button1_click():
    print('Слова Павла Чубинського')


def button2_click():
    tkinter.messagebox.showinfo("Відповідь", "Музика Михайла Вербицького")


window = tkinter.Tk()
window.title('Bправа 2')
window.geometry('400x300')
label1 = tkinter.Label(text="Aвтори гiмну украïни")
label1.pack()
button1 = tkinter.Button(window, text="Cлова!", command=button1_click)
button1.pack()
button2 = tkinter.Button(window, text="Музикa!", command=button2_click)
button2.pack()
window.mainloop()
