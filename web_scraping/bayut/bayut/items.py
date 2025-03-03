# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BayutItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price_amount = scrapy.Field()
    location_address = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    property_area = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    purpose = scrapy.Field()
    reference = scrapy.Field()
    completion_status = scrapy.Field()
    furnishing_status = scrapy.Field()
    date_posted = scrapy.Field()
    ownership = scrapy.Field()
    amenities = scrapy.Field()
    agent_name = scrapy.Field()
    #price_per_meter = scrapy.Field()