

def add_route(arg):
    import PySimpleGUI as sg
    import sqlite3

    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""SELECT country_name from countries order by country_code""")
    #a_country = [i for i in cursor.fetchall()]
    a_country = cursor.fetchall()


    layout = [[sg.Text("Условия поставки", size=(16, 1)), sg.Combo(values=["DDP", "DAP", "FCA"], size=(10, 3))],
              [sg.Text("Город", size=(16, 1)), sg.InputText(size=(15, 2))],
              [sg.Text("Переход", size=(16, 1)), sg.InputText(size=(15, 2))],
              [sg.Text("Стоимость", size=(16, 1)), sg.InputText(size=(15, 2))],
              [sg.Text("Код страны ввоза", size=(16, 1)),
               sg.InputCombo(values=a_country, size=(20, 5), key='-INN-', enable_events=True)],
              [sg.Text("Код области", size=(16, 1)), sg.Input(size=(3, 1), key="OUT", enable_events=True)],
               [sg.Submit("Добавить")]]

    window = sg.Window('Добавить Маршрут', layout, finalize=True)

    def pressed():
        #abc = str(win_values['-INN-'][0])
        #print(abc)
        sql = 'SELECT * from countries where country_name LIKE "%' + str(win_values['-INN-']).upper() + '%"'
        cursor.execute(sql)
        #window['-INN-'].set_value()
        abc = cursor.fetchall()
        print(abc)
        window['-INN-'].update(values=abc)


    while True:

        # The Event Loop
        event, win_values = window.read()
        #value = win_values[OUT]
        #print(value)0
        if event in (None, 'Exit', 'Cancel'):
            break

        window['-INN-'].bind('<Key>', pressed())

        if event == 'OUT' and len(win_values['OUT']) > 2:
            window.Element('Добавить').SetFocus()
        if event == 'Добавить':

            conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
            cursor = conn.cursor()
            cursor.execute("""SELECT id from routs""")
            a = [i[0] for i in cursor.fetchall()]
            if len(a) == 0:
                id_key = 1
            else:
                id_key = max(a) + 1

            args = [(id_key, arg, win_values[0], win_values[1], win_values[2], win_values[3], win_values[4][0], win_values[5], win_values[4][1])]

            sql = ("""INSERT INTO routs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""")

            cursor.executemany(sql, args)
            conn.commit()
            cursor.close()
            conn.close()
            window.close()

def del_route(arg):
    import sqlite3
    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    # Создание таблицы
    sql = ("""DELETE FROM routs WHERE id=?)""")

    cursor.execute(sql, arg)
    # Сохраняем изменения
    conn.commit()

    cursor.close()
    conn.close()

#add_route("10/04-2015/03-0857")

