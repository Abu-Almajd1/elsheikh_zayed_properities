import scrapy
from propertyfinder.items import PropertyFinderItem

class PropertyfinderpropertySpider(scrapy.Spider):
    name = "propertyfinderspider"
    allowed_domains = ["propertyfinder.eg"]
    start_urls = [
        "https://www.propertyfinder.eg/en/search?l=28683&c=1&fu=0&ob=mr"
    ]

    def parse(self, response):
        # Extract property URLs from the outer page
        property_cards = response.xpath(
            '//div[@class="view_desktop_column--primary__ayoqS"]//a[@class="property-card-module_property-card__link__L6AKb"]/@href'
        ).getall()

        for property_url in property_cards:
            full_url = response.urljoin(property_url)
            yield scrapy.Request(url=full_url, callback=self.parse_details)

        # Handle pagination
        next_page = response.xpath('//a[@data-testid="pagination-page-next-link"]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)


    def parse_details(self, response):
        # Define a dictionary to hold scraped data
        item = PropertyFinderItem()

        # Extract data from the inner page
        item['url'] = response.url
        item['title'] = response.xpath('//h1[contains(@class, "styles_desktop_title__j0uNx")]/text()').get(default='N/A')
        item['price'] = response.xpath('//p[@data-testid="property-price"]/span[@data-testid="property-price-value"]/text()').get(default='N/A')
        item['location'] = response.xpath('//p[@class="styles-module_map__title__M2mBC"]/text()').get(default='N/A')
        item['property_type'] = response.xpath('//p[@data-testid="property-details-type"]/text()').get(default='N/A')
        item['bedrooms'] = response.xpath('//p[@data-testid="property-details-bedrooms"]/text()').get(default='N/A')
        item['bathrooms'] = response.xpath('//p[@data-testid="property-details-bathrooms"]/text()').get(default='N/A')
        item['area'] = response.xpath('//p[@data-testid="property-details-size"]/text()').get(default='N/A')
        item['available_from'] = response.xpath('//p[@data-testid="property-details-rental-availability-date"]/text()').get(default='N/A')
        item['description'] = " ".join(
            response.xpath('//article[@data-testid="dynamic-sanitize-html"]//text()').getall()
        ).strip()
        item['amenities'] = response.xpath(
            '//section[@data-testid="amenities-section"]//div[@class="styles_amenity__c2P5u"]/p[@class="styles_text__IlyiW"]/text()'
        ).getall()

        yield item