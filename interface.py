import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append('/Users/apple/fakenews/single_page_scraper/single_page_scraper')
import pandas as pd
from twisted.internet import reactor



from scrapy.crawler import CrawlerProcess
from single_page_scraper.spiders.scraper_thread import SinglePageSpiderThread

from scrapy.utils.project import get_project_settings

# print(os.getcwd())
# print(sys.executable)
reactor.suggestThreadPoolSize(30)
print(sys.argv[1])
begin = int(sys.argv[1])
d = pd.read_csv('./single_page_scraper/TitleAndLink2.csv', usecols=['title', 'link'], skiprows=range(1,begin), nrows=10)
#
print(d)
process = CrawlerProcess(get_project_settings())
i=1
for website in d.link:
    process.crawl(SinglePageSpiderThread, category=website,n=begin+i)
    i+=1

process.start()  # the script will block here until the crawling is finished
