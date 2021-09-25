import requests
from bs4 import BeautifulSoup as soup
import json

productInput = input("Please enter your product you want to find: ")
productURLInput = productInput.replace(" ","%20")
my_url = 'https://groceries.morrisons.com/webshop/api/v1/search?searchTerm=' + productURLInput
response = requests.get(my_url)
responseCode = str(response)
if responseCode == "<Response [200]>":
    productListFound = soup(response.text, 'html.parser')
    productListJson = json.loads(str(productListFound))
    if 'mainFopCollection' in productListJson:
        print("We have found your product: " + productInput)
        containers = productListJson['mainFopCollection']['sections']
        for container in containers:
            productContainer = container['fops']
            for container in productContainer:
                productSku = container['sku']
                productLink = 'https://groceries.morrisons.com/products/-' + productSku
                if 'product' in container:
                    productName = container['product']['name']
                    productImage = 'https://groceries.morrisons.com/productImages/116/116564011_0_640x640.jpg'
                    productPrice = container['product']['price']['current']
                    productUnitPrice = container['product']['price']['unit']['price']
                    unit = container['product']['price']['unit']['per']
                    print("Product link: ", productLink)
                    print("Product name: ", productName)
                    print("Image: ",productImage)
                    print("Price: ", productPrice)
                    print("Price per unit: ", productUnitPrice, unit)
                    morrisons_table_data = []
                    morrisons_table_data.append({
                        'Product link: ': [productLink],
                        'Product name: ': [productName],
                        'Image': [productImage],
                        'Price: ': [productPrice],
                        'Price per unit: ': [productUnitPrice],
                        'Unit': [unit]
                        })
                    with open('m_data.txt', 'w') as outfile:
                        json.dump(morrisons_table_data, outfile)
                else:
                    pass
    else:
        print("Not available!")
    print("Thank you for using our service!")
else:
    print("Please try again later!")
