# usage: scrapy crawl single_page_spider_simplified
#  -a category=https://www.snopes.com/fact-check/teenage-daughter-shirt-pregnant/
# this version is collect simplified information


import scrapy
import re
import pandas as pd
from scrapy.selector import Selector
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from single_page_scraper.items import SinglePageScraperItem


class SinglePageSpiderSimplified(scrapy.Spider):
    def __init__(self):
        self.n = 7
        self.d = pd.read_csv('/Users/apple/fakenews/single_page_scraper/single_page_scraper/TitleAndLink2.csv',
                             usecols=['title', 'link'])
        # self.driver = webdriver.Chrome(executable_path='/Users/apple/Downloads/chromedriver')
        self.start_urls = [self.d.iat[self.n, 1]]

    name = 'single_page_spider_simplified'

    # def __init__(self,
    #              category='https://www.snopes.com/fact-check/accused-russian-spy-mariia-butina-photographed-oval-office/'):
    #     self.start_urls = [category]

    def parse(self, response):
        # self.driver.get(response.url)
        # hxs = Selector(text=self.driver.page_source)
        ARTICLE_SELECTOR = '.article-text-inner'
        RATING_SELECTOR = '.rating-wrapper'


        temp_img = "".join(response.css(ARTICLE_SELECTOR).css('img ').extract())
        temp_script = "".join(response.css('head').css('script').extract())
        self.n += 1
        if self.n >= self.d.iloc[:, 0].size:
            return
        print(self.n)
        rating = response.css(RATING_SELECTOR).css('span ::text').extract_first()
        # if rating is None:
        #     rating = 'NULL'
        # else:
        #     rating = rating.lower()

        if len(re.findall(r'srcset="(.*?)[,|"]', temp_img)) > 0 and not (rating is None):
            yield {
                'id': self.n,
                'image_url': re.findall(r'srcset="(.*?)[\?|,|"]', temp_img)[0],  # list
                'permalink': "".join(re.findall(r'permalink: \'(.*?)\'', temp_script)),
                'tweet_id': response.css('.article-text-inner').css('.twitter-tweet ::text').extract()
            }

        # next_page = 'https://www.snopes.com/fact-check/gareth-southgate-waistcoat/'

        next_page = self.d.iat[self.n, 1]

        # print(next_page)
        if next_page:
            # normal page

            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse,
                dont_filter=True
            )
        # self.driver.close()
        print("Done!")
