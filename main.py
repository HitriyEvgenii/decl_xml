#version v.2.1.2

import pandas
import group_by_invoices_pys as gbip
import create_decl_v2 as cd_v2
import transport_cost_with_lite as tc
import etc_functions as ef
import PySimpleGUI as sg
import xlrd
import filter_route_ttk as frt

CURRENCY_TODAY = ef.CURRENCY_TODAY

#ur1 = r"C:\Users\Clo3\PycharmProjects\create_xml"
ur1 = r"C:\Prg\otch"


#url1 = r"C:\Users\Clo3\PycharmProjects\create_xml"
url1 = r"\\First\таможня\бараб"


layout = [
    [sg.Text('File 1'), sg.InputText(default_text=ur1+"\зпрТранспортЗаявки_ПечатьИнфо.xls"), sg.FileBrowse()],
    [sg.Radio('Москальков', 'RADIO1', default=True, size=(10,1)), sg.Radio('Волчек', "RADIO1")],
    #[sg.Output(size=(88, 20))],
    [sg.Submit("Экспорт xml"), sg.Cancel(), sg.Submit("Маршруты")]]

window = sg.Window('File Compare', layout)

while True:

    # The Event Loop
    event, win_values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Маршруты':
        root = frt.App_filter()
        root.mainloop()


    if event == 'Экспорт xml':
        cd_v2.create_xml.win_value = win_values[1]
        #url1 = win_values[0]
        workbook = xlrd.open_workbook(ur1 + '\зпрТранспортЗаявки_ПечатьИнфо.xls', encoding_override='cp1251')
        data = pandas.read_excel(workbook, sheet_name=0, dtype=object)
        workbook2 = xlrd.open_workbook(url1+"\данные по ДТ.xls", encoding_override='cp1251')
        data_c = pandas.read_excel(workbook2, sheet_name=0, dtype=object)
        while len(data) > 0:
            contracts = list(data['НомерДоговора'].unique())
            try:
                for contract in contracts:
                    data_v = data_c[data_c['НомерДоговора'] == contract.split(' ')[0]].astype(object)  # data contract
                    if len(data_v) == 0:
                        data = pandas.DataFrame()
                        sg.popup(f"Отсутствует договор в базе №{contract}!!!")
                        break
                    cd_v2.create_xml.contract_data = data_v
                    invoices = gbip.group_invoices(data[data['НомерДоговора'] == contract])
                    if invoices is None:
                        data = pandas.DataFrame()
                        break
                    data_xml = data.query('НомерИнвойса in @invoices')
                    data = data.query('НомерИнвойса not in @invoices')
                    data_xml_stz = data_xml[data_xml['СТЗ'] == "СТЗ"]
                    data_xml_not_stz = data_xml[data_xml['СТЗ'] != "СТЗ"]
                    print(data_xml['ВалютаПоИнвойсу'].unique())
                    currency = CURRENCY_TODAY[data_xml['ВалютаПоИнвойсу'].unique()[0]]
                    if currency[1] == 1:
                        cd_v2.create_xml.currency = str(currency[0])
                        cd_v2.create_xml.scaleN = "0"
                    else:
                        cd_v2.create_xml.currency = str(currency[0])
                        cd_v2.create_xml.scaleN = "2"

                    truck_1 = data_xml['НомерАвто'].unique()[0]
                    truck_2 = data_xml['НомерПрицепа'].unique()[0]
                    cd_v2.create_xml.truck_1 = truck_1.replace(" ", "").upper()
                    cd_v2.create_xml.truck_2 = truck_2.replace(" ", "").upper()
                    trucks = ef.country_truck(data_xml['НомерАвто'].unique()[0], data_xml['НомерПрицепа'].unique()[0])
                    cd_v2.create_xml.truck_1_country_name = trucks[0]
                    cd_v2.create_xml.truck_2_country_name = trucks[1]

                    if len(data_xml_stz) > 0:
                        data_transport_cost = tc.transport_cost(contract.split(' ')[0],
                                                            ', '.join([str(i) for i in data_xml_stz['НомерИнвойса'].unique().tolist()]))
                        while data_transport_cost is None:
                            data_transport_cost = tc.transport_cost(contract.split(' ')[0],
                                                                    ', '.join([str(i) for i in data_xml_stz[
                                                                        'НомерИнвойса'].unique().tolist()]))
                            #break
                        xml_stz = cd_v2.create_xml()
                        xml_stz.goodsQ = str(len(data_xml_stz['КодТНВЭД'].unique()))
                        xml_stz.cargoQ = str(data_xml_stz['КоличествоМест'].sum())
                        xml_stz.decl_number = 'ИСХ.' + str(data_xml_stz['НомерИнвойса'].unique()) + 'СТЗ'
                        if xml_stz.goodsQ == '1':
                            xml_stz.PageQ = "1"
                        else:
                            xml_stz.PageQ = str(1 + (int((int(xml_stz.goodsQ) - 1) / 3) + 1))
                        xml_stz.GoodsLocationCode = "80"
                        xml_stz.PreviousCustomsProcedureModeCode = "78"
                        xml_stz.GoodsMoveFeatureCode = "102"
                        xml_stz.root_elements()
                        xml_stz.DeclGoodsShipmentDetails(data_xml_stz, data_transport_cost)
                        xml_stz.save_xml(str(data_xml_stz['НомерИнвойса'].unique()) + '_СТЗ')
                        del xml_stz

                    if len(data_xml_not_stz) > 0:
                        data_transport_cost = tc.transport_cost(contract.split(' ')[0],
                                                            ', '.join([str(i) for i in data_xml_not_stz['НомерИнвойса'].unique().tolist()]))
                        while data_transport_cost is None:
                            data_transport_cost = tc.transport_cost(contract.split(' ')[0],
                                                                    ', '.join([str(i) for i in data_xml_not_stz[
                                                                        'НомерИнвойса'].unique().tolist()]))
                            #break
                        xml_not_stz = cd_v2.create_xml()
                        xml_not_stz.goodsQ = str(len(data_xml_not_stz['КодТНВЭД'].unique()))
                        xml_not_stz.cargoQ = str(data_xml_not_stz['КоличествоМест'].sum())
                        xml_not_stz.decl_number = 'ИСХ.' + str(data_xml_not_stz['НомерИнвойса'].unique()) + 'К'
                        if xml_not_stz.goodsQ == '1':
                            xml_not_stz.PageQ = "1"
                        else:
                            xml_not_stz.PageQ = str(1 + (int((int(xml_not_stz.goodsQ) - 1) / 3) + 1))
                        xml_not_stz.GoodsLocationCode = "60"
                        xml_not_stz.PreviousCustomsProcedureModeCode = "00"
                        xml_not_stz.GoodsMoveFeatureCode = "000"
                        xml_not_stz.root_elements()
                        xml_not_stz.DeclGoodsShipmentDetails(data_xml_not_stz, data_transport_cost)
                        xml_not_stz.save_xml(str(data_xml_not_stz['НомерИнвойса'].unique()) + '_К')
                        del xml_not_stz
                    sg.Popup("Готово")
            except LookupError:
                print(LookupError)


