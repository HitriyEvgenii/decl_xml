import xlrd
import PySimpleGUI as sg
import addroute

def transport_cost(arg, arg2):
    import sqlite3
    import PySimpleGUI as sg
    import addroute_tk as add_tk


    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    sql = "SELECT terms, city, border, transport_cost, id FROM routs WHERE contract=?"

    route = []
    route.append([sg.Text('Транспортные расходы Invoice ' + arg2)])

    for row in cursor.execute(sql, [(arg)]):
        route.append([sg.Radio(row[0] + " " + row[1] + ",  " + row[2] +
                              # ", Стоимость - " + row[3] + " USD", 'RADIO1',size=(50, 1), key=row[4])])
                               ", Стоимость - " + row[3] + " USD", 'RADIO1', key=row[4])])
    route.append([sg.Submit("Экспорт xml"), sg.Submit("Добавить"), sg.Submit("Удалить")])

    layout = route

    window = sg.Window(arg2, layout)

    while True:

        # The Event Loop
        event, win_values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break

        if event == 'Экспорт xml':
            for j in win_values:
                if win_values[j] is True:
                    route = cursor.execute("""SELECT * FROM routs WHERE id =?""", [(j)]).fetchall()
                    window.close()
                    return route

        if event == 'Добавить':
            window.close()
            #ad.add_route(arg)
            add_tk.add_route_tk(arg)
            break

        if event == 'Удалить':
            for j in win_values:
                if win_values[j] is True:
                    window.close()
                    cursor.execute("""DELETE FROM routs WHERE id =?""", [(j)])
                    conn.commit()

            window.close()
            #transport_cost(arg)



#transport_cost("10/04-2015/03-0857", '1')

