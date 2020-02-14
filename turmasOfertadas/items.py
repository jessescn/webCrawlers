import scrapy

class ClasseItem(scrapy.Item):

    periodo = scrapy.Field()
    codigo = scrapy.Field()
    turma = scrapy.Field()
    disciplina = scrapy.Field()
    horarios = scrapy.Field()
    oferta = scrapy.Field()