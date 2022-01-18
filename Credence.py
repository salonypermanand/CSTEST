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
    for el in soup1.find("div", {"class": "cw-tabs__body container"}).findAll('p'):
        print(el.get_text())
