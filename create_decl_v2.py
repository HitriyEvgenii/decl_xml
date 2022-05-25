#version v.2.1.2

import xml  .etree.ElementTree as xml
from datetime import datetime, timedelta
import pandas as pd

class create_xml:

    def __init__(self, pageQ=1, goodsQ=1, cargoQ=1):
        self.pageQ = str(pageQ)
        self.goodsQ = str(goodsQ)
        self.cargoQ = str(cargoQ)
        self.root = xml.Element("gd:GoodsDeclaration")
        #self.node1 = xml.Element("")
        #self.subnode = xml.SubElement(self.node1, "cacdo:ConsigneeDetails")
       # self.subnode2 = xml.SubElement(self.subnode, '')
        #self.subnode3 = xml.SubElement(self.subnode2, '')
        #self.subnode3.text = ''

    def root_elements(self):


        self.root = xml.Element("gd:GoodsDeclaration")
        self.root.set("xmlns:csdo", "urn:EEC:M:SimpleDataObjects:v0.4.10")
        self.root.set("xmlns:casdo", "urn:EEC:M:CA:SimpleDataObjects:v1.5.1")
        self.root.set("xmlns:ccdo", "urn:EEC:M:ComplexDataObjects:v0.4.10")
        self.root.set("xmlns:cacdo", "urn:EEC:M:CA:ComplexDataObjects:v1.5.1")
        self.root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.root.set("xmlns:gd", "urn:EEC:R:036:GoodsDeclaration:v1.1.0")
        self.root.set("xsi:schemaLocation", "urn:EEC:R:036:GoodsDeclaration:v1.1.0")

        EDocCode = xml.Element("csdo:EDocCode")
        self.root.append(EDocCode)
        EDocCode.text = "R.036"

        EDocId = xml.Element("csdo:EDocId")
        self.root.append(EDocId)
        EDocId.text = "709D924C-C0A8-010F-015D-8D622449EE71"

        EDocDateTime = xml.Element("csdo:EDocDateTime")
        self.root.append(EDocDateTime)
        EDocDateTime.text = str(datetime.now().date()) + "T00:00:00"

        DeclarationKindCode = xml.Element("casdo:DeclarationKindCode")
        self.root.append(DeclarationKindCode)
        DeclarationKindCode.text = "ЭК"

        CustomsProcedureCode = xml.Element("casdo:CustomsProcedureCode", codeListId="2002")
        self.root.append(CustomsProcedureCode)
        CustomsProcedureCode.text = "10"

        EDocIndicatorCode = xml.Element("casdo:EDocIndicatorCode")
        self.root.append(EDocIndicatorCode)
        EDocIndicatorCode.text = "ЭД"

        PageQuantity = xml.Element("csdo:PageQuantity")
        self.root.append(PageQuantity)
        PageQuantity.text = self.pageQ

        GoodsQuant = xml.Element("casdo:GoodsQuantity")
        self.root.append(GoodsQuant)
        GoodsQuant.text = self.goodsQ

        CargoQuantity = xml.Element("casdo:CargoQuantity")
        self.root.append(CargoQuantity)
        CargoQuantity.text = self.cargoQ

        create_xml.dDetails(self)

        #create_xml.DeclGoodsShipmentDetails(self, data_v)

        workers = [['ЕВГЕНИЙ', 'ВЛАДИМИРОВИЧ', 'МОСКАЛЬКОВ', 'СПЕЦИАЛИСТ', 'ВМ1469628', '2006-07-19', '2026-04-15'
                       , '296', '2006-08-02'],
                   ['ВЛАДИМИР', 'АНАТОЛЬЕВИЧ', 'ВОЛЧЁК', 'ВЕДУЩИЙ СПЕЦИАЛИСТ', 'ВМ2059805', '2012-12-21', '2022-12-21'
                       , '144', '2018-09-27']
                   ]
        if self.win_value == True:
            ind = workers[0]
        else:
            ind = workers[1]

        node1 = xml.Element("cacdo:SignatoryPersonV2Details")
        self.root.append(node1)
        subnode2 = xml.SubElement(node1, "cacdo:SigningDetails")
        subnode3 = xml.SubElement(subnode2, "ccdo:FullNameDetails")
        subnode4 = xml.SubElement(subnode3, "csdo:FirstName")
        subnode4.text = ind[0]
        subnode4 = xml.SubElement(subnode3, "csdo:MiddleName")
        subnode4.text = ind[1]
        subnode4 = xml.SubElement(subnode3, "csdo:LastName")
        subnode4.text = ind[2]
        subnode3 = xml.SubElement(subnode2, "csdo:PositionName")
        subnode3.text = ind[3]
        subnode3 = xml.SubElement(subnode2, "ccdo:CommunicationDetails")
        subnode4 = xml.SubElement(subnode3, "csdo:CommunicationChannelCode")
        subnode4.text = "TE"
        subnode4 = xml.SubElement(subnode3, "csdo:CommunicationChannelName")
        subnode4.text = "ТЕЛЕФОН"
        subnode4 = xml.SubElement(subnode3, "csdo:CommunicationChannelId")
        subnode4.text = "+375 212 480124"
        subnode3 = xml.SubElement(subnode2, "casdo:SigningDate")
        subnode3.text = str(datetime.now().date())

        subnode2 = xml.SubElement(node1, "ccdo:IdentityDocV3Details")
        subnode3 = xml.SubElement(subnode2, "csdo:UnifiedCountryCode", codeListId="2021")
        subnode3.text = "BY"
        subnode3 = xml.SubElement(subnode2, "csdo:IdentityDocKindCode", codeListId="2053")
        subnode3.text = "BY01001"
        subnode3 = xml.SubElement(subnode2, "csdo:DocId")
        subnode3.text = ind[4]
        subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
        subnode3.text = ind[5]
        subnode3 = xml.SubElement(subnode2, "csdo:DocValidityDate")
        subnode3.text = ind[6]

        subnode2 = xml.SubElement(node1, "cacdo:PowerOfAttorneyDetails")
        subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
        subnode3.text = "11004"
        subnode3 = xml.SubElement(subnode2, "csdo:DocId")
        subnode3.text = ind[7]
        subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
        subnode3.text = ind[8]

        node1 = xml.Element("casdo:InternalDocId")
        self.root.append(node1)
        node1.text = self.decl_number

        #return self.root

    def dDetails(self):
        declarantDetails = xml.Element("cacdo:DeclarantDetails")
        self.root.append(declarantDetails)

        SubjectBriefName = xml.SubElement(declarantDetails, "csdo:SubjectBriefName")
        SubjectBriefName.text = 'ООО ' + '"ПО"' + 'ЭНЕРГОКОМПЛЕКТ"'

        TaxpayerId = xml.SubElement(declarantDetails, "csdo:TaxpayerId")
        TaxpayerId.text = '300528652'

        SubjectAddressDetails = xml.Element("ccdo:SubjectAddressDetails")
        declarantDetails.append(SubjectAddressDetails)

        UnifiedCountryCode = xml.SubElement(SubjectAddressDetails, "csdo:UnifiedCountryCode", codeListId="2021")
        UnifiedCountryCode.text = "BY"

        CityName = xml.SubElement(SubjectAddressDetails, "csdo:CityName")
        CityName.text = "ВИТЕБСК"

        StreetName = xml.SubElement(SubjectAddressDetails, "csdo:StreetName")
        StreetName.text = "МОСКОВСКИЙ ПР-Т"

        BuildingNumberId = xml.SubElement(SubjectAddressDetails, "csdo:BuildingNumberId")
        BuildingNumberId.text = "94Б"

        PostCoded = xml.SubElement(SubjectAddressDetails, "csdo:PostCode")
        PostCoded.text = "210036"

        RegisterDocumentIdDetails = xml.Element("cacdo:RegisterDocumentIdDetails")
        declarantDetails.append(RegisterDocumentIdDetails)

        UnifiedCountryCode = xml.SubElement(RegisterDocumentIdDetails, "csdo:UnifiedCountryCode", codeListId="2021")
        UnifiedCountryCode.text = "BY"

        RegistrationNumberId = xml.SubElement(RegisterDocumentIdDetails, "casdo:RegistrationNumberId")
        RegistrationNumberId.text = "BY/0119/ТИП3"

    def DeclGoodsShipmentDetails(self, data, data_transport_cost):
        self.transport_cost = int(data_transport_cost[0][5])

        node1 = xml.Element("cacdo:DeclarationGoodsShipmentDetails")
        self.root.append(node1)

        subnode = xml.SubElement(node1, "cacdo:DepartureCountryDetails")
        subnode2 = xml.SubElement(subnode, "casdo:CACountryCode", codeListId="2021")
        subnode2.text = "BY"
        subnode2 = xml.SubElement(subnode, "casdo:ShortCountryName")
        subnode2.text = "БЕЛАРУСЬ"
        subnode2 = xml.SubElement(subnode, "csdo:TerritoryCode")
        subnode2.text = "000"

        subnode = xml.SubElement(node1, "cacdo:DestinationCountryDetails")
        subnode2 = xml.SubElement(subnode, "casdo:CACountryCode", codeListId="2021")
        subnode2.text = str(data_transport_cost[0][6])
        subnode2 = xml.SubElement(subnode, "casdo:ShortCountryName")
        subnode2.text = str(data_transport_cost[0][8])
        subnode2 = xml.SubElement(subnode, "csdo:TerritoryCode")
        subnode2.text = str(data_transport_cost[0][7])

        subnode = xml.SubElement(node1, "cacdo:TradeCountryDetails")
        subnode2 = xml.SubElement(subnode, "casdo:CACountryCode", codeListId="2021")
        subnode2.text = str(self.contract_data['Код'][self.contract_data.index[0]])

        subnode2 = xml.SubElement(subnode, "csdo:TerritoryCode")
        subnode2.text = str(self.contract_data['КодТерритории'][self.contract_data.index[0]])

        subnode = xml.SubElement(node1, "cacdo:DeliveryTermsDetails")
        subnode2 = xml.SubElement(subnode, "casdo:DeliveryTermsCode", codeListId="2014")
        subnode2.text = str(data_transport_cost[0][2])
        subnode2 = xml.SubElement(subnode, "casdo:PlaceName")
        subnode2.text = str(data_transport_cost[0][3])
        subnode2 = xml.SubElement(subnode, "casdo:DeliveryKindCode")
        subnode2.text = "02"

        subnode = xml.SubElement(node1, "casdo:CAValueAmount", currencyCode=data['ВалютаПоИнвойсу'][data.index[0]],
                                 currencyCodeListId="2022")
        subnode.text = str(round(data['СтоимостьВАЛ'].sum(), 2))


        subnode = xml.SubElement(node1, "casdo:ExchangeRate", currencyCode=data['ВалютаПоИнвойсу'][data.index[0]],
                                 currencyCodeListId="2022", scaleNumber=self.scaleN)
        subnode.text = str(self.currency) # курс


        subnode = xml.SubElement(node1, "cacdo:ConsignorDetails")
        subnode2 = xml.SubElement(subnode, "casdo:EqualIndicator")
        subnode2.text = "1"

        subnode = xml.SubElement(node1, "cacdo:ConsigneeDetails")
        subnode2 = xml.SubElement(subnode, "csdo:SubjectBriefName")
        subnode2.text = str(self.contract_data['НаименованиеОрганизации'][self.contract_data.index[0]])
        subnode2 = xml.SubElement(subnode, "ccdo:SubjectAddressDetails")
        subnode3 = xml.SubElement(subnode2, "csdo:UnifiedCountryCode", codeListId="2021")
        subnode3.text = str(self.contract_data['Код'][self.contract_data.index[0]])
        subnode3 = xml.SubElement(subnode2, "csdo:CityName")
        subnode3.text = str(self.contract_data['Город'][self.contract_data.index[0]])
        subnode3 = xml.SubElement(subnode2, "csdo:StreetName")
        subnode3.text = str(self.contract_data['Улица'][self.contract_data.index[0]])
        subnode3 = xml.SubElement(subnode2, "csdo:BuildingNumberId")
        subnode3.text = str(self.contract_data['НомерДома'][self.contract_data.index[0]])
        subnode3 = xml.SubElement(subnode2, "csdo:PostCode")
        subnode3.text = str(self.contract_data['Индекс'][self.contract_data.index[0]])

        subnode = xml.SubElement(node1, "cacdo:FinancialSettlementSubjectDetails")
        subnode2 = xml.SubElement(subnode, "casdo:EqualIndicator")
        subnode2.text = "1"

        subnode = xml.SubElement(node1, "cacdo:OriginCountryDetails")
        subnode2 = xml.SubElement(subnode, "casdo:CACountryCode", codeListId="2021")
        subnode2.text = "BY"
        subnode2 = xml.SubElement(subnode, "casdo:ShortCountryName")
        subnode2.text = "БЕЛАРУСЬ"

        subnode = xml.SubElement(node1, "cacdo:TransactionNatureDetails")
        subnode2 = xml.SubElement(subnode, "casdo:TransactionNatureCode")
        subnode2.text = "201"
        subnode2 = xml.SubElement(subnode, "casdo:TransactionFeatureCode")
        subnode2.text = "21"

        subnode = xml.SubElement(node1, "cacdo:DeclarationConsignmentDetails")
        subnode2 = xml.SubElement(subnode, "casdo:ContainerIndicator")
        subnode2.text = "0"
        subnode2 = xml.SubElement(subnode, "cacdo:BorderTransportDetails")
        subnode3 = xml.SubElement(subnode2, "csdo:UnifiedTransportModeCode", codeListId="2004")
        subnode3.text = "31"
        subnode3 = xml.SubElement(subnode2, "casdo:RegistrationNationalityCode", codeListId="2021")
        subnode3.text = self.truck_1_country_name
        subnode3 = xml.SubElement(subnode2, "casdo:TransportMeansQuantity")
        subnode3.text = "2"
        subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
        subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=self.truck_1_country_name,
                                  countryCodeListId="2021") #countryCode='ct[0]'
        subnode4.text = self.truck_1 #truck  # номер тягача
        subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
        subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=self.truck_2_country_name,
                                  countryCodeListId="2021")
        subnode4.text = self.truck_2 #trailer  # номер полуприцепа
        subnode2 = xml.SubElement(subnode, "cacdo:ArrivalDepartureTransportDetails")
        subnode3 = xml.SubElement(subnode2, "casdo:RegistrationNationalityCode", codeListId="2021")
        subnode3.text = self.truck_1_country_name
        subnode3 = xml.SubElement(subnode2, "casdo:TransportMeansQuantity")
        subnode3.text = "2"
        subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
        subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=self.truck_1_country_name, countryCodeListId="2021") #countryCode='ct[0]'
        subnode4.text = self.truck_1
        subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
        subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=self.truck_2_country_name,   #countryCode='ct[1][:-1]'
                                  countryCodeListId="2021")
        subnode4.text = self.truck_2

        subnode = xml.SubElement(node1, "cacdo:GoodsLocationDetails")
        subnode2 = xml.SubElement(subnode, "casdo:GoodsLocationCode", codeListId="2023")
        subnode2.text = self.GoodsLocationCode

        subnode2 = xml.SubElement(subnode, "csdo:CustomsOfficeCode")
        subnode2.text = "07000"
        subnode2 = xml.SubElement(subnode, "casdo:CustomsControlZoneId")
        subnode2.text = "ПЗ07260/0001129"

        i = 1
        for code in data['КодТНВЭД'].unique():
            subnode = xml.SubElement(node1, "cacdo:DeclarationGoodsItemDetails")
            data_item = data[data['КодТНВЭД'] == code]
            self.GoodsItemDetails(subnode, data_item, i)
            i += 1

    def GoodsItemDetails(self, subnode, data_item, i):
        from etc_functions import CURRENCY_TODAY
        #import etc_functions as ef

        subnode2 = xml.SubElement(subnode, "casdo:ConsignmentItemOrdinal")
        subnode2.text = str(i)

        subnode2 = xml.SubElement(subnode, "csdo:CommodityCode")
        code = data_item['КодТНВЭД'].unique()[0]
        subnode2.text = str(code)

        subnode2 = xml.SubElement(subnode, "casdo:GoodsDescriptionText")
        if str(code) == "8544499108":
            discription = "ПРОВОДА И КАБЕЛИ С ИЗОЛИРОВАННЫМИ ПРОВОДНИКАМИ ДИАМЕТРОМ БОЛЕЕ 0.51ММ, НА НАПРЯЖЕНИЕ БОЛЕЕ 80В," \
                          " НО МЕНЕЕ 1000В (БЕЗ СОЕДИНИТЕЛЬНЫХ ПРИСПОСОБЛЕНИЙ)"
        elif str(code) == "8544609009":
            discription = "ПРОВОДА И КАБЕЛИ С ИЗОЛИРОВАННЫМИ АЛЮМИНИЕВЫМИ ПРОВОДНИКАМИ НА НАПРЯЖЕНИЕ БОЛЕЕ 1000В" \
                          " (БЕЗ СОЕДИНИТЕЛЬНЫХ ПРИСПОСОБЛЕНИЙ)"
        elif str(code) == "8544601000":
            discription = "ПРОВОДА И КАБЕЛИ С ИЗОЛИРОВАННЫМИ МЕДНЫМИ ПРОВОДНИКАМИ НА НАПРЯЖЕНИЕ БОЛЕЕ 1000В" \
                          " (БЕЗ СОЕДИНИТЕЛЬНЫХ ПРИСПОСОБЛЕНИЙ)"
        elif str(code) == "7614100000":
            discription = "СКРУЧЕННАЯ ПРОВОЛОКА ИЗ АЛЮМИНИЯ БЕЗ ЭЛЕКТРИЧЕСКОЙ ИЗОЛЯЦИИ СО СТАЛЬНЫМ СЕРДЕЧНИКОМ"

        elif str(code) == "7614900000":
            discription = "СКРУЧЕННАЯ ПРОВОЛОКА ИЗ АЛЮМИНИЯ БЕЗ ЭЛЕКТРИЧЕСКОЙ ИЗОЛЯЦИИ"

        subnode2.text = discription

        subnode2 = xml.SubElement(subnode, "csdo:UnifiedGrossMassMeasure", measurementUnitCode="166",
                                  measurementUnitCodeListId="2016")
        subnode2.text = str(round(data_item['ВесБрутто'].sum(), 0))

        subnode2 = xml.SubElement(subnode, "csdo:UnifiedNetMassMeasure", measurementUnitCode="166",
                                  measurementUnitCodeListId="2016")
        subnode2.text = str(round(data_item['ВесНетто'].sum(), 0)) ############################

        subnode2 = xml.SubElement(subnode, "casdo:GoodsProhibitionFreeCode")
        subnode2.text = "С"

        subnode2 = xml.SubElement(subnode, "cacdo:GoodsItemGroupDetails")
        subnode3 = xml.SubElement(subnode2, "casdo:GoodsDescriptionText")
        subnode3.text = discription
        subnode3 = xml.SubElement(subnode2, "cacdo:CommodityGroupItemDetails")
        subnode4 = xml.SubElement(subnode3, "cacdo:CommodityDescriptionDetails")
        subnode5 = xml.SubElement(subnode4, "casdo:TradeMarkName")
        subnode5.text = "ЭНЕРГОКОМПЛЕКТ"
        subnode5 = xml.SubElement(subnode4, "csdo:ProductMarkName")
        subnode5.text = str(", ".join(set([row.split()[1] for row in data_item['НаименованиеМЦ'].tolist()])))
        subnode4 = xml.SubElement(subnode3, "cacdo:ManufacturerDetails")
        subnode5 = xml.SubElement(subnode4, "csdo:SubjectBriefName")
        subnode5.text = 'ООО ' + '"ПО"' + 'ЭНЕРГОКОМПЛЕКТ"'
        subnode4 = xml.SubElement(subnode3, "cacdo:GoodsMeasureDetails")
        subnode5 = xml.SubElement(subnode4, "casdo:GoodsMeasure", measurementUnitCode="166",
                                  measurementUnitCodeListId="2016")
        subnode5.text = str(round(data_item['ВесНетто'].sum(), 0))
        subnode5 = xml.SubElement(subnode4, "casdo:MeasureUnitAbbreviationCode")
        subnode5.text = "КГ"

        subnode2 = xml.SubElement(subnode, "cacdo:CargoPackagePalletDetails")
        subnode3 = xml.SubElement(subnode2, "casdo:CargoQuantity")
        subnode3.text = str(round(data_item['КоличествоМест'].sum(), 0))
        subnode3 = xml.SubElement(subnode2, "casdo:CargoKindName")
        subnode3.text = "БАРАБАН"

        subnode2 = xml.SubElement(subnode, "casdo:CleanNetMassMeasure", measurementUnitCode="166",
                                  measurementUnitCodeListId="2016")
        subnode2.text = str(round(data_item['ВесНетто'].sum(), 0))

        subnode2 = xml.SubElement(subnode, "cacdo:OriginCountryDetails")
        subnode3 = xml.SubElement(subnode2, "casdo:CACountryCode", codeListId="2021")
        subnode3.text = "BY"

        subnode2 = xml.SubElement(subnode, "cacdo:PreferenceDetails")
        subnode3 = xml.SubElement(subnode2, "casdo:CustomsClearanceChargesPrefCode", codeListId="2008")
        subnode3.text = "--"
        subnode3 = xml.SubElement(subnode2, "casdo:CustomsDutyPrefCode", codeListId="2008")
        subnode3.text = "--"
        subnode3 = xml.SubElement(subnode2, "casdo:ExcisePrefCode", codeListId="2008")
        subnode3.text = "-"
        subnode3 = xml.SubElement(subnode2, "casdo:VATPrefCode", codeListId="2008")
        subnode3.text = "--"

        subnode2 = xml.SubElement(subnode, "cacdo:CustomsProcedureDetails")
        subnode3 = xml.SubElement(subnode2, "casdo:CustomsProcedureCode", codeListId="2002")
        subnode3.text = "10"

        subnode3 = xml.SubElement(subnode2, "casdo:PreviousCustomsProcedureModeCode", codeListId="2002")
        subnode3.text = self.PreviousCustomsProcedureModeCode #"00"
        subnode3 = xml.SubElement(subnode2, "casdo:GoodsMoveFeatureCode", codeListId="2002")
        subnode3.text = self.GoodsMoveFeatureCode


        subnode2 = xml.SubElement(subnode, "casdo:CAValueAmount", currencyCode=data_item['ВалютаПоИнвойсу'].unique()[0],
                                  currencyCodeListId="2022")
        item_summa = round(data_item['СтоимостьВАЛ'].sum(), 2)
        subnode2.text = str(item_summa)
        currency = CURRENCY_TODAY[data_item['ВалютаПоИнвойсу'].unique()[0]]
        usd = CURRENCY_TODAY['USD'][0]

        subnode2 = xml.SubElement(subnode, "casdo:StatisticValueAmount", currencyCode="USD", currencyCodeListId="2022")
        if currency[1] == 1:
            subnode2.text = str(round((currency[0] * item_summa / usd)
                                      - (data_item['ВесБрутто'].sum() * int(self.transport_cost) / 20000), 2))

        else:
            subnode2.text = str(round((currency[0] / 100 * item_summa / usd)
                                      - (data_item['ВесБрутто'].sum() * int(self.transport_cost) / 20000), 2))

        for cmr in data_item.groupby(['НомерЦМР', 'ДатаЦМР']):
            subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
            subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
            subnode3.text = "02015"
            subnode3 = xml.SubElement(subnode2, "csdo:DocId")
            subnode3.text = str(cmr[0][0])
            subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
            item_date = cmr[0][1].strftime('%Y-%m-%d')
            subnode3.text = str(item_date)
            subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
            subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
            subnode4.text = "0"

        subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
        subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
        subnode3.text = "03011"
        subnode3 = xml.SubElement(subnode2, "csdo:DocId")
        subnode3.text = self.contract_data['НомерДоговора'][self.contract_data.index[0]]
        subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
        if type(self.contract_data['ДатаДоговора'][self.contract_data.index[0]]) is str:
            subnode3.text = self.contract_data['ДатаДоговора'][self.contract_data.index[0]]
        else:
            subnode3.text = "" #str(minimalist_xldate_as_datetime(consignee[8], 0).date())
        subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
        subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
        subnode4.text = "0"

        subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
        subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
        subnode3.text = "03031"
        subnode3 = xml.SubElement(subnode2, "csdo:DocId")
        subnode3.text = str(self.contract_data['Регистрация'][self.contract_data.index[0]])
        subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
        subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
        subnode4.text = "0"

        for inv in data_item.groupby(['НомерИнвойса', 'ДатаИнвойса']):
            subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
            subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
            subnode3.text = "04021"
            subnode3 = xml.SubElement(subnode2, "csdo:DocId")
            subnode3.text = str(inv[0][0])
            subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
            item_date = inv[0][1].strftime('%Y-%m-%d')
            subnode3.text = str(item_date)
            subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
            subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
            subnode4.text = "0"

        if self.PreviousCustomsProcedureModeCode == "78":
            subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
            subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
            subnode3.text = "08034"
            subnode3 = xml.SubElement(subnode2, "csdo:DocId")
            subnode3.text = "10"
            subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
            subnode3.text = "2011-06-09"
            subnode3 = xml.SubElement(subnode2, "csdo:DocStartDate")
            subnode3.text = "2011-06-09"
            subnode3 = xml.SubElement(subnode2, "csdo:DocValidityDate")
            subnode3.text = "2025-12-31"
            subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
            subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
            subnode4.text = "0"

    def save_xml(self, name):
        #mypath = 'd:\\таможня\\'
        mypath = "\\\\First\\таможня\\"
        tree = xml.ElementTree(self.root)
        filename = name + "_DT.xml"
        tree.write(mypath + filename, encoding="utf-8", xml_declaration=True)
        return print('Привет!')


