# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Scrapy item

import scrapy


class GetEmailsItem(scrapy.Item):
    url = scrapy.Field()
    email = scrapy.Field()