from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient()
db = client.mydata
collection = db.dailynews

url = 'https://tw.****daily.com/hot/daily'

news_page = requests.get(url)
news = BeautifulSoup()