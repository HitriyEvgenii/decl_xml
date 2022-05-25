import requests
def country_truck(arg1, arg2):
    import PySimpleGUI as sg

    layout = [[sg.Text('Тягач ', size=(6, 1)), sg.Text(arg1, size=(10, 1)), sg.Radio('BY', 'tr', key='BY', default=True),
                        sg.Radio('RU', 'tr',key='RU'), sg.Radio('PL', 'tr', key='PL'), sg.Radio('LT', 'tr', key='LT'),
               sg.Radio('LV', 'tr', key='LV')],
                       [sg.Text('Прицеп', size=(6, 1)), sg.Text(arg2, size=(10, 1)), sg.Radio('BY', 'tra', key='BY1', default=True),
                        sg.Radio(text='RU',group_id='tra', key='RU1'), sg.Radio('PL', 'tra', key='PL1'), sg.Radio('LT', 'tra', key='LT1')
                           , sg.Radio('LV', 'tra', key='LV1')],
                        [sg.Submit("Добавить")]]

    window = sg.Window('File Compare', layout)

    while True:

        # The Event Loop
        event, win_values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == 'Добавить':
            tr1 = []

            for i in win_values:
                if win_values[i] is True:
                    tr1.append(window[i].Text)
            window.close()
            return tr1
#def currency(arg):
    #import requests
    #response_cur = requests.get(f'https://www.nbrb.by/api/exrates/rates/{arg}?parammode=2').json()
    #return response_cur['Cur_OfficialRate'], response_cur['Cur_Scale']

def currency_dict():
    import requests
    #response_cur = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0', verify=False).json()
    response_cur = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0', verify=False).json()
    currence_dict = {i['Cur_Abbreviation']: [i['Cur_OfficialRate'], i['Cur_Scale']] for i in response_cur }
    #response_cur = [i for i in response_cur if i['Cur_Abbreviation'] == arg]
    #return response_cur[0]['Cur_OfficialRate'], response_cur[0]['Cur_Scale']
    return currence_dict

def currency(arg):
    import requests

    response_cur = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0', verify=False).json()
    #response_cur = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0', verify=False).json()
    #currence_dict = {i['Cur_Abbreviation']: [i['Cur_OfficialRate'], i['Cur_Scale']] for i in response_cur }
    response_cur = [i for i in response_cur if i['Cur_Abbreviation'] == arg]
    return response_cur[0]['Cur_OfficialRate'], response_cur[0]['Cur_Scale']
    #return currence_dict

CURRENCY_TODAY = currency_dict()

#if CURRENCY_TODAY.__len__() != 0:

#    CURRENCY_TODAY = currency_dict()
#    print(CURRENCY_TODAY.__len__())
#else:
#    CURRENCY_TODAY = currency_dict()
