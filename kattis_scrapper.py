"""
Scrapper for getting point of each problem in Kattis Website

v.1.1.1
"""

from attr import s
import requests
from bs4 import BeautifulSoup
import re 
import time 

class PointScrapper: 
    def getPoints(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        return str(soup.find('span', class_='difficulty_number').get_text())