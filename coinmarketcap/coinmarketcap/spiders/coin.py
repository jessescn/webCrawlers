# -*- coding: utf-8 -*-
import scrapy
from coinmarketcap.items import CoinItem

class CoinSpider(scrapy.Spider):
    """Classe que representa o spider referente a extração dos dados acerca das moedas"""
    name = 'coin'
    start_urls = ['https://coinmarketcap.com/all/views/all/']

    def start_requests(self):
        """Metodo chamado ao executar o spider"""
        url = self.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Callback com os dados acerca de todas as moedas do site"""
        table = response.css("tbody tr")
        for row in table:
            coin = CoinItem(
                name=row.css("a.currency-name-container::text").get(),
                symbol=row.css("td.col-symbol::text").get(),
                market_cap=row.css("td.market-cap::text").get(),
                price=row.css("a.price::attr(data-usd)").get(),
                circulation_supply=row.css("td.circulating-supply span::attr(data-supply)").get(),
                volume=row.css("a.volume::attr(data-usd)").get())

            yield coin
