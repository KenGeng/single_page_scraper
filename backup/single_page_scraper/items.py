

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinglePageScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # when use scraper.py, uncomment following code
    # id = scrapy.Field()
    # claim = scrapy.Field()
    # rating = scrapy.Field()
    # image_url = scrapy.Field()
    # permalink = scrapy.Field()
    # publish_date = scrapy.Field()

    # when use scraper_simplified.py, uncomment following code
    id = scrapy.Field()
    image_url = scrapy.Field()
    permalink = scrapy.Field()
