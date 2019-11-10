import scrapy


class Spyder(scrapy.Spider):
    name = 'spyder'

    start_urls = ['https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=']

    def parse(self, response):
        import ipdb; ipdb.set_trace()
        pass