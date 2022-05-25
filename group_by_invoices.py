from tkinter import *
from tkinter.ttk import Checkbutton, LabelFrame




def group_invoices(arg):
    print(arg)
    window = Tk()
    window.title("Добро пожаловать в приложение PythonRu")
    window.geometry('400x250')

    invoices = list(arg.index)
    group_1 = LabelFrame(window, text="СТЗ")
    group_1.pack(side=TOP)

    # group_1.pack(padx=10, pady=5)

    lb1_list = []

    def print_value():
        print(checkbutton.info)

    choice = []
    for i in range(0, len(invoices)):
        choice.append(IntVar())
        checkbutton = Checkbutton(group_1, variable=choice[-1], name='var'+str(i), onvalue=1, offvalue=-5, command=print_value)
        checkbutton.grid(row=i, column=0)
        checkbutton.state(['!alternate'])
        checkbutton.state(['selected'])
        # print(checkbutton.state())
        #print(var)

        name = IntVar(group_1, value=arg['СтоимостьВАЛ'].values[i])
        lb1 = Entry(group_1, textvariable=name, width=10, bg='red')
        lb1.grid(row=i, column=1)

        lb2 = Label(group_1, text=arg['ВесНетто'].values[i], width=10, bg='red', anchor='e')
        lb2.grid(row=i, column=2)

        lb3 = Label(group_1, text=arg['ВесБрутто'].values[i], width=10, bg='red', anchor='e')
        lb3.grid(row=i, column=3)

        lb4 = Label(group_1, text=arg['КоличествоМест'].values[i])
        lb4.grid(row=i, column=4)

        lb1_list.append(float((lb1.get())))
        #print(lb1_list)

    lb5 = Label(group_1, text='Итого')
    lb5.grid(row=len(invoices), column=0)

    lb6 = Label(group_1, text=sum(lb1_list))
    lb6.grid(row=len(invoices), column=1)

    window.bind()

    window.mainloop()


