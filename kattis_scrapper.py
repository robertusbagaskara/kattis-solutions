import requests
from bs4 import BeautifulSoup
import re 
# import time 

# start_time = time.time()

class PointScrapper: 
    def getPoints(self, url):
        r = requests.get(url)
        # point = re.search("<span>...</span>|", str(r.content))
        # return point.group().replace("<span>", "").replace("</span>", "")
        soup = BeautifulSoup(r.content, 'html5lib')
        return(str(soup.find_all('span')[-1]).replace("<span>", "").replace("</span>", ""))  

# test = PointScrapper()
# test.getPoints("https://open.kattis.com/problems/logo")

# print("--- Done in %s seconds ---" % (time.time() - start_time))