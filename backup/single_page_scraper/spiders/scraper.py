# usage: scrapy crawl single_page_spider


import scrapy
import re
import pandas as pd


from single_page_scraper.items import SinglePageScraperItem


class SinglePageSpider(scrapy.Spider):
    def __init__(self):
        self.n = 0
        self.d = pd.read_csv('/Users/apple/fakenews/single_page_scraper/single_page_scraper/TitleAndLink2.csv',
                             usecols=['title', 'link'])
        self.start_urls = [self.d.iat[self.n, 1]]

    name = 'single_page_spider'

    # def __init__(self,
    #              category='https://www.snopes.com/fact-check/accused-russian-spy-mariia-butina-photographed-oval-office/'):
    #     self.start_urls = [category]

    def parse(self, response):
        ARTICLE_SELECTOR = '.article-text-inner'
        RATING_SELECTOR = '.rating-wrapper'
        temp_img = "".join(response.css(ARTICLE_SELECTOR).css('img ').extract())
        temp_script = "".join(response.css('head').css('script').extract())
        self.n += 1
        if self.n >= self.d.iloc[:, 0].size:
            return

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
        # # above yield code can work well; the following code commented is another way. But, it uses [[ instead of [ for url and link
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
        # yield item

        # next_page = 'https://www.snopes.com/fact-check/gareth-southgate-waistcoat/'

        next_page = self.d.iat[self.n, 1]

        # print(next_page)
        if next_page :
            # normal page
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse,
                dont_filter=True
            )
        print("Done!")
