import requests
from bs4 import BeautifulSoup
import json

productInput = input("Please enter your product you want to find: ")
productURLInput = productInput.replace(" ","%20")
my_url = 'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]=' + productURLInput
response = requests.get(my_url).json()
print("We have found your product: " + productInput)
print(response)
sainsbury_table_data = []
for departure in response['products']:
    sainsbury_table_data.append({
       'Product link: ': departure['full_url'],
       'Product name: ': departure['name'],
       'Image': departure['image'],
       'Price: ': departure['retail_price'],
       'Price per unit: ': departure['unit_price']
    })
with open('s_data.txt', 'w') as outfile:
    json.dump(sainsbury_table_data, outfile)
print(sainsbury_table_data)
print("Thank you for using our service!")
