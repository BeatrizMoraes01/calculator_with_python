# importar modulo tkinter
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#3b3b3b" #black
cor2 = "#feffff" #white
cor3 = "#37474F" #black-
cor4 = "#424345"

fundo = "#e8e6e6"
cor10 = "#363434"

# janela principal

janela = Tk()
janela.title("Calculator")
janela.geometry("235x287")
janela.config(bg=cor1)

# frames resultado

frame_tela = Frame(janela, width=300, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

# frames cientifica

frame_cientifica = Frame(janela, width=300, height=86)
frame_cientifica.grid(row=1, column=0)

# frames outras operações

frame_corpo = Frame(janela, width=300, height=340)
frame_corpo.grid(row=2, column=0)

# config tela
label_tela = Label(frame_tela, text='123456789', width=16, height=2, bg=cor3, padx=7, anchor='e', bd=0, justify=RIGHT, font=('Ivi 18'), fg=cor2)
label_tela.place(x=0, y=0)

# botões cientificos

b_0 = Button(frame_cientifica, text='tan', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica, text='sin', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=59, y=0)
b_2 = Button(frame_cientifica, text='cos', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=118, y=0)
b_3 = Button(frame_cientifica, text='sqrt', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_3.place(x=177, y=0)

b_0 = Button(frame_cientifica, text='log', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=29)
b_1 = Button(frame_cientifica, text='log10', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=59, y=29)
b_2 = Button(frame_cientifica, text='e', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=118, y=29)
b_3 = Button(frame_cientifica, text='pow', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_3.place(x=177, y=29)

b_0 = Button(frame_cientifica, text='pi', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=58)
b_1 = Button(frame_cientifica, text=',', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=59, y=58)
b_2 = Button(frame_cientifica, text='(', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=118, y=58)
b_3 = Button(frame_cientifica, text=')', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_3.place(x=177, y=58)

# botões outras operações

b_0 = Button(frame_corpo, text='C', width=14, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_corpo, text='%', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=118, y=0)
b_2 = Button(frame_corpo, text='/', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=177, y=0)


b_0 = Button(frame_corpo, text='7', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=29)
b_1 = Button(frame_corpo, text='8', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=59, y=29)
b_2 = Button(frame_corpo, text='9', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=118, y=29)
b_3 = Button(frame_corpo, text='*', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, font=('Ivi 10 bold'), fg=cor2)
b_3.place(x=177, y=29)

b_0 = Button(frame_corpo, text='4', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=58)
b_1 = Button(frame_corpo, text='5', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=59, y=58)
b_2 = Button(frame_corpo, text='6', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=118, y=58)
b_3 = Button(frame_corpo, text='-', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, font=('Ivi 10 bold'), fg=cor2)
b_3.place(x=177, y=58)

b_0 = Button(frame_corpo, text='1', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=87)
b_1 = Button(frame_corpo, text='2', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=59, y=87)
b_2 = Button(frame_corpo, text='3', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=118, y=87)
b_3 = Button(frame_corpo, text='+', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, font=('Ivi 10 bold'), fg=cor2)
b_3.place(x=177, y=87)

b_0 = Button(frame_corpo, text='0', width=14, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_0.place(x=0, y=116)
b_1 = Button(frame_corpo, text='.', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor1, font=('Ivi 10 bold'), fg=cor2)
b_1.place(x=118, y=116)
b_2 = Button(frame_corpo, text='=', width=6, height=1, relief=RAISED, overrelief=RIDGE, bg=cor4, font=('Ivi 10 bold'), fg=cor2)
b_2.place(x=177, y=116)


# executor
janela.mainloop()