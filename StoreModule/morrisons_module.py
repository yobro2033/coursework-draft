import requests
from bs4 import BeautifulSoup as soup
import json

productInput = input("Please enter your product you want to find: ")
productURLInput = productInput.replace(" ","%20")
my_url = 'https://groceries.morrisons.com/search?entry=' + productURLInput
response = requests.get(my_url)
responseCode = str(response)
if responseCode == "<Response [200]>":
    print("We have found your product: " + productInput)
    productListFound = soup(response.text, 'html.parser')
    containers = productListFound.findAll('div',{"class":"fop-item fop-item-offer"})
    for container in containers:
        productLinkContainer = container.findAll('div',{"class":"fop-contentWrapper"})
        productLinkItem = productLinkContainer[0].a["href"]
        productLink = 'https://groceries.morrisons.com' + productLinkItem
        productImageContainer = container.find('div',{"class":"fop-img-wrapper"})
        productImageRef = productImageContainer.img["src"]
        productImage = 'https://groceries.morrisons.com' + productImageRef
        productName = productImageContainer.div.img["alt"]
        price_container = container.find('span',{"class":"fop-price price-offer"})
        productPrice = price_container.text
        #Some cases there is an extra pattern of HTML
        #Traceback (most recent call last):
        #   File "morrisons_module.py", line 23, in <module>
        #   productPrice = price_container.text
        #   AttributeError: 'NoneType' object has no attribute 'text'
        unitprice_container = container.find('span',{"class":"fop-unit-price"})
        productUnitPrice = unitprice_container.text
        #Some cases there is an extra pattern of HTML
        print("Product link: ", productLink)
        print("Product name: ", productName)
        print("Image: ",productImage)
        print("Price: ", productPrice)
        print("Price per unit: ", productUnitPrice)
        morrisons_table_data = []
        morrisons_table_data.append({
            'Product link: ': [productLink],
            'Product name: ': [productName],
            'Image': [productImage],
            'Price: ': [productPrice],
            'Price per unit: ': [productUnitPrice]
        })
        with open('m_data.txt', 'w') as outfile:
            json.dump(morrisons_table_data, outfile)
    print("Thank you for using our service!")
else:
    print("Please try again later!")
