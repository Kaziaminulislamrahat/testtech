import csv
from os import remove
import requests
from bs4 import BeautifulSoup as bs
url="https://www.gadgetsnow.com/laptops/Lenovo-IdeaPad-5-82LN00A3IN-Laptop-AMD-Ryzen-7-5700U-AMD-Radeon-16GB-512GB-SSD-Windows-10"
response=requests.get(url)
#print(response.text)
html=bs(response.text, "html.parser")
#print(html)
list_table_head={}
table_head=html.find_all('th')
list_table_head[0]=(table_head)
#list_table_head.append(table_head)
list_table_body={}
table_body=html.find_all('td')
list_table_body[0]=(table_body)



#list_table_body.append(table_body)



#print(list_table_body,list_table_head)


data=[list_table_head[0],list_table_body[0]]

header = ('Parameter', 'Magnitude')

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    writer.writerow(data)
