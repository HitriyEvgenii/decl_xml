import xlrd
import xml  .etree.ElementTree as xml
from datetime import datetime, timedelta
import PySimpleGUI as sg
import requests
import transport_cost_with_lite as tc
import pandas
import group_by_invoices
import group_by_invoices_pys

abc = []

def minimalist_xldate_as_datetime(xldate, datemode):
    # datemode: 0 for 1900-based, 1 for 1904-based
    return (
        datetime(1899, 12, 30)
        + timedelta(days=xldate + 1462 * datemode)
        )

def GoodsItemDetails(subnode, i):


    subnode2 = xml.SubElement(subnode, "casdo:ConsignmentItemOrdinal")
    subnode2.text = str(decl[i][0])

    subnode2 = xml.SubElement(subnode, "csdo:CommodityCode")
    subnode2.text = str(int(decl[i][1]))

    subnode2 = xml.SubElement(subnode, "casdo:GoodsDescriptionText")
    if str(int(decl[i][1])) == "8544499108":
        discription = "ПРОВОДА И КАБЕЛИ С ИЗОЛИРОВАННЫМИ ПРОВОДНИКАМИ ДИАМЕТРОМ БОЛЕЕ 0.51ММ, НА НАПРЯЖЕНИЕ БОЛЕЕ 80В," \
                        " НО МЕНЕЕ 1000В (БЕЗ СОЕДИНИТЕЛЬНЫХ ПРИСПОСОБЛЕНИЙ)"
    elif str(int(decl[i][1])) == "8544609009":
        discription = "ПРОВОДА И КАБЕЛИ С ИЗОЛИРОВАННЫМИ АЛЮМИНИЕВЫМИ ПРОВОДНИКАМИ НА НАПРЯЖЕНИЕ БОЛЕЕ 1000В" \
                        " (БЕЗ СОЕДИНИТЕЛЬНЫХ ПРИСПОСОБЛЕНИЙ)"
    elif str(int(decl[i][1])) == "8544601000":
        discription = "ПРОВОДА И КАБЕЛИ С ИЗОЛИРОВАННЫМИ МЕДНЫМИ ПРОВОДНИКАМИ НА НАПРЯЖЕНИЕ БОЛЕЕ 1000В" \
                        " (БЕЗ СОЕДИНИТЕЛЬНЫХ ПРИСПОСОБЛЕНИЙ)"
    elif str(int(decl[i][1])) == "7614100000":
        discription = "СКРУЧЕННАЯ ПРОВОЛОКА ИЗ АЛЮМИНИЯ БЕЗ ЭЛЕКТРИЧЕСКОЙ ИЗОЛЯЦИИ СО СТАЛЬНЫМ СЕРДЕЧНИКОМ"

    elif str(int(decl[i][1])) == "7614900000":
        discription = "СКРУЧЕННАЯ ПРОВОЛОКА ИЗ АЛЮМИНИЯ БЕЗ ЭЛЕКТРИЧЕСКОЙ ИЗОЛЯЦИИ"

    subnode2.text = discription

    subnode2 = xml.SubElement(subnode, "csdo:UnifiedGrossMassMeasure", measurementUnitCode="166",
                              measurementUnitCodeListId="2016")
    subnode2.text = str(int(decl[i][4]))

    subnode2 = xml.SubElement(subnode, "csdo:UnifiedNetMassMeasure", measurementUnitCode="166",
                              measurementUnitCodeListId="2016")
    subnode2.text = str(int(decl[i][3]))

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
    subnode5.text = str(", ".join(decl[i][7]))
    subnode4 = xml.SubElement(subnode3, "cacdo:ManufacturerDetails")
    subnode5 = xml.SubElement(subnode4, "csdo:SubjectBriefName")
    subnode5.text = 'ООО ' + '"ПО"' + 'ЭНЕРГОКОМПЛЕКТ"'
    subnode4 = xml.SubElement(subnode3, "cacdo:GoodsMeasureDetails")
    subnode5 = xml.SubElement(subnode4, "casdo:GoodsMeasure", measurementUnitCode="166",
                              measurementUnitCodeListId="2016")
    subnode5.text = str(decl[i][3])
    subnode5 = xml.SubElement(subnode4, "casdo:MeasureUnitAbbreviationCode")
    subnode5.text = "КГ"

    subnode2 = xml.SubElement(subnode, "cacdo:CargoPackagePalletDetails")
    subnode3 = xml.SubElement(subnode2, "casdo:CargoQuantity")
    subnode3.text = str(int(decl[i][5]))
    subnode3 = xml.SubElement(subnode2, "casdo:CargoKindName")
    subnode3.text = "БАРАБАН"

    subnode2 = xml.SubElement(subnode, "casdo:CleanNetMassMeasure", measurementUnitCode="166",
                              measurementUnitCodeListId="2016")
    subnode2.text = str(decl[i][3])

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

    if decl[i][8] == "":
        subnode3 = xml.SubElement(subnode2, "casdo:PreviousCustomsProcedureModeCode", codeListId="2002")
        subnode3.text = "00"
        subnode3 = xml.SubElement(subnode2, "casdo:GoodsMoveFeatureCode", codeListId="2002")
        subnode3.text = "000"
    else:
        subnode3 = xml.SubElement(subnode2, "casdo:PreviousCustomsProcedureModeCode", codeListId="2002")
        subnode3.text = "78"
        subnode3 = xml.SubElement(subnode2, "casdo:GoodsMoveFeatureCode", codeListId="2002")
        subnode3.text = "102"

    subnode2 = xml.SubElement(subnode, "casdo:CAValueAmount", currencyCode=consignee[6], currencyCodeListId="2022")
    subnode2.text = str(decl[i][2])

    subnode2 = xml.SubElement(subnode, "casdo:StatisticValueAmount", currencyCode="USD", currencyCodeListId="2022")
    if currency(consignee[6])[1] == 1:
        subnode2.text = str(round((CUR[0] * decl[i][2] / usd) - (decl[i][4] * int(abc[0][5])/20000), 2))

    else:
        #print(((CUR[0] / 100 * decl[i][2] / usd) - (decl[i][4] * int(abc[0][5]) / 20000)))
        subnode2.text = str(round(((CUR[0] / 100 * decl[i][2] / usd) - (decl[i][4] * int(abc[0][5]) / 20000)), 2))
    #print("stat= ", subnode2.text, abc)

    subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
    subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
    subnode3.text = "02015"
    subnode3 = xml.SubElement(subnode2, "csdo:DocId")
    subnode3.text = decl[i][11]
    subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
    subnode3.text = decl[i][12]
    subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
    subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
    subnode4.text = "0"

    subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
    subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
    subnode3.text = "03011"
    subnode3 = xml.SubElement(subnode2, "csdo:DocId")
    subnode3.text = consignee[7]
    subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
    if type(consignee[8]) is str:
        subnode3.text = consignee[8]
    else:
        subnode3.text = str(minimalist_xldate_as_datetime(consignee[8], 0).date())
    subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
    subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
    subnode4.text = "0"

    subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
    subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
    subnode3.text = "03031"
    subnode3 = xml.SubElement(subnode2, "csdo:DocId")
    subnode3.text = consignee[9]
    subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
    subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
    subnode4.text = "0"

    subnode2 = xml.SubElement(subnode, "cacdo:PresentedDocDetails")
    subnode3 = xml.SubElement(subnode2, "csdo:DocKindCode", codeListId="2009")
    subnode3.text = "04021"
    subnode3 = xml.SubElement(subnode2, "csdo:DocId")
    subnode3.text = decl[i][9]
    subnode3 = xml.SubElement(subnode2, "csdo:DocCreationDate")
    subnode3.text = decl[i][10]
    subnode3 = xml.SubElement(subnode2, "cacdo:DocumentPresentingDetails")
    subnode4 = xml.SubElement(subnode3, "casdo:DocPresentKindCode")
    subnode4.text = "0"

    if str(decl[0][8]) == 'СТЗ':
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

def dDetails():

    declarantDetails = xml.Element("cacdo:DeclarantDetails")

    SubjectBriefName = xml.Element("csdo:SubjectBriefName")
    declarantDetails.append(SubjectBriefName)
    SubjectBriefName.text = 'ООО ' + '"ПО"' + 'ЭНЕРГОКОМПЛЕКТ"'

    TaxpayerId = xml.Element("csdo:TaxpayerId")
    declarantDetails.append(TaxpayerId)
    TaxpayerId.text = '300528652'

def DeclGoodsShipmentDetails(node1):

    subnode = xml.SubElement(node1, "cacdo:DepartureCountryDetails")
    subnode2 = xml.SubElement(subnode, "casdo:CACountryCode", codeListId="2021")
    subnode2.text = "BY"
    subnode2 = xml.SubElement(subnode, "casdo:ShortCountryName")
    subnode2.text = "БЕЛАРУСЬ"
    subnode2 = xml.SubElement(subnode, "csdo:TerritoryCode")
    subnode2.text = "000"

    subnode = xml.SubElement(node1, "cacdo:DestinationCountryDetails")
    subnode2 = xml.SubElement(subnode, "casdo:CACountryCode", codeListId="2021")
    subnode2.text = str(abc[0][6])
    subnode2 = xml.SubElement(subnode, "casdo:ShortCountryName")
    subnode2.text = str(abc[0][8])
    subnode2 = xml.SubElement(subnode, "csdo:TerritoryCode")
    subnode2.text = str(abc[0][7])

    subnode = xml.SubElement(node1, "cacdo:TradeCountryDetails")
    subnode2 = xml.SubElement(subnode, "casdo:CACountryCode", codeListId="2021")
    subnode2.text = consignee[1]
    subnode2 = xml.SubElement(subnode, "csdo:TerritoryCode")
    subnode2.text = consignee[12]

    subnode = xml.SubElement(node1, "cacdo:DeliveryTermsDetails")
    subnode2 = xml.SubElement(subnode, "casdo:DeliveryTermsCode", codeListId="2014")
    subnode2.text = abc[0][2]
    subnode2 = xml.SubElement(subnode, "casdo:PlaceName")
    subnode2.text = abc[0][3]
    subnode2 = xml.SubElement(subnode, "casdo:DeliveryKindCode")
    subnode2.text = "02"

    subnode = xml.SubElement(node1, "casdo:CAValueAmount", currencyCode=consignee[6], currencyCodeListId="2022")
    subnode.text = str(round(CAValueAmount, 2))


    if CUR[1] == 1:
        subnode = xml.SubElement(node1, "casdo:ExchangeRate", currencyCode=consignee[6], currencyCodeListId="2022",
                                 scaleNumber="0")
        subnode.text = str(CUR[0])

    else:
        subnode = xml.SubElement(node1, "casdo:ExchangeRate", currencyCode=consignee[6], currencyCodeListId="2022",
                                 scaleNumber="2")
        subnode.text = str(CUR[0])

    subnode = xml.SubElement(node1, "cacdo:ConsignorDetails")
    subnode2 = xml.SubElement(subnode, "casdo:EqualIndicator")
    subnode2.text = "1"

    subnode = xml.SubElement(node1, "cacdo:ConsigneeDetails")
    subnode2 = xml.SubElement(subnode, "csdo:SubjectBriefName")
    subnode2.text = consignee[0]
    subnode2 = xml.SubElement(subnode, "ccdo:SubjectAddressDetails")
    subnode3 = xml.SubElement(subnode2, "csdo:UnifiedCountryCode", codeListId="2021")
    subnode3.text = consignee[1]
    subnode3 = xml.SubElement(subnode2, "csdo:CityName")
    subnode3.text = consignee[3]
    subnode3 = xml.SubElement(subnode2, "csdo:StreetName")
    subnode3.text = consignee[4]
    subnode3 = xml.SubElement(subnode2, "csdo:BuildingNumberId")
    subnode3.text = str(consignee[5])
    subnode3 = xml.SubElement(subnode2, "csdo:PostCode")
    subnode3.text = str(consignee[2])

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
    subnode3.text = ct[0]
    subnode3 = xml.SubElement(subnode2, "casdo:TransportMeansQuantity")
    subnode3.text = "2"
    subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
    subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=ct[0], countryCodeListId="2021")
    subnode4.text = truck  # номер тягача
    subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
    subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=ct[1][:-1], countryCodeListId="2021")
    subnode4.text = trailer  # номер полуприцепа
    subnode2 = xml.SubElement(subnode, "cacdo:ArrivalDepartureTransportDetails")
    subnode3 = xml.SubElement(subnode2, "csdo:UnifiedTransportModeCode", codeListId="2004")
    #subnode3.text = "31"
    subnode3 = xml.SubElement(subnode2, "casdo:RegistrationNationalityCode", codeListId="2021")
    subnode3.text = ct[0]
    subnode3 = xml.SubElement(subnode2, "casdo:TransportMeansQuantity")
    subnode3.text = "2"
    subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
    subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=ct[0], countryCodeListId="2021")
    subnode4.text = truck  # номер тягача
    subnode3 = xml.SubElement(subnode2, "cacdo:TransportMeansRegistrationIdDetails")
    subnode4 = xml.SubElement(subnode3, "csdo:TransportMeansRegId", countryCode=ct[1][:-1], countryCodeListId="2021")
    subnode4.text = trailer  # номер полуприцепа

    subnode = xml.SubElement(node1, "cacdo:GoodsLocationDetails")
    subnode2 = xml.SubElement(subnode, "casdo:GoodsLocationCode", codeListId="2023")
    if decl[0][8] == 'СТЗ':
        subnode2.text = "80"
    else:
        subnode2.text = "60"
    subnode2 = xml.SubElement(subnode, "csdo:CustomsOfficeCode")
    subnode2.text = "07000"
    subnode2 = xml.SubElement(subnode, "casdo:CustomsControlZoneId")
    subnode2.text = "ПЗ07260/0001129"

    for i in range(len(decl)):
        subnode = xml.SubElement(node1, "cacdo:DeclarationGoodsItemDetails")
        GoodsItemDetails(subnode, i)

def dDetails(declarantDetails):


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

def createXML():



    root = xml.Element("gd:GoodsDeclaration")
    root.set("xmlns:csdo", "urn:EEC:M:SimpleDataObjects:v0.4.10")
    root.set("xmlns:casdo", "urn:EEC:M:CA:SimpleDataObjects:v1.5.1")
    root.set("xmlns:ccdo", "urn:EEC:M:ComplexDataObjects:v0.4.10")
    root.set("xmlns:cacdo", "urn:EEC:M:CA:ComplexDataObjects:v1.5.1")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xmlns:gd", "urn:EEC:R:036:GoodsDeclaration:v1.1.0")
    root.set("xsi:schemaLocation", "urn:EEC:R:036:GoodsDeclaration:v1.1.0")


    EDocCode = xml.Element("csdo:EDocCode")
    root.append(EDocCode)
    EDocCode.text = "R.036"

    EDocId = xml.Element("csdo:EDocId")
    root.append(EDocId)
    EDocId.text = "709D924C-C0A8-010F-015D-8D622449EE71"

    EDocDateTime = xml.Element("csdo:EDocDateTime")
    root.append(EDocDateTime)
    EDocDateTime.text = str(datetime.now().date()) + "T00:00:00"

    DeclarationKindCode = xml.Element("casdo:DeclarationKindCode")
    root.append(DeclarationKindCode)
    DeclarationKindCode.text = "ЭК"

    CustomsProcedureCode = xml.Element("casdo:CustomsProcedureCode", codeListId="2002")
    root.append(CustomsProcedureCode)
    CustomsProcedureCode.text = "10"

    EDocIndicatorCode = xml.Element("casdo:EDocIndicatorCode")
    root.append(EDocIndicatorCode)
    EDocIndicatorCode.text = "ЭД"




    PageQuantity = xml.Element("csdo:PageQuantity")
    root.append(PageQuantity)
    PageQuantity.text = str(PageQ)

    GoodsQuant = xml.Element("casdo:GoodsQuantity")
    root.append(GoodsQuant)
    GoodsQuant.text = str(GoodsQ)

    CargoQuantity = xml.Element("casdo:CargoQuantity")
    root.append(CargoQuantity)
    #CargoQuantity.text = str(GoodsQ)


    if decl[0][5] != '':
        CargoQuantity.text = str(int(sum([i[5] for i in decl])))
    else:
        CargoQuantity.text = ''

    declarantDetails = xml.Element("cacdo:DeclarantDetails")
    root.append(declarantDetails)
    dDetails(declarantDetails)


    node1 = xml.Element("cacdo:DeclarationGoodsShipmentDetails")
    root.append(node1)

    DeclGoodsShipmentDetails(node1)

    workers = [['ЕВГЕНИЙ', 'ВЛАДИМИРОВИЧ', 'МОСКАЛЬКОВ', 'СПЕЦИАЛИСТ', 'ВМ1469628', '2006-07-19', '2026-04-15'
                   , '296', '2006-08-02'],
               ['ВЛАДИМИР', 'АНАТОЛЬЕВИЧ', 'ВОЛЧЁК', 'ВЕДУЩИЙ СПЕЦИАЛИСТ', 'ВМ2059805', '2012-12-21', '2022-12-21'
                   , '144', '2018-09-27' ]
               ]
    if win_values[1] == True:
        ind = workers[0]
    else:
        ind = workers[1]

    node1 = xml.Element("cacdo:SignatoryPersonV2Details")
    root.append(node1)
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
    root.append(node1)
    if str(decl[0][8]) == 'СТЗ':
        node1.text = decl[0][9] + "СТЗ"
    else:
        node1.text = decl[0][9] + "K"

    mypath = 'd:\\таможня\\'
    #mypath = "\\\\First\\таможня\\"
    if decl[0][8] == 'СТЗ':
        tree = xml.ElementTree(root)
        filename = str(decl[0][9]) + "СТЗ" + "_DT.xml"
        tree.write(mypath + filename, encoding="utf-8", xml_declaration=True)
    else:
        tree = xml.ElementTree(root)
        filename = str(decl[0][9]) + "K" + "_DT.xml"
        tree.write(mypath + filename, encoding="utf-8", xml_declaration=True)

def country_truck(arg1, arg2):
    import PySimpleGUI as sg

    layout = [[sg.Text('Тягач ', size=(6, 1)), sg.Text(arg1, size=(10, 1)), sg.Radio('BY', 'tr', key='BY', default=True),
                        sg.Radio('RU', 'tr',key='RU'), sg.Radio('PL', 'tr', key='PL'), sg.Radio('LT', 'tr', key='LT'),
               sg.Radio('LV', 'tr', key='LV')],
                       [sg.Text('Прицеп', size=(6, 1)), sg.Text(arg2, size=(10, 1)), sg.Radio('BY', 'tra', key='BY1', default=True),
                        sg.Radio('RU', 'tra', key='RU1'), sg.Radio('PL', 'tra', key='PL1'), sg.Radio('LT', 'tra', key='LT1')
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
                    tr1.append(i)
            window.close()
            return tr1

def currency(arg):
    response_cur = requests.get(f'https://www.nbrb.by/api/exrates/rates/{arg}?parammode=2').json()
    return response_cur['Cur_OfficialRate'], response_cur['Cur_Scale']

usd = currency('USD')[0]




layout = [
    #[sg.Text('File 1'), sg.InputText(default_text=r"C:\Prg\otch\зпрТранспортЗаявки_ПечатьИнфо.xls"), sg.FileBrowse()],
    [sg.Text('File 1'), sg.InputText(default_text=r"C:\Users\Clo3\PycharmProjects\create_xml\зпрТранспортЗаявки_ПечатьИнфо.xls"), sg.FileBrowse()],
    #[sg.Checkbox('Москальков', size=(15,1), key='mosk', default=True), sg.Checkbox('Волчек', key='volch')],
    #[sg.Checkbox('Волчек', size=(15,1), key='volch', default=False, enable_events=True)],
    [sg.Radio('Москальков', 'RADIO1', default=True, size=(10,1)), sg.Radio('Волчек', "RADIO1")],
    #[sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1))],
    #[sg.Radio('My second Radio!', "RADIO1")],
    #[sg.Output(size=(88, 20))],
    [sg.Submit("Экспорт xml"), sg.Cancel()]]

window = sg.Window('File Compare', layout)

while True:

    # The Event Loop
    event, win_values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break

    if event == 'Экспорт xml':
        #print(win_values[0])
        url1 = win_values[0]

        rb = xlrd.open_workbook(url1, encoding_override="cp1251")
        #rb2 = xlrd.open_workbook(r"\\First\таможня\бараб\данные по ДТ.xls", encoding_override="cp1251")
        rb2 = xlrd.open_workbook(r"C:\Users\Clo3\PycharmProjects\create_xml\данные по ДТ.xls", encoding_override="cp1251")
        sheet = rb.sheet_by_index(0)
        sheet2 = rb2.sheet_by_index(0)
        rb_pandas = pandas.read_excel(url1, sheet_name='зпрТранспортЗаявки_ПечатьИнфо')
        #print(rb_pandas)
        data_pand = rb_pandas.groupby(['НомерИнвойса', 'СТЗ', 'НомерДоговора'], dropna=False)[['СтоимостьВАЛ', 'ВесНетто', 'ВесБрутто', 'КоличествоМест']].sum()

        #print(list(data_pand.index.values))
        group_by_invoices_pys.group_invoices(data_pand)
        #group_by_invoices.group_invoices(data_pand)
        print(list(data_pand.sum()[['СтоимостьВАЛ', 'ВесНетто', 'ВесБрутто', 'КоличествоМест']]))
        vals = [sheet.row_values(rownum) for rownum in range(1, sheet.nrows)]
        vals2 = [sheet2.row_values(rownum) for rownum in range(1, sheet2.nrows)]

        truck = sheet.cell_value(1, -2).replace(" ", "")
        trailer = sheet.cell_value(1, -1).replace(" ", "")
        print('USD -', currency('USD')[0])
        print()
        print(truck, trailer)
        print()
        ct = country_truck(truck, trailer)


        a = 0

        number_rows = sheet.col_values(1, 1)
        invoices = set(sheet.col_values(1, 1))



        for invoice in invoices:
            invoice_goods = []
            for i in range(1, len(number_rows) + 1):
                if invoice == sheet.cell_value(i, 1):
                    invoice_goods.append(sheet.row_values(i))

            codes_tnved = []
            for i in range(len(invoice_goods)):
                if invoice_goods[i][5] not in codes_tnved:
                    codes_tnved.append(invoice_goods[i][5])

            kol_goods = len(codes_tnved)

            decl = []
            good = 1
            for i in codes_tnved:
                summa = 0
                netto = 0
                brutto = 0
                goodsquantity = 0
                goods = set()
                for j in invoice_goods:
                    if i == j[5]:
                        summa += j[11]
                        netto += j[13]
                        brutto += j[14]
                        if j[16] == '':
                            goodsquantity = 0
                        else:
                            goodsquantity += j[16]
                        word = j[7].split(" ")

                        dog = j[6].split(" ")[0]
                        goods.add(word[1].upper())
                decl.append([good, i, round(summa, 2), netto, brutto, goodsquantity, dog, goods,
                             invoice_goods[0][0], invoice_goods[0][1], str(minimalist_xldate_as_datetime((invoice_goods[0][2]), 0).date()),
                            invoice_goods[0][3], str(minimalist_xldate_as_datetime((invoice_goods[0][4]), 0).date())])

                good += 1

            consignee = []
            if len(decl) != 0:

                for i in vals2:
                    if decl[0][6] == i[7]:
                        consignee = i
                        break


                CAValueAmount = 0
                GoodsQ = len(decl)

                b = 1 + (int((GoodsQ - 1) / 3) + 1)
                if GoodsQ == 1:
                    PageQ = 1
                else:
                    PageQ = b

                for i in decl:
                    CAValueAmount += i[2]

                try:
                    abc = tc.transport_cost(consignee[7], decl[0][9])
                    if abc == None:
                        break

                except:
                    sg.popup("В базе отсутствует договор " + decl[0][6])
                    break
            CUR = currency(consignee[6])
            print('Курс ', consignee[6], " - ", CUR[0] )
            print(decl)
            #createXML()
            try:
                createXML()
            except:
                print("Что-то пошло не так!")




