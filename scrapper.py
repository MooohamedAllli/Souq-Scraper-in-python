import os
import requests
from parsel import Selector
import csv

def checkNull(word):
    word = str(word)
    if word==" ":
        return 'None'
    else:
        return word

if os.path.exists('E:\Py Projects\SouqScrapper\SouqProducts.csv'):
    filecsv = open('SouqProducts.csv', 'a')
    FileStatus = 'append'
else:
    filecsv = open('SouqProducts.csv', 'w')

productCategory = 'wigs'
URL = 'https://egypt.souq.com/eg-en/'+productCategory+'/l/?page='

csv_columns = ['title', 'price', 'rateInfo']

for page in range(1):
    content = requests.get(URL+str(page+1))
    select = Selector(text=content.text)
    products = select.xpath('//div[@class="column column-block block-grid-large single-item"]')
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    if FileStatus != 'append':
       writer.writeheader()
    for pt in products:
        title = str(pt.xpath('.//a[@class="itemLink block sPrimaryLink"]/text()').get())
        price = pt.xpath('.//span[@class="itemPrice"]/text()').get()
        rateI = str(pt.xpath('.//i[@class="star-rating-svg"]/i/@style').get()).removeprefix('width:')
        writer.writerow({'title': checkNull(title), 'price': checkNull(price), 'rateInfo': checkNull(rateI)})
filecsv.close()