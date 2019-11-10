import scrapy


class Spyder(scrapy.Spider):
    name = 'spyder'
    start_urls = [
        'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_ve'\
        'nda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma='
    ]

    def parse(self, response):
        imoveis = response.xpath('//div[@id = "property-listing"]//div[@class = "row"]//div[re:test(@class, "item")]')
        for imovel in imoveis:
            id_xpath = imovel.xpath('.//div[@class = "info"]//p[@class = "corta_desc"]//strong/text()').get()
            price_2_xpath = imovel.xpath('.//div[@class = "price"]//span[2]/text()').get()
            price_1_xpath = imovel.xpath('.//div[@class = "price"]//span/text()').get()
            if price_2_xpath != None:
                price_xpath = price_2_xpath
            else:
                price_xpath = price_1_xpath
            
            area_xpath = imovel.xpath('.//div[@class = "info"]//ul[@class = "amenities"]//li/text()').get()
            print(dict(id=id_xpath, price=price_xpath, area=area_xpath))