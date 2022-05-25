import xlrd
import PySimpleGUI as sg
import addroute

def transport_cost(arg):
    #import addroute as rt
    import PySimpleGUI as sg
    rb = xlrd.open_workbook(r"C:\Users\Clo3\PycharmProjects\create_xml\данные по ДТ.xls",
                             encoding_override="cp1251")
    sheet = rb.sheet_by_index(1)
    vals = [sheet.row_values(rownum) for rownum in range(0, sheet.nrows)]
    route = []
    route.append([sg.Text('Транспортные расходы')])
    for i in range(0, len(vals)):
        if vals[i][0] == arg:
            #route.append([sg.Checkbox(vals[i][1] + " " + vals[i][2] + " " + vals[i][3], size=(30, 1), key= str(i))])
            route.append([sg.Radio(vals[i][1] + " " + vals[i][2] + " " + vals[i][3], 'RADIO1',size=(30, 1), key= str(i))])
    route.append([sg.Submit("Экспорт xml"), sg.Submit("Добавить")])
    #route.append([])

    layout = route


    window = sg.Window('File Compare', layout)

    while True:

        # The Event Loop
        event, win_values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break

        if event == 'Экспорт xml':
            for j in win_values:
                if win_values[j] is True:
                    window.close()
                    return vals[int(j)]

        if event == 'Добавить':
            window.close()
            addroute.add_route()



print(transport_cost("10/04-2015/03-0857"))

