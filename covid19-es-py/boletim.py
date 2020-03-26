import logging
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
        # self.URLBoletins = config.read('config.ini')['feed']
        self.feedBoletins = None

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

        for linha in tabela[1:-1]:  # Exclui header (primeira linha) e total (última linha)
            dadoslinha = list(map(lambda linha: linha.text, linha.find_all("p")))
            municipio = dadoslinha[0]
            self.casos[municipio] = {
                'casosConfirmados': dadoslinha[1],
                'casosDescartados': dadoslinha[2],
                'casosSuspeitos': dadoslinha[3],
                'totalCasos': dadoslinha[4]
            }

        dadosTotalGeral = list(map(lambda linha: linha.text, linha.find_all("p")))
        self.totalGeral = {
                'casosConfirmados': dadosTotalGeral[1],
                'casosDescartados': dadosTotalGeral[2],
                'casosSuspeitos': dadosTotalGeral[3],
                'totalCasos': dadosTotalGeral[4]
        }

        self.nMunicipiosInfectados = len(tabela[1:-1])


if __name__ == "__main__":
    boletimAlvo = Boletim("https://coronavirus.es.gov.br/Not%C3%ADcia/secretaria-da-saude-divulga-25o-boletim-de-covid-19")
    boletimAlvo.carrega_casos_boletim()
    print(boletimAlvo.casos)
