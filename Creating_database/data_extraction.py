import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import Methods
import csv
import openpyxl
from openpyxl.workbook import Workbook

start_url = "https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/autosuche/?engineTypes=Elektro&pageNumber=1"
page = requests.get(start_url).text
doc = BeautifulSoup(page,"html.parser")

#################### GETTING COLUMN NAMES *only required for the first time if the csv is not created

"""column_names = [[],[],[],[],[],[],[],[]]
column_names = Methods.Iterating_through_pages_to_get_column_names(column_names,doc)

with open("column_names.csv","w") as f:
    write = csv.writer(f)
    for name in column_names:
        write.writerow(name)
"""
#################### BUILDING A DATABASE
#reading column names from csv file to array
temp_column_names = []
column_names = ""
with open("column_names.csv","r") as f:
    for line in f:
        temp_column_names.append(line)
temp_column_names.remove("\n")
for name in temp_column_names:
    name = str(name).replace("\n","")
    column_names = column_names + name + ","
while column_names[-1] == ",":
    column_names = column_names[:-1]

#creating a database

list_of_column_names = column_names.split(",")

for i in range(len(list_of_column_names)):
    list_of_column_names[i] = list_of_column_names[i].replace("zarez",",")

list_of_column_names.remove("")

data = {}
for name in list_of_column_names:
    data[name] = []

data = Methods.Iterating_through_pages_to_get_data(data,doc)


df = pd.DataFrame.from_dict(data)
df.to_excel("ADAC_Database.xlsx")






