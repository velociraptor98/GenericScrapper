import scrapy


class TestSpider(scrapy.Spider):
    name = "caratlane"
    allowed_domains = ["www.caratlane.com"]
    start_urls = ["https://www.caratlane.com/jewellery/rings.html"]

    def parse(self, response):
        print("REACHED")
        testSelector = response.css('.bottomContainer')
        for selector in testSelector:
            yield {
                'price': selector.css('div>p>span::text').extract_first(),
                'name': selector.css('.css-x56fp3::text').extract_first()
            }
        next_page_link = response.css('li.next a::attr(href)').extract_first()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)