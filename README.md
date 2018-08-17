# single_page_scraper
single page scraper on snope.com

## Description
This s spider based on Scrapy framework to crawl each page of snopes.com (pages like:https://www.snopes.com/fact-check/spanish-cafe-video/)

## Dependency
1. Python3.6
2. Scrapy

## Usage
In the single_page_scraper/spiders/scraper.py, you can change csv file path to fulfill your needs.
```python
scrapy crawl single_page_spider
```
the output file's format or name can be modified in pipelines.py
## Other Details
There are 3 spiders in `single_page_scraper/spiders/`. : `scraper.py` is the basic one; `scraper_simplified.py` produces simplified information; `scraper_thread.py` is a multi-thread version, but not finsihed.

`single_page_scraper/interface.py` is a multi-thread version,  which is much faster, but it can't work well when there are more than 100 pages. If you want to use it, just `python interface.py`
