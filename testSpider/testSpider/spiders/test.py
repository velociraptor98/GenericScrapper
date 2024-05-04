import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["www.giva.co"]
    start_urls = ["https://www.giva.co/collections/rings","https://www.giva.co/collections/pendants"]

    def parse(self, response):
        testSelector = response.css('.card__information')
        for selector in testSelector:
            yield {
                'price': selector.css('.price__container .price__regular .price-item::text').extract_first(),
                'name': selector.css('.card__heading>a::text').extract_first()
            }
        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)