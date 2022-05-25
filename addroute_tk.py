import tkinter as tk
from tkinter import ttk
import sqlite3

def add_route_tk(arg):
    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""SELECT country_name from countries order by country_name""")
    a_country = cursor.fetchall()


    app = tk.Tk()
    app.title('Маршрут')
    app.geometry('300x280+500+300')
    app.resizable(0, 0)

    labelTop = tk.Label(app, text="Добавить маршрут", bg="green", justify='center')
    labelTop.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W)

    label_1 = tk.Label(app, text="Условия поставки")
    label_1.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W)
    combo_1 = ttk.Combobox(app, values=["FCA",
                                    "DAP",
                                    "DDP"], width=15)
    combo_1.grid(column=1, row=1, ipadx=5, pady=5, sticky=tk.W)

    label_2 = tk.Label(app, text="Город")
    label_2.grid(column=0, row=2, ipadx=5, pady=5, sticky=tk.W)
    input_1 = tk.Entry(app, width=15)
    input_1.grid(column=1, row=2, ipadx=5, pady=5, sticky=tk.W)

    label_3 = tk.Label(app, text="Переход")
    label_3.grid(column=0, row=3, ipadx=5, pady=5, sticky=tk.W)
    input_2 = tk.Entry(app, width=15)
    input_2.grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.W)

    label_4 = tk.Label(app, text="Стоимость")
    label_4.grid(column=0, row=4, ipadx=5, pady=5, sticky=tk.W)
    input_3 = tk.Entry(app, width=15)
    input_3.grid(column=1, row=4, ipadx=5, pady=5, sticky=tk.W)

    def pressed():
        arg1 = str(combo_2.get()).upper()
        sql = 'SELECT country_name from countries where country_name LIKE "%' + arg1 + '%" order by country_name'
        cursor.execute(sql)
        abc = cursor.fetchall()
        abc2 = []
        for row in abc:
            abc2.append(row[0])

        #print(abc2)
        combo_2["values"] = abc2

    def pressed_2(event):
        value = combo_2.get()
        sql = 'SELECT country_code from countries WHERE country_name="' + value + '"'
        cursor.execute(sql)
        value_2 = str(cursor.fetchone()[0])
        input_5.delete(0, 'end')
        input_5.insert(0, value_2)


    label_5 = tk.Label(app, text="Код страны ввоза")
    label_5.grid(column=0, row=5, ipadx=5, pady=5, sticky=tk.W)
    combo_2 = ttk.Combobox(app, values=a_country, width=15, postcommand=pressed)
    combo_2.grid(column=1, row=5, ipadx=5, pady=5, sticky=tk.W)
    input_5 = tk.Entry(app, width=2)
    input_5.grid(column=2, row=5, ipadx=5, pady=5, sticky=tk.W)
    combo_2.bind('<<ComboboxSelected>>', pressed_2)

    label_6 = tk.Label(app, text="Код области")
    label_6.grid(column=0, row=6, ipadx=5, pady=5, sticky=tk.W)
    input_4 = tk.Entry(app, width=3)
    input_4.grid(column=1, row=6, ipadx=5, pady=5, sticky=tk.W)


    def command():
        conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor.execute("""SELECT id from routs""")
        a = [i[0] for i in cursor.fetchall()]
        if len(a) == 0:
            id_key = 1
        else:
            id_key = max(a) + 1

        input_3_value = input_3.get()
        input_3_value = float(input_3_value)
        input_3_value = int(input_3_value)
        args = [(id_key, arg, combo_1.get(), input_1.get(), input_2.get(), str(input_3_value), input_5.get(), input_4.get(),
             combo_2.get())]


        sql = ("""INSERT INTO routs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""")

        cursor.executemany(sql, args)
        conn.commit()
        cursor.close()
        conn.close()
        app.destroy()
        app.quit()
        #command = lambda: print(combo_1.get(), input_1.get(), input_2.get(), input_3.get(), combo_2.get(), input_4.get())
    button = ttk.Button(app, text= 'Добавить', command=command)
    button.grid(column=0, row=10, ipadx=5, pady=5, sticky=tk.W)



    app.mainloop()

#add_route_tk('27/02-2019')