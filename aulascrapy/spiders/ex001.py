from scrapy import Selector
from urllib.request import urlopen

# html = urlopen('https://www.pythonparatodos.com.br/formulario.html')
# sel = Selector(text=html.read())

# lista = sel.xpath('//input[@type="text"]')
# nova_lista = lista.extract()
# for x in nova_lista:
#     print(x)
# print(lista.extract_first())

# lista = sel.xpath('//input')
# quarto_input = lista[3]
# print(quarto_input.extract())

# lista = sel.css('html > body > form > table > tr')
# lista = lista.extract()
# for x in lista:
#     print(x)

# lista = sel.css('tr:nth-of-type(2)')
# nova_lista = lista.extract()
# for x in nova_lista:
#     print(x)

# exemplo 4
# código html puro
html = """
    <html>
        <head>
            <title>Aula Python Web Scraping</title>
        </head>
        <body>
            <h1>Curso Python Web Scraping</h1>

            <form action="formulario_pythonwebscraping1.php" method="POST">
                Informe os dados abaixo:<br><br>
                <table>
                    <tr>
                        <td>Nome:</td>
                        <td><input class="teste" type="text" name="nome" size="50" maxlength="100"></input></td>
                    </tr>
                    <tr>
                        <td>E-mail:</td>
                        <td><input type="text" name="email" size="50" maxlength="100"></input></td>
                    </tr>
                    <tr>
                        <td>Celular:</td>
                        <td><input id="celular" type="text" name="celular" size="20" maxlength="14"></input></td>
                    </tr>
                    <tr>
                        <td><input id="enviar" type="submit" name="enviar" value="Enviar dados"></td>
                    </tr>
                </table>
            </form>
        </body>
    </html>
"""
sel = Selector(text=html)
# lista = sel.css('input.teste')
# lista = sel.css('input::attr(id)')
lista = sel.css('input::attr(class)')
for x in lista:
    print(x.extract())