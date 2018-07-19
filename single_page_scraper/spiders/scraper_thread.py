import scrapy
import re
import pandas as pd
# usage: scrapy crawl single_page_spider -a category=https://www.snopes.com/fact-check/teenage-daughter-shirt-pregnant/

from single_page_scraper.items import SinglePageScraperItem


class SinglePageSpiderThread(scrapy.Spider):

    name = 'single_page__thread_spider'

    def __init__(self,
                 category='https://www.snopes.com/fact-check/accused-russian-spy-mariia-butina-photographed-oval-office/'):
        self.start_urls = [category]

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
            'claim': response.css(ARTICLE_SELECTOR).css('p ').extract_first().strip(),
            'rating': rating,
            'image_url': re.findall(r'srcset="(.*?)[,|"]', temp_img),  # list
            'permalink': "".join(re.findall(r'permalink: \'(.*?)\'', temp_script)),
            'publish_date': "".join(re.findall(r'datePublished : \'(.*?)\'', temp_script))

        }
        # item = SinglePageScraperItem()
        # item['id'] = self.n
        # claim = response.css(ARTICLE_SELECTOR).css('p ::text').extract_first().strip()
        # item['claim'] = claim
        #
        # rating = response.css(RATING_SELECTOR).css('span ::text').extract_first()
        # if rating is None:
        #     item['rating'] = 'NULL'
        # else:
        #     item['rating'] = rating.lower()
        #
        # item['image_url'] = re.findall(r'srcset="(.*?)[,|"|\?]', temp_img),
        # item['permalink'] = "".join(re.findall(r'permalink: \'(.*?)\'', temp_script)),
        # item['publish_date'] = "".join(re.findall(r'datePublished : \'(.*?)\'', temp_script))
        # # yield item


        print("Done!")
