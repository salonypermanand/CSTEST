from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def FoodCategory():
    article_text=''
    req = Request('https://www.chewy.com/b/dog-288', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    article = soup.find("div", {"class": "dept__popover__content"}).findAll('a')
    for val in article:
        article_text += '\n' + ''.join(val.findAll(text=True))
    print(article_text)

def wetfood():
    req = Request('https://www.chewy.com/b/wet-food-293', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup1 = BeautifulSoup(webpage, 'html.parser')
    for link in soup1.find_all('a',
                          attrs={'href': re.compile("^https://")}):
       print(link.get('href'))

def pagescount():
    req = Request('https://www.chewy.com/b/wet-food-293', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup1 = BeautifulSoup(webpage, 'html.parser')
    list = soup1.find_all('ul', {'class': 'kib-pagination-new__list'})
    for el in soup1.find_all('li', attrs={'class': 'kib-pagination-new__list-item'}):
        pages = el.get_text()
    pages = int(pages)
    print("NUMBER OF PAGES TO BE OPEN----%d" % pages)

def productDetail():
    req = Request('https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup1 = BeautifulSoup(webpage, 'html.parser')
    all_scripts = soup1.find_all("script", {"src":False})
    all_scripts=(all_scripts[18].text.strip()[118:-1])
    reqdData=(str(all_scripts).replace("'",'"').replace('canonicalURL','"canonicalURL"').replace('ajaxURL','"ajaxURL"').replace('sku','"sku"').replace('images','"images"').replace('price','"price"').replace(",\n                     ]", "]"))
    data = json.loads(reqdData)
    print("Images from Json Are:")
    print(data['381335']['images'],data['141436']['images'],data['141437']['images'],data['141438']['images'])
    print("Product Price from Json Are:")
    print(data['381335']['price'], data['141436']['price'], data['141437']['price'], data['141438']['price'])
    print("Size Is:" + soup1.find('title').text[-21:-16])
    for el in soup1.find("div", {"id": "product-title"}).findAll('h1'):
        print("Product Name is" + el.get_text())
    for el in soup1.find("section", {"class": "descriptions__content cw-tabs__content--left"}).find('p'):
        print("Description is" + el.get_text())
    for el in soup1.find("section", {"class": "descriptions__content cw-tabs__content--left"}).findAll('ul'):
        print("Key Benfilte Are" +el.get_text())
    for element in soup1.find("article", {"id": "Nutritional-Info"}).findAll('section',class_='cw-tabs__content--left'):
        print("Ingredients: ", element.find("p").text)
    for element in soup1.find("div", {"class": "pdp-align"}).findAll('div',class_='pdp-ext-content'):
        brand=str(element.find("h2").text).split()[1]
        print("Brand Name: ", brand)

