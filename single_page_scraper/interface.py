
import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append('/Users/apple/fakenews/single_page_scraper/single_page_scraper')
import pandas as pd
from twisted.internet import reactor



# reactor.suggestThreadPoolSize(30)
print(sys.path)
from scrapy.crawler import CrawlerProcess
from single_page_scraper.spiders.scraper import SinglePageSpider

from scrapy.utils.project import get_project_settings
# print(os.getcwd())
# print(sys.executable)

# skiprows=[1,sys.argv[1]]
# d = pd.read_csv('./TitleAndLink2.csv', usecols=['title', 'link'], skiprows=skiprows,nrows=30)
#
# process = CrawlerProcess(get_project_settings())
# for website in d.link:
#     process.crawl(SinglePageSpider, category=website)
#
# process.start()  # the script will block here until the crawling is finished
