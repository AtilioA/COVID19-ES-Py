import logging
import unicodedata
import requests
import configparser
from bs4 import BeautifulSoup
config = configparser.ConfigParser()

# Produz registros
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    filename='scraperboletim.log',
                    level=logging.DEBUG)
mainLogger = logging.getLogger(__name__)
mainLogger.setLevel(logging.DEBUG)


class ScraperBoletim():
    def __init__(self, ):
        self.URLFeedBoletins = "https://coronavirus.es.gov.br/Noticias"
        # self.html = self.carrega_html_feed(self.URLFeedBoletins)
        self.URLsBoletins = None

    def carrega_html_feed(self, URLPagina):
        if URLPagina:
            req = requests.get(URLPagina)
        else:
            req = requests.get(self.URLFeedBoletins)
        if req.status_code == 200:
            mainLogger.info(f'Requisição bem sucedida para {req.url}')
            # Retrieve the HTML content
            content = req.content
            html = BeautifulSoup(content, 'html.parser')
            return html
        else:
            mainLogger.error(f'Requisição falhou para {req.url}')

    def extrai_boletins_pagina(self, URLPagina):
        try:
            html = self.carrega_html_feed(URLPagina)
            articleNoticias = html.find_all(
                "article", class_="noticia list-content-item content-item")
            linksArticle = list(map(lambda article: article.find_all("a")[
                                0]['href'], articleNoticias))
            return linksArticle
        except AttributeError:
            return None

    def extrai_todos_boletins(self):
        todosBoletins = []
        i = 0
        while(True):
            boletinsPagina = self.extrai_boletins_pagina(
                f"https://coronavirus.es.gov.br/Noticias?page={i}")
            if boletinsPagina:
                todosBoletins.extend(self.extrai_boletins_pagina(
                    f"https://coronavirus.es.gov.br/Noticias?page={i}"))
                i += 1
            else:
                break
        self.URLsBoletins = todosBoletins
        return todosBoletins


class Boletim():
    def __init__(self, URLBoletim):
        self.url = URLBoletim
        self.html = self.carrega_html_boletim()
        self.casos = {}
        self.totalGeral = {}
        self.nMunicipiosInfectados = 0
        self.carrega_casos_boletim()

    def carrega_html_boletim(self):
        req = requests.get(self.url)
        if req.status_code == 200:
            mainLogger.info(f'Requisição bem sucedida para {self.url}!')
            # Retrieve the HTML content
            content = req.content
            html = BeautifulSoup(content, 'html.parser')
            return html
        else:
            mainLogger.error(f'Requisição falhou para {self.url}.')

    def carrega_tabela_boletim(self):
        return self.html.find(class_="clearfix body-part").find_all("tr")

    def carrega_casos_boletim(self):
        tabela = self.carrega_tabela_boletim()

        # Exclui header (primeira linha) e total (última linha)
        for linha in tabela[1:-1]:
            dadoslinha = list(
                map(lambda linha: linha.text, linha.find_all("p")))
            municipio = dadoslinha[0]
            self.casos[municipio] = {
                'casosConfirmados': dadoslinha[1],
                'casosDescartados': dadoslinha[2],
                'casosSuspeitos': dadoslinha[3],
                'totalCasos': dadoslinha[4]
            }

        dadosTotalGeral = list(map(lambda linha: unicodedata.normalize(
            "NFKD", linha.text), tabela[-1].find_all("p")))
        self.totalGeral = {
            'casosConfirmados': dadosTotalGeral[1],
            'casosDescartados': dadosTotalGeral[2],
            'casosSuspeitos': dadosTotalGeral[3],
            'totalCasos': dadosTotalGeral[4]
        }

        self.nMunicipiosInfectados = len(tabela[1:-1])


if __name__ == "__main__":
    scraper = ScraperBoletim()
    print(scraper.extrai_todos_boletins())
