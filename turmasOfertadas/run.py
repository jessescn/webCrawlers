import os
from dotenv import load_dotenv

from turmasOfertadas import TurmasSpider
from scrapy.crawler import CrawlerProcess

load_dotenv()

def run_spider():

    process = CrawlerProcess(settings={
        'LOG_ENABLED': False
    })

    enrollment = os.getenv('MATRICULA')
    password = os.getenv('SENHA')

    process.crawl(TurmasSpider, matricula=enrollment, senha=password)
    process.start()
    # Agora as turmas estão na variavel abaixo
    turmas = TurmasSpider.items

if __name__ == '__main__':
    run_spider()