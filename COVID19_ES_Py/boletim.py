import re
import logging
import unicodedata
import requests
import configparser
from bs4 import BeautifulSoup
from .utils import remove_acentos
from .exceptions import BoletimError

config = configparser.ConfigParser()
config.read('./config.ini')

# Produz registros
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    filename='scraperboletim.log',
                    level=logging.DEBUG)
mainLogger = logging.getLogger(__name__)
mainLogger.setLevel(logging.DEBUG)


class ScraperBoletim():
    """
    Um objeto ScraperBoletim é capaz de varrer o feed de boletins em busca de suas URLs.

    Attributes
    ----------
    URLFeedBoletins : string
        A URL do feed de boletins.
    URLsBoletins : list : string
        Uma lista com URLs dos boletins.
    """
    def __init__(self, ):
        self.URLFeedBoletins = config['url']['DOMINIO_FEED']
        self.URLsBoletins = None

    def carrega_html_feed(self, URLPagina):
        """Carrega o HTML de uma página do feed de boletins.

        Parameters
        ----------
        URLPagina : string
            Página do feed a ser varrido.

        Returns
        ----------
        html : objeto BS4
            O objeto BS4 do HTML lido ou None se houver falha na requisição."""

        if URLPagina:
            req = requests.get(URLPagina)
        else:
            req = requests.get(self.URLFeedBoletins)
        if req.status_code == 200:
            mainLogger.info(f"Requisição bem sucedida para {req.url}")
            # Pega conteúdo (HTML) da requisição
            content = req.content
            html = BeautifulSoup(content, 'html.parser')
            return html
        else:
            mainLogger.error(f"Requisição falhou para {req.url}")

    def extrai_boletins_pagina(self, URLPagina):
        """Extrai as URLs dos boletins presentes em uma página do feed de boletins.

        Parameters
        ----------
        URLPagina : string
            Página do feed a ser varrido.

        Returns
        ----------
        linksBoletins : list : string
            Lista com URLs dos boletins da página do feed ou None se houver falha na requisição."""

        try:
            html = self.carrega_html_feed(URLPagina)
            articleNoticias = html.find_all(
                'article', class_='noticia list-content-item content-item')
            linksBoletins = list(map(lambda article: article.find_all('a')[0]['href'], articleNoticias))
            return linksBoletins
        except AttributeError:
            return None

    def extrai_todos_boletins(self):
        """Extrai as URLs de todos os boletins publicados até o momento.

        Returns
        ----------
        todosBoletins : list : string
            Lista com URLs de todos os boletins publicados até o momento."""

        todosBoletins = []
        i = 0
        while(True):
            boletinsPagina = self.extrai_boletins_pagina(
                f"https://coronavirus.es.gov.br/Noticias?page={i}")
            if boletinsPagina:
                todosBoletins.extend(self.extrai_boletins_pagina(f"https://coronavirus.es.gov.br/Noticias?page={i}"))
                i += 1
            else:
                break
        self.URLsBoletins = todosBoletins
        return todosBoletins

    def url_ultimo_boletim(self):
        """Busca URL do último boletim e retorna-a.

        Returns
        ----------
        url : string
            URL do último boletim ou None se busca falhar."""

        html = self.carrega_html_feed(self.URLFeedBoletins)
        try:
            articleNoticia = html.find('article', class_='noticia list-content-item content-item')
            ultimaNoticia = articleNoticia.find('a')['href']
            return config['url']['DOMINIO_BOLETINS'] + ultimaNoticia
        except AttributeError:
            return None

    def carrega_ultimo_boletim(self):
        """Busca a URL do último boletim e instancia objeto Boletim com esta.

        Returns
        ----------
        boletim : Boletim
            Objeto Boletim carregado com a URL do último boletim emitido."""

        urlBoletim = self.url_ultimo_boletim()
        return Boletim(urlBoletim)


class Boletim():
    """
    Um objeto Boletim é capaz de extrair números de casos de um boletim.

    Parameters
    ----------
    URLBoletim : string
        A URL do boletim a ser processado.

    Attributes
    ----------
    url : string
        A URL do boletim.
    n : string
        O número do boletim.
    html : BeautifulSoup4
        O HTML lido como objeto BS4.
    casos : dict
        O dicionário de casos registrados nos municípios do ES.
    totalGeral : dict
        O dicionário do total de casos registrados no ES.
    nMunicipiosInfectados : int
        O número de municípios infectados.
    """

    def __init__(self, URLBoletim):
        self.url = URLBoletim
        self.n = self.extrai_numero_boletim()
        self.html = self.carrega_html_boletim()
        self.casos = {}
        self.totalGeral = {}
        self.nMunicipiosInfectados = 0
        self.carrega_casos_boletim()

    def __str__(self):
        return f"Boletim nº {self.n}.\nURL: {self.url}\n{self.nMunicipiosInfectados} municípios com possíveis casos.\nTotal ES: {self.totalGeral}"

    def extrai_numero_boletim(self):
        """Extrai o número do boletim."""

        buscaPadrao = re.search(r'(\d+)o', self.url)
        if buscaPadrao:
            return buscaPadrao.group(1)

    def carrega_html_boletim(self):
        """Faz requisição para o boletim e retorna seu HTML como objeto BS4."""

        req = requests.get(self.url)
        if req.status_code == 200:
            mainLogger.info(f'Requisição bem sucedida para {self.url}!')
            # Pega conteúdo (HTML) da requisição
            content = req.content
            html = BeautifulSoup(content, 'html.parser')
            return html
        else:
            mainLogger.error(f'Requisição falhou para {self.url}.')

    def carrega_tabela_boletim(self):
        """Seleciona a tabela do boletim com número de casos no Estado."""

        return self.html.find(class_="clearfix body-part").find_all("tr")

    def carrega_casos_boletim(self):
        """Carrega tabela do boletim e extrai número de casos.
        Preenche nMunicipiosInfectados e os dicionários casos e totalGeral."""

        tabela = self.carrega_tabela_boletim()

        # Exclui header (primeira linha) e total (última linha)
        for linha in tabela[1:-1]:
            dadoslinha = list(
                map(lambda linha: linha.text, linha.find_all("p")))
            municipio = dadoslinha[0]

            self.casos[municipio] = {
                'casosConfirmados': unicodedata.normalize("NFKD", dadoslinha[1]).replace(' ', '0'),
                'casosDescartados': unicodedata.normalize("NFKD", dadoslinha[2]).replace(' ', '0'),
                'casosSuspeitos': unicodedata.normalize("NFKD", dadoslinha[3]).replace(' ', '0'),
                'totalCasos': unicodedata.normalize("NFKD", dadoslinha[4]).replace(' ', '0')
            }

        dadosTotalGeral = list(map(lambda linha: unicodedata.normalize(
            "NFKD", linha.text), tabela[-1].find_all("p")))
        self.totalGeral = {
            'casosConfirmados': unicodedata.normalize("NFKD", dadosTotalGeral[1]),
            'casosDescartados': unicodedata.normalize("NFKD", dadosTotalGeral[2]),
            'casosSuspeitos': unicodedata.normalize("NFKD", dadosTotalGeral[3]),
            'totalCasos': unicodedata.normalize("NFKD", dadosTotalGeral[4])
        }

        self.nMunicipiosInfectados = len(tabela[1:-1])

    def pesquisa_casos_municipio(self, municipio):
        """Realiza pesquisa no boletim por casos registrados em um município.

        Parameters
        ----------
        municipio : string
            O município a ser pesquisado.

        Returns
        ----------
        self.casos[municipio] : dict
            O dicionário de casos registrados no município, BoletimError se não for encontrado."""

        stringMunicipioTratada = remove_acentos(municipio).lower().strip()
        stringsMunicipiosTratadas = list(
            map(lambda string: remove_acentos(string).lower().strip(), self.casos.keys()))
        try:
            indiceMunicipio = stringsMunicipiosTratadas.index(
                stringMunicipioTratada)
        except ValueError:  # O município não foi encontrado
            mainLogger.error(f"Município {municipio} não encontrado no boletim.")
            raise BoletimError(f"O município \"{stringMunicipioTratada}\" não foi encontrado no boletim. Pode ter ocorrido um erro de digitação ou o município não registrou casos de COVID-19.")
        else:
            municipio = list(self.casos.keys())[indiceMunicipio]
            return self.casos[municipio]


if __name__ == '__main__':
    # Exemplos de uso

    # Inicializando o scraper
    scraper = ScraperBoletim()

    # Carregando objeto Boletim com último boletim emitido
    boletim = scraper.carrega_ultimo_boletim()
    print(boletim.casos)
    print(boletim.nMunicipiosInfectados)
