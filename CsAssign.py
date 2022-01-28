import requests
from bs4 import BeautifulSoup
link = "https://daiyafoods.com/food-service/"
headers={'User-Agent': 'Mozilla/5.0'}
result = requests.get(link, headers=headers)
soup = BeautifulSoup(result.content.decode(), 'html.parser')
product=''
article = soup.find("div", {"class": "-df-homeProductsCarouselScroll carouselScroll df2020-slides fs-slides"}).findAll('p')
for val in article:
    product += ''.join(val.findAll(text=True))
print("Available Product Name are"+product)

