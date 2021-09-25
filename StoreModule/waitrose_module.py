import requests
from bs4 import BeautifulSoup as soup
import re
productInput = input("Please enter your product you want to find: ")
productURLInput = productInput.replace(" ","%20")
my_url = 'https://www.waitrose.com/ecom/shop/search?&searchTerm=' + productURLInput
response = requests.get(my_url)
responseCode = str(response)
if responseCode == "<Response [200]>":
    print("We have found your product: " + productInput)
    productListFound = soup(response.text, 'html.parser')
    containers = productListFound.findAll("div",{"class":"container-fluid"})
    for container in containers:
        productLinkContainer = container.find("header", attrs={"class": True})
        print(productLinkContainer)
        productLinkItem = productLinkContainer.a["href"]
        productLink = 'https://www.waitrose.com' + productLinkItem
        productNameContainer = container.findAll("span",{"class":"name___CmYia"})
        productName = productNameContainer[0].text
        price_container = container.findAll("div",{"class":"prices___1JkR4"})
        productPrice = price_container.span.p.span["text"]
        unitprice_container = container.findAll("div",{"class":"pricePerUnit___1gifh priceInfo___1J8aK"})
        productUnitPrice = unitprice_container.p.text
        print("Product link: ", productLink)
        print("Product name: ", productName)
        print(productImage)
        print("Price: ", productPrice)
        print("Price per unit: ", productUnitPrice)
	waitrose_table_data = []
        waitrose_table_data.append({
            'Product link: ': [productLink],
            'Product name: ': [productName],
            'Image': [productImage],
            'Price: ': [productPrice],
            'Price per unit: ': [productUnitPrice]
        })
        with open('w_data.txt', 'w') as outfile:
            json.dump(waitrose_table_data, outfile)
else:
	print("Please try again later!")
