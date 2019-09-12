import scrapy

class AosFatosSpider(scrapy.Spider):
    name = "aos_fatos"

    start_urls = ["https://aosfatos.org/"]

    def parse(self, response):
        """Callback da página inicial"""
        links = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
        for link in links:
            yield scrapy.Request(response.urljoin(link), callback=self.parse_category)

    def parse_category(self, response):
        """Callback para pegar todas as noticias em uma pagina"""
        news  = response.css(".card::attr(href)").getall()
        for new in news:
            yield scrapy.Request(response.urljoin(new), callback=self.parse_new)
        
        pages_url = response.css('.pagination a::attr(href)').getall()
        for page in pages_url:
            yield scrapy.Request(response.urljoin(page), callback=self.parse_category)

    def parse_new(self, response):
        """Callback para pegar as informações de uma noticia"""
        title =  response.css('article h1::text').getall()
        date = ' '.join(response.css('p.publish_date::text').get().split())
        quotes =  response.css('article blockquote p')
        for quote in quotes:
            quote_text = quote.css('::text').get()
            status = quote.xpath(
                './parent::blockquote/preceding-sibling::figure//figcaption//text()').get()

            yield {
                'title': title,
                'date': date,
                'url': response.url,
                'status': status,
                'quote_text': quote_text
            }
