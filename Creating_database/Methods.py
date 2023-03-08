from bs4 import BeautifulSoup
import requests
import re

######################################## GETTING COLUMN NAMES
"""
method takes list that contains 8 more lists for each category from ADAC webpage
+ parsed.html webpage

and returns list of data by which column names will be defined
"""

def Getting_column_names(column_names,doc):

    ################################################################### ALLGEMEIN
    allgemein_table = doc.find(id="allgemein")
    allgemein_table_class = allgemein_table.parent
    allgemein_content_table =  allgemein_table_class.find("tbody")
    allgemein_content_items = allgemein_content_table.find_all("td")

    for item in range(0,len(allgemein_content_items),2):
        item_string = str(allgemein_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[0]:
            column_names[0].append(parameter)

    ################################################################### MOTOR UND ANTRIEB

    motor_und_antrieb_table = doc.find(id="motor-und-antrieb")
    motor_und_antrieb_table_class = motor_und_antrieb_table.parent
    motor_und_antrieb_content_table =  motor_und_antrieb_table_class.find("tbody")
    motor_und_antrieb_content_items = motor_und_antrieb_content_table.find_all("td")

    for item in range(0,len(motor_und_antrieb_content_items),2):
        item_string = str(motor_und_antrieb_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[1]:
            column_names[1].append(parameter)

    ################################################################### MASSE UND GEWICHTE

    masse_und_gewichte_table = doc.find(id="masse-und-gewichte")
    masse_und_gewichte_table_class = masse_und_gewichte_table.parent
    masse_und_gewichte_content_table = masse_und_gewichte_table_class.find("tbody")
    masse_und_gewichte_content_items = masse_und_gewichte_content_table.find_all("td")

    for item in range(0,len(masse_und_gewichte_content_items),2):
        item_string = str(masse_und_gewichte_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[2]:
            column_names[2].append(parameter)

    ################################################################### KAROSSERIE UND FAHRWERK

    karosserie_und_fahrwerk_table = doc.find(id="karosserie-und-fahrwerk")
    karosserie_und_fahrwerk_table_class = karosserie_und_fahrwerk_table.parent
    karosserie_und_fahrwerk_content_table = karosserie_und_fahrwerk_table_class.find("tbody")
    karosserie_und_fahrwerk_content_items = karosserie_und_fahrwerk_content_table.find_all("td")

    for item in range(0,len(karosserie_und_fahrwerk_content_items),2):
        item_string = str(karosserie_und_fahrwerk_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[3]:
            column_names[3].append(parameter)

    ################################################################### MESSWERTE HERSTELLER

    messwerte_hersteller_table = doc.find(id="messwerte-hersteller")
    messwerte_hersteller_table_class = messwerte_hersteller_table.parent
    messwerte_hersteller_content_table = messwerte_hersteller_table_class.find("tbody")
    messwerte_hersteller_content_items = messwerte_hersteller_content_table.find_all("td")

    for item in range(0,len(messwerte_hersteller_content_items),2):
        item_string = str(messwerte_hersteller_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[4]:
            column_names[4].append(parameter)

    ################################################################### SICHERHEITSAUSSTATTUNG

    sicherheitsausstattung_table = doc.find(id="sicherheitsausstattung")
    sicherheitsausstattung_table_class = sicherheitsausstattung_table.parent
    sicherheitsausstattung_content_table = sicherheitsausstattung_table_class.find("tbody")
    sicherheitsausstattung_content_items = sicherheitsausstattung_content_table.find_all("td")

    for item in range(0,len(sicherheitsausstattung_content_items),2):
        item_string = str(sicherheitsausstattung_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[5]:
            column_names[5].append(parameter)

    ################################################################### HERSTELLERGARANTIEN

    herstellergarantien_table = doc.find(id="herstellergarantien")
    herstellergarantien_table_class = herstellergarantien_table.parent
    herstellergarantien_content_table = herstellergarantien_table_class.find("tbody")
    herstellergarantien_content_items = herstellergarantien_content_table.find_all("td")

    for item in range(0,len(herstellergarantien_content_items),2):
        item_string = str(herstellergarantien_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[6]:
            column_names[6].append(parameter)

    ################################################################### PREISE UND AUSSTATTUNG

    preise_und_ausstattung_table = doc.find(id="preise-und-ausstattung")
    preise_und_ausstattung_table_class = preise_und_ausstattung_table.parent
    preise_und_ausstattung_content_table = preise_und_ausstattung_table_class.find("tbody")
    preise_und_ausstattung_content_items = preise_und_ausstattung_content_table.find_all("td")

    for item in range(0,len(preise_und_ausstattung_content_items),2):
        item_string = str(preise_und_ausstattung_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        parameter=parameter.replace(",","zarez")
        if parameter not in column_names[7]:
            column_names[7].append(parameter)

    return column_names

"""
method iterates through all pages and checks for all possible column names
"""
def Iterating_through_pages_to_get_column_names(column_names,doc):
    ############################################################################ GET NUMBER OF PAGES
    page_text = doc.find(["div"], attrs={"data-testid": "pagination"})
    all_a = page_text.find_all("a")
    target_a = all_a[-2]
    a_string = (str(target_a).split("</a>")[-2]).split(">")[-1]
    number_of_pages = int(a_string)

    ############################################################################ ITERATION AND URL LOADING

    for page in range(1, number_of_pages + 1):
        print(page)
        url = f"https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/autosuche/?engineTypes=Elektro&pageNumber={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")

        table_of_all_items_on_page = doc.find(["div"], class_="sc-chSlKD dUYZym")
        urls_list = table_of_all_items_on_page.find_all(["a"])
        for u in urls_list:
            temp_url = (str(u).split("href=")[-1]).split(">")[0]
            temp_url = temp_url.replace('"', "")
            temp_page = "https://www.adac.de" + temp_url + "#technische-daten"
            temp_doc = BeautifulSoup(requests.get(temp_page).text, "html.parser")
            column_names = Getting_column_names(column_names, temp_doc)

    return column_names

######################################## GETTING DATA
"""
method takes dictionary and webpage in html.parse format and fills the dictionary lists with data
and returns that dictionary
"""

def Getting_data_from_one_page(data,doc):

    ################################################################### ALLGEMEIN
    allgemein_table = doc.find(id="allgemein")
    allgemein_table_class = allgemein_table.parent
    allgemein_content_table =  allgemein_table_class.find("tbody")
    allgemein_content_items = allgemein_content_table.find_all("td")

    for item in range(0,len(allgemein_content_items)-1,2):
        item_string = str(allgemein_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(allgemein_content_items[item+1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]
        if parameter in data:
            data[parameter].append(value)

    ################################################################### MOTOR UND ANTRIEB

    motor_und_antrieb_table = doc.find(id="motor-und-antrieb")
    motor_und_antrieb_table_class = motor_und_antrieb_table.parent
    motor_und_antrieb_content_table =  motor_und_antrieb_table_class.find("tbody")
    motor_und_antrieb_content_items = motor_und_antrieb_content_table.find_all("td")

    for item in range(0,len(motor_und_antrieb_content_items)-1,2):
        item_string = str(motor_und_antrieb_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(motor_und_antrieb_content_items[item + 1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]

        if parameter in data:
            data[parameter].append(value)

    ################################################################### MASSE UND GEWICHTE

    masse_und_gewichte_table = doc.find(id="masse-und-gewichte")
    masse_und_gewichte_table_class = masse_und_gewichte_table.parent
    masse_und_gewichte_content_table = masse_und_gewichte_table_class.find("tbody")
    masse_und_gewichte_content_items = masse_und_gewichte_content_table.find_all("td")

    for item in range(0,len(masse_und_gewichte_content_items)-1,2):
        item_string = str(masse_und_gewichte_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(masse_und_gewichte_content_items[item + 1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]

        if parameter in data:
            data[parameter].append(value)

    ################################################################### KAROSSERIE UND FAHRWERK

    karosserie_und_fahrwerk_table = doc.find(id="karosserie-und-fahrwerk")
    karosserie_und_fahrwerk_table_class = karosserie_und_fahrwerk_table.parent
    karosserie_und_fahrwerk_content_table = karosserie_und_fahrwerk_table_class.find("tbody")
    karosserie_und_fahrwerk_content_items = karosserie_und_fahrwerk_content_table.find_all("td")

    for item in range(0,len(karosserie_und_fahrwerk_content_items)-1,2):
        item_string = str(karosserie_und_fahrwerk_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(karosserie_und_fahrwerk_content_items[item + 1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]

        if parameter in data:
            data[parameter].append(value)

    ################################################################### MESSWERTE HERSTELLER

    messwerte_hersteller_table = doc.find(id="messwerte-hersteller")
    messwerte_hersteller_table_class = messwerte_hersteller_table.parent
    messwerte_hersteller_content_table = messwerte_hersteller_table_class.find("tbody")
    messwerte_hersteller_content_items = messwerte_hersteller_content_table.find_all("td")

    for item in range(0,len(messwerte_hersteller_content_items)-1,2):
        item_string = str(messwerte_hersteller_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(messwerte_hersteller_content_items[item + 1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]

        if parameter in data:
            data[parameter].append(value)

    ################################################################### SICHERHEITSAUSSTATTUNG

    sicherheitsausstattung_table = doc.find(id="sicherheitsausstattung")
    sicherheitsausstattung_table_class = sicherheitsausstattung_table.parent
    sicherheitsausstattung_content_table = sicherheitsausstattung_table_class.find("tbody")
    sicherheitsausstattung_content_items = sicherheitsausstattung_content_table.find_all("td")

    for item in range(0,len(sicherheitsausstattung_content_items)-1,2):
        item_string = str(sicherheitsausstattung_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(sicherheitsausstattung_content_items[item + 1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]

        if parameter in data:
            data[parameter].append(value)

    ################################################################### HERSTELLERGARANTIEN

    herstellergarantien_table = doc.find(id="herstellergarantien")
    herstellergarantien_table_class = herstellergarantien_table.parent
    herstellergarantien_content_table = herstellergarantien_table_class.find("tbody")
    herstellergarantien_content_items = herstellergarantien_content_table.find_all("td")

    for item in range(0,len(herstellergarantien_content_items)-1,2):
        item_string = str(herstellergarantien_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(herstellergarantien_content_items[item + 1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]

        if parameter in data:
            data[parameter].append(value)

    ################################################################### PREISE UND AUSSTATTUNG

    preise_und_ausstattung_table = doc.find(id="preise-und-ausstattung")
    preise_und_ausstattung_table_class = preise_und_ausstattung_table.parent
    preise_und_ausstattung_content_table = preise_und_ausstattung_table_class.find("tbody")
    preise_und_ausstattung_content_items = preise_und_ausstattung_content_table.find_all("td")

    for item in range(0,len(preise_und_ausstattung_content_items)-1,2):
        item_string = str(preise_und_ausstattung_content_items[item])
        parameter = (item_string.split("/td")[-2]).split(">")[-1][:-1]
        value_string = str(preise_und_ausstattung_content_items[item + 1])
        value = (value_string.split("/td")[-2]).split(">")[-1][:-1]

        if parameter in data and parameter != "Grundpreis":
            data[parameter].append(value)

    return data

"""
method iterates through all pages and fills database
"""
def Iterating_through_pages_to_get_data(data,doc):
    ############################################################################ GET NUMBER OF PAGES
    page_text = doc.find(["div"], attrs={"data-testid": "pagination"})
    all_a = page_text.find_all("a")
    target_a = all_a[-2]
    a_string = (str(target_a).split("</a>")[-2]).split(">")[-1]
    number_of_pages = int(a_string)


    ############################################################################ ITERATION AND URL LOADING

    for page in range(1, number_of_pages+1):
        print(page)
        url = f"https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/autosuche/?engineTypes=Elektro&pageNumber={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        table_of_all_items_on_page = doc.find(["div"], class_="sc-dusCKN iybrLp") #check class name if thecode is not working
        urls_list = table_of_all_items_on_page.find_all(["a"])
        for u in urls_list:
            temp_url = (str(u).split("href=")[-1]).split(">")[0]
            temp_url = temp_url.replace('"', "")
            temp_page = "https://www.adac.de" + temp_url + "#technische-daten"
            temp_doc = BeautifulSoup(requests.get(temp_page).text, "html.parser")
            data = Getting_data_from_one_page(data, temp_doc)
            ###### created for filling empty places
            lenght = len(data["Marke"])
            for key,list in data.items():
                if len(list) < lenght:
                    list.append("")

    return data

