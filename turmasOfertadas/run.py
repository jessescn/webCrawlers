import os
from dotenv import load_dotenv

from turmasOfertadas import SubjectsSpider
from scrapy.crawler import CrawlerProcess

load_dotenv()


def setup_process(export_json=False):
    
    settings = {
        'LOG_ENABLED': False
    }

    if export_json:
        settings['FEED_FORMAT'] = 'json'
        settings['FEED_URI'] = 'subjects.json'
        settings['FEED_EXPORT_ENCODING'] = 'utf-8'

    process = CrawlerProcess(settings=settings)

    return process

def run_spider(export_json=False):

    process = setup_process(export_json)

    enrollment = os.getenv('MATRICULA')
    password = os.getenv('SENHA')

    process.crawl(SubjectsSpider, matricula=enrollment, senha=password)
    process.start()
    # Agora as turmas estão na variavel abaixo
    turmas = SubjectsSpider.items

if __name__ == '__main__':
    run_spider(export_json=True)