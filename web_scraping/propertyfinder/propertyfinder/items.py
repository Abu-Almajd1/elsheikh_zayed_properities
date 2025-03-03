# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class PropertyFinderItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    property_type = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    area = scrapy.Field()
    available_from = scrapy.Field()
    description = scrapy.Field()
    amenities = scrapy.Field()