import requests
from bs4 import BeautifulSoup
import csv
from datetime import date


def get_price(URL, name):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return [name, soup.find(id="product-price").text.strip()]

def get_data():
    data_of_new_mobile = get_price("https://www.newmobile.hu/hu/webshop/apple/apple-iphone-12-mini-64gb-mobiltelefon?id=40977", "New Mobile bolt")
    data_of_ujgsm = get_price("https://www.ujgsm.hu/hu/webshop/apple/apple-iphone-12-mini-64gb-mobiltelefon?id=40977","UJ GSM bolt")

    return [data_of_new_mobile, data_of_ujgsm]

def open_csv_file(filename):
    today = date.today().strftime("%d/%m/%Y")
    data_of_prices= get_data()
    for data in data_of_prices:
        name_of_shop = data[0]
        price = data[1]
        with open(filename, 'r') as file:
            last_line = file.readlines()[-1]
            last_ID=int(last_line.split(',')[0])
            print(last_ID)

        fields = [last_ID+1, name_of_shop, today, price]

        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)


#print (get_price_new_mobile())
open_csv_file("pricesCVS.csv")