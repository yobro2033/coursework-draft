import requests
from bs4 import BeautifulSoup as soup
import json

productInput = input("Please enter your product you want to find: ")
productURLInput = productInput.replace(" ","+")
my_url = 'https://www.tesco.com/groceries/en-GB/search?query=' + productURLInput
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(my_url, headers=headers)
responseCode = str(response)
if responseCode == "<Response [200]>":
    print("We have found your product: " + productInput)
    productListFound = soup(response.text, 'html.parser')
    containers = productListFound.findAll("div",{"class":"product-tile-wrapper"})
    for container in containers:
        productLinkContainer = container.find("div",{"class":"tile-content"})
        productLinkItem = productLinkContainer.a["href"]
        productLink = 'https://www.tesco.com' + productLinkItem
        productImageContainer = container.find("div",{"class":"product-image__container"})
        productImage = productImageContainer.img["src"]
        productName = productImageContainer.img["alt"]
        price_container = container.find("div",{"class":"price-per-sellable-unit price-per-sellable-unit--price price-per-sellable-unit--price-per-item"})
        productPrice = price_container.div.text
        #some cases it have div some cases not, make sure it's dynamic
        unitprice_container = container.find("div",{"class":"price-per-quantity-weight"})
        print(unitprice_container)
        productUnitPrice = unitprice_container.span.text
        unitprice_weight_container = unitprice_container.find("span",{"class":"weight"})
        unitprice_weight = unitprice_weight_container.text
        #some cases it have span some cases not, make sure it's dynamic
        print("Product link: ", productLink)
        print("Product name: ", productName)
        print("Image: ", productImage)
        print("Price: ", productPrice)
        print("Price per unit: " + productUnitPrice + " " + unitprice_weight )
        tesco_table_data = []
        tesco_table_data.append({
            'Product link: ': [productLink],
            'Product name: ': [productName],
            'Image': [productImage],
            'Price: ': [productPrice],
            'Price per unit: ': [productUnitPrice + " " + unitprice_weight]
        })
        with open('t_data.txt', 'w') as outfile:
            json.dump(tesco_table_data, outfile)
    print("Thank you for using our service!")
else:
	print("Please try again later!")
