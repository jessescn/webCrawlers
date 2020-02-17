import scrapy
from items import SubjectItem

def authentation_failed(response):
    """ Função para checar se a autenticação falhou """
    return response.css('div.alert p::text').get() == 'Erro'

class SubjectsSpider(scrapy.Spider):

    name = 'turmas'
    start_urls = ['https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/Controlador?command=Home']
    items = []

    def __init__(self, matricula=None, senha=None):
        self.matricula = matricula
        self.senha = senha

    def parse(self, response):

        return scrapy.FormRequest.from_response(
            response,
            formdata={'login': self.matricula, 'senha':self.senha},
            callback=self.after_login
        )

    def after_login(self, response):

        if not authentation_failed(response):
            yield scrapy.Request(response.urljoin('?command=AlunoDisciplinasOfertadas'),
                                                     callback=self.get_subjects)
        else:
            print('\nCredenciais inválidas!\n')


    def get_subjects(self, response):

        table = response.xpath('//table[@id="tabOferta"]/tbody/tr')
        for line in table:
            values = line.xpath('./td//text()').getall()

            data = [value.replace('\r', '').replace('\n','') for value in values if value != '']

            subjectCode , subjectIndex = data[1].split(' - ')

            subject = SubjectItem(
                                periodo=data[0],
                                codigo=subjectCode,
                                turma=subjectIndex,
                                disciplina=data[2],
                                horarios=[data[3], data[4]],
                                oferta=data[-1])

            self.items.append(subject)

            yield  subject
