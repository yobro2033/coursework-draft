import requests
from bs4 import BeautifulSoup as soup
import json
productInput = input("Please enter your product you want to find: ")
productURLInput = productInput.replace(" ","%20")
my_url = 'https://www.iceland.co.uk/search?q=' + productURLInput
response = requests.get(my_url)
responseCode = str(response)
if responseCode == "<Response [200]>":
    print("We have found your product: " + productInput)
    productListFound = soup(response.text, 'html.parser')
    containers = productListFound.findAll("div",{"class":"product-tile"})
    for container in containers:
        productLinkContainer = container.find("div",{"class":"product-image"})
        productLinkItem = productLinkContainer.a["href"]
        productName = productLinkContainer.a["title"]
        productImage = productLinkContainer.a.picture.img["src"]
        price_container = container.find("span",{"class":"product-sales-price"})
        productPrice = price_container.text
        unitprice_container = container.find("div",{"class":"product-pricing-info"})
        productUnitPrice = unitprice_container.text
        print("Product link: ", productLinkItem)
        print("Product name: ", productName)
        print("Image: ",productImage)
        print("Price: ", productPrice)
        print("Price per unit: ", productUnitPrice)
        iceland_table_data = []
        iceland_table_data.append({
            'Product link: ': [productLinkItem],
            'Product name: ': [productName],
            'Image': [productImage],
            'Price: ': [productPrice],
            'Price per unit: ': [productUnitPrice]
        })
        with open('i_data.txt', 'w') as outfile:
            json.dump(iceland_table_data, outfile)
    print("Thank you for using our service!")
else:
	print("Please try again later!")
