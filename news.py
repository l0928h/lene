# -*- coding:utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class Spider(scrapy.Spider):
    name = "news"
    start_urls = ('https://tw.stock.yahoo.com/news_list/url/d/e/N1.html',)

def parse(self, response):
    sp = BeautifulSoup(response.body, "html.parser")
    news = sp.select('#newListTable a.mbody')
    content = list()
    for headline in news:
        temp = dict()
        temp['title'] = headline.text
        temp['url'] = headline['href']
        content.append(temp)
    print(content)