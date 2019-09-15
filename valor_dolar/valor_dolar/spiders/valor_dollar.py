# -*- coding: utf-8 -*-
import scrapy


class ValorDollarSpider(scrapy.Spider):
    name = 'valor_dollar'
    start_urls = ['https://www.melhorcambio.com/dolar-hoje']

    def parse(self, response):
        valor = response.css('[id="comercial"]::attr(value)').get()
        print("\nO valor atual do dolar é {}\n".format(valor))
        yield valor
