# usage: scrapy crawl single_page_spider -a category=https://www.snopes.com/fact-check/teenage-daughter-shirt-pregnant/
# this version is for multiple thread use in interface.py

import scrapy
import re


class SinglePageSpiderThread(scrapy.Spider):

    name = 'single_page__thread_spider'

    def __init__(self,
                 category='https://www.snopes.com/fact-check/accused-russian-spy-mariia-butina-photographed-oval-office/',n=1):
        self.start_urls = [category]
        self.n = n

    def parse(self, response):

        ARTICLE_SELECTOR = '.article-text-inner'
        RATING_SELECTOR = '.rating-wrapper'

        temp_img = "".join(response.css(ARTICLE_SELECTOR).css('img ').extract())
        temp_script = "".join(response.css('head').css('script').extract())

        rating = response.css(RATING_SELECTOR).css('span ::text').extract_first()
        if rating is None:
            rating = 'NULL'
        else:
            rating = rating.lower()
        yield {
            'id': self.n,
            'claim': response.css(ARTICLE_SELECTOR).css('p ::text').extract_first().strip(),
            'rating': rating,
            'image_url': re.findall(r'srcset="(.*?)[,|"]', temp_img),  # list
            'permalink': "".join(re.findall(r'permalink: \'(.*?)\'', temp_script)),
            'publish_date': "".join(re.findall(r'datePublished : \'(.*?)\'', temp_script))

        }

        print("Done!")
