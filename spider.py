import scrapy

pass_list = ["/de", "/en", "http", "pdf", "zip", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "png", "jpg", "jpeg", "gif", "bmp", "tiff", "ico", "svg", "webp", "tel", "mailto"]
pages_processed = []
max_pages = 1000

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.deklerkbv.nl/nl",
    ]
    count = 0
    
    def parse(self, response):
        for content in response.xpath("//body"):
            yield {
                "url": response.url,
                "title": content.xpath("//h1").get(),
            }

        pages = response.xpath("//a/@href").getall()
        if pages is not None:
            for page in pages:
                if page not in pages_processed and not any(part in page.lower() for part in pass_list) and self.count < max_pages:
                    pages_processed.append(page)
                    print("PROCESSING: ", page)
                    yield response.follow(page, self.parse)
                    self.count = self.count+1
