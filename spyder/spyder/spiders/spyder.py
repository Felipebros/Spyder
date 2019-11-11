import scrapy

from decimal import Decimal


class Spyder(scrapy.Spider):
    name = 'spyder'
    start_urls = [
        'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_ve'\
        'nda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma='
    ]
    site = 'https://www.imoveismartinelli.com.br/'

    def parse(self, response):
        imoveis = response.xpath('//div[@id = "property-listing"]//div[@class'\
            ' = "row"]//div[re:test(@class, "item")]')
        for imovel in imoveis:
            price_2_xpath = imovel.xpath(
                './/div[@class = "price"]//span[2]/text()').get()
            if price_2_xpath != None:
                price_xpath = self.desmascarar_moeda(price_2_xpath)
            else:
                price_1_xpath = imovel.xpath(
                    './/div[@class = "price"]//span/text()').get()
                price_xpath = self.desmascarar_moeda(price_1_xpath)

            yield {
                'price': price_xpath,
                'area': self.desmascarar_area(imovel.xpath(
                    './/div[@class = "info"]//ul[@class = "amenities"]//li/te'\
                    'xt()').get()),
                'id': imovel.xpath('.//div[@class = "info"]//p[@class = "cor'\
                    'ta_desc"]//strong/text()').get(),
            }

        proxima_pagina = response.xpath('//div[re:test(@class, "paginatio'\
            'n")]//ul//li[last()]//a/@href').get()
        if proxima_pagina != 'JavaScript:void(0)':
            proxima_pagina = self.site + proxima_pagina
            yield scrapy.Request(proxima_pagina, callback=self.parse)


    def desmascarar_moeda(self, valor):
        try:
            valor = Decimal(float(valor.replace('R$', '').replace('.', '')
                .replace(',', '.')))
        except:
            return None
        return valor

    def desmascarar_area(self, valor):
        try:
            valor =  Decimal(float(valor.replace(' m', '')
                .replace(' ', '')))
        except:
            return None
        return valor