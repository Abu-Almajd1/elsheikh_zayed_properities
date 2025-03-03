import scrapy
from bayut.items import BayutItem

class BayutspiderSpider(scrapy.Spider):
    name = "bayutspider"
    allowed_domains = ["www.bayut.eg"]
    start_urls = ["https://www.bayut.eg/en/giza/properties-for-sale-in-sheikh-zayed/"]

    def parse(self, response):
        # Extract all URLs matching the pattern
        detail_urls = response.xpath('//a[contains(@href, "/en/property/details-")]/@href').getall()
        for url in detail_urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(url=full_url, callback=self.parse_details)

        # Handle pagination
        next_page = response.xpath('//a[@title="Next"]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        item = BayutItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="d8b96890 fontCompensation"]/text()').get()
        item['price_amount'] = response.xpath('//div[contains(@class, "_2923a568")]//span[@aria-label="Price"]/text()').get(default='N/A')
        item['location_address'] = response.xpath('//div[@aria-label="Property header"]/text()').get(default='N/A')
        item['bedrooms'] = response.xpath('//span[@aria-label="Beds"]//span[@class="_140e6903"]/text()').get(default='N/A')
        item['bathrooms'] = response.xpath('//span[@aria-label="Baths"]//span[@class="_140e6903"]/text()').get(default='N/A')
        item['property_area'] = response.xpath('//span[@aria-label="Area"]//span[@class="_140e6903"]/span/text()').get(default='N/A')
        item['description'] = " ".join(response.xpath('//div[@aria-label="Property description"]//span[@class="_3547dac9"]/text()').getall())
        item['type'] = response.xpath('//li[span[text()="Type"]]/span[@aria-label="Type"]/text()').get(default='N/A')
        item['purpose'] = response.xpath('//li[span[text()="Purpose"]]/span[@aria-label="Purpose"]/text()').get(default='N/A')
        item['reference'] = response.xpath('//li[span[text()="Reference no."]]/span[@aria-label="Reference"]/text()').get(default='N/A')
        item['completion_status'] = response.xpath('//li[@aria-label="Property completion status"]/span[@aria-label="Completion status"]/text()').get(default='N/A')
        item['furnishing_status'] = response.xpath('//li[@aria-label="Property furnishing status"]/span[@aria-label="Furnishing"]/text()').get(default='N/A')
        item['date_posted'] = response.xpath('//li[span[text()="Added on"]]/span[@aria-label="Reactivated date"]/text()').get(default='N/A')
        item['ownership'] = response.xpath('//li[span[text()="Ownership"]]/span[@aria-label="Ownership"]/text()').get(default='N/A')
        item['amenities'] = response.xpath('//div[@class="_01ade828"]/span[@class="_7181e5ac"]/text()').getall()
        item['agent_name'] = response.xpath('//span[@aria-label="Agency name"]/text()').get(default='N/A')
        yield item