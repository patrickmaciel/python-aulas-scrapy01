import scrapy

class SpiderCitacoes(scrapy.Spider):
    name = 'citacoes2'

    start_urls = [
        'http://quotes.toscrape.com/page/1',
        'http://quotes.toscrape.com/page/2',
    ]

    def parse(self, response):
        pagina = response.url.split('/')[-2]
        nome_arquivo = f'citacoes-{pagina}.html'
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)

        self.log(f'Arquivo salvo {nome_arquivo}')
