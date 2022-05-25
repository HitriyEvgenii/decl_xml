
def frame_col(arg, arg2):
    import PySimpleGUI as sg
    check, col, route, summa, summa_netto, summa_brutto, summa_mest = [], [], [], [], [], [], []

    invoices = list(arg.index)

    font = "Arial, 11"
    for i in range(0, len(invoices)):
        col.append([sg.Checkbox(invoices[i][0], size=(10, 1), key=arg2+str(i), default=True, enable_events=True, font=font),
                    sg.Text(text=round(arg['СтоимостьВАЛ'].values[i], 2), key=arg2+'T'+str(i), size=(10, 1), justification='RIGHT', font=font),
                    sg.Text(text=arg['ВесНетто'].values[i], key=arg2+'NETTO'+str(i), size=(10, 1), justification='RIGHT', font=font),
                   sg.Text(text=arg['ВесБрутто'].values[i], key=arg2+'BRUTTO' + str(i), size=(10, 1), justification='RIGHT', font=font),
                    sg.Text(text=arg['КоличествоМест'].values[i], key=arg2+'MEST' + str(i), size=(10, 1), justification='RIGHT', font=font),
                    ]
                   )
        summa.append(arg['СтоимостьВАЛ'].values[i])
        summa_netto.append(arg['ВесНетто'].values[i])
        summa_brutto.append(arg['ВесБрутто'].values[i])
        summa_mest.append(arg['КоличествоМест'].values[i])



        check.append(arg2+str(i))
    col.append([sg.Text(text='Итого', size=(13, 1), text_color='black', justification='center', font=font),
                sg.Text(text=round(sum(summa), 2), size=(10, 1), text_color='black', key=arg2+'-SUM-', justification='RIGHT', font=font),
                sg.Text(text=sum(summa_netto), size=(10, 1), text_color='black', key=arg2+'-NETTO-', justification='RIGHT', font=font),
                sg.Text(text=sum(summa_brutto), size=(10, 1), text_color='black', key=arg2+'-BRUTTO-', justification='RIGHT', font=font),
                sg.Text(text=round(sum(summa_mest), 0), size=(10, 1), text_color='black', key=arg2+'-MEST-', justification='RIGHT', font=font),
                ])
    return col, check

def group_invoices(arg):
    font = "Arial, 11"
    arg = arg.groupby(['НомерИнвойса', 'СТЗ', 'НомерДоговора'], dropna=False)[['СтоимостьВАЛ', 'ВесНетто', 'ВесБрутто', 'КоличествоМест']].sum()
    import PySimpleGUI as sg
    invoices = [i[0] for i in arg.index.to_list()]

    frames, col, route, summa, summa_netto, summa_brutto, summa_mest = [], [], [], [], [], [], []
    check = []
    arg1 = arg.groupby(['СТЗ'], dropna=False).sum()
    stz = arg.loc[arg.index.get_level_values('СТЗ') == 'СТЗ']
    not_stz = arg.loc[arg.index.get_level_values('СТЗ').isnull()]


    if len(arg1.index) == 2:
        frame_stz = frame_col(stz, 'CH')
        frame_not_stz = frame_col(not_stz, 'CHN')
        route.append([sg.Frame('CТЗ', frame_stz[0])]) #, sg.Column(frame_col(not_stz, 'CHN'))
        route.append([sg.Frame('ЭК', frame_not_stz[0])])  # , sg.Column(frame_col(not_stz, 'CHN'))
        check = frame_stz[1] + frame_not_stz[1]

    else:
        frame = frame_col(arg, 'CH')
        check = frame[1]
        if arg.index[0][1] == 'СТЗ':
            route.append([sg.Frame('СТЗ', frame[0])])
        else:
            route.append([sg.Frame('ЭК', frame_col(arg, 'CH')[0])])
    stroka = list(arg.sum())
    route.append([sg.T(text='Общий итог', size=(10, 1), justification='RIGHT', font=font),
                  sg.T(text=round(stroka[0],2), size=(10, 1), justification='RIGHT', font=font),
                  sg.T(text=int(stroka[1]), size=(10, 1), justification='RIGHT', font=font),
                  sg.T(text=int(stroka[2]), size=(10, 1), justification='RIGHT', font=font),
                  sg.T(text=int(stroka[3]), size=(10, 1), justification='RIGHT', font=font)]) # НИЖНИЙ ИТОГ


    layout = [[sg.Text('Инвойсы к договору')],
              [sg.Frame(arg.index[0][2], route, font='Any 11', title_color='black')],
              [sg.Submit("Экспорт xml"), sg.Submit("Добавить")]]

    window = sg.Window('File Compare', layout)

    while True:

        # The Event Loop
        event, win_values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event in check:
            if win_values[event] == False:
                t_sum = round(float(window[event[:-1]+'-SUM-'].get()) - float(window[event[:-1]+'T' + event[-1:]].get()), 2)
                window[event[:-1]+"-SUM-"].update(str(t_sum))
                t_sum = round(int(window[event[:-1]+'-NETTO-'].get()) - int(window[event[:-1]+'NETTO' + event[-1:]].get()), 2)
                window[event[:-1]+"-NETTO-"].update(str(t_sum))
                t_sum = round(int(window[event[:-1]+'-BRUTTO-'].get()) - int(window[event[:-1]+'BRUTTO' + event[-1:]].get()), 2)
                window[event[:-1]+"-BRUTTO-"].update(str(t_sum))
                t_sum = round((float(window[event[:-1]+'-MEST-'].get()) - float(window[event[:-1]+'MEST' + event[-1:]].get())), 0)
                window[event[:-1]+"-MEST-"].update(str(t_sum))

                invoices.remove(window[event].Text)

                #print(window[event].Text)
                print(invoices)

            else:
                t_sum = round(float(window[event[:-1]+'-SUM-'].get()) + float(window[event[:-1]+'T' + event[-1:]].get()), 2)
                window[event[:-1]+"-SUM-"].update(str(t_sum))
                t_sum = round(int(window[event[:-1]+'-NETTO-'].get()) + int(window[event[:-1]+'NETTO' + event[-1:]].get()), 2)
                window[event[:-1]+"-NETTO-"].update(str(t_sum))
                t_sum = round(int(window[event[:-1]+'-BRUTTO-'].get()) + int(window[event[:-1]+'BRUTTO' + event[-1:]].get()), 2)
                window[event[:-1]+"-BRUTTO-"].update(str(t_sum))
                t_sum = round((float(window[event[:-1]+'-MEST-'].get()) + float(window[event[:-1]+'MEST' + event[-1:]].get())), 0)
                window[event[:-1]+"-MEST-"].update(str(t_sum))

                invoices.append(window[event].Text)

        if event == 'Экспорт xml':
            #for j in win_values:
                #if win_values[j] is True:
            window.close()
            return invoices

       # if event == 'Добавить':
       #     window.close()
        #    addroute.add_route()

