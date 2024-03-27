#Importing libraries
import requests
from bs4 import BeautifulSoup as BS

# Parsing data
r = requests.get("https://www.marktplaats.nl/q/lego+poppetjes/")
html = BS(r.content, 'html.parser')

# Checking the data
if html != 0:
    kek = "Data received"
    
print(kek)

# Displays information about all received objects
page = 1

while True:
    r = requests.get("https://www.marktplaats.nl/q/lego+poppetjes/p/" + str(page) + "/")
    html = BS(r.content, 'html.parser')
    pages = html.select(".hz-Listings--list-view > .hz-Listing--list-item ")
    
    if (len(pages)):
        for el in pages:
            tittle = el.find("h3", {"class": "hz-Listing-title"}).text
            cost = el.find("span", {"class": "hz-Listing-price"}).text
            img = el.find("img").get("src")
            url = el.find("a", {"class": "hz-Link hz-Link--block hz-Listing-coverLink"}).get("href")
            
            print(f'Product: \n {tittle}', f'\nPrice: \n {cost}', f'\nPicture: \n {img}')
            print(f'Url: \n https://www.marktplaats.nl' + str(url) + f'\n')
        page += 1
    else:
        break

