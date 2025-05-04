"""
Scrapper for getting point of each problem in Kattis Website

v.1.1.1
"""

import requests
from bs4 import BeautifulSoup

class PointScrapper: 
    def getPoints(self, url):
        r = requests.get(url)
        #soup = BeautifulSoup(r.content, 'html5lib')
        soup = BeautifulSoup(r.content, "lxml")
        return str(soup.find('span', class_='difficulty_number').get_text())