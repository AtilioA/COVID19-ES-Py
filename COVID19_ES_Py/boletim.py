"""O módulo `boletim.py` é o principal do pacote.
Nele são introduzidas as classes e métodos utilizados para coletar dados dos boletins emitidos pelo Governo.

"""

import re
from urllib.parse import urljoin
import logging
import unicodedata
import requests
import arrow
from bs4 import BeautifulSoup
from .utils import trata_entradas_tabela, remove_caracteres_especiais, MUNICIPIOS
from .exceptions import BoletimError

DOMINIO_FEED = "https://coronavirus.es.gov.br/Noticias"
DOMINIO_BOLETINS = "https://coronavirus.es.gov.br/"

# Produz registros
logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    filename="scraperboletim.log",
    level=logging.DEBUG,
)
mainLogger = logging.getLogger(__name__)
mainLogger.setLevel(logging.DEBUG)


class ScraperBoletim:
    """
    Um objeto `ScraperBoletim` é capaz de varrer o feed de boletins em busca de suas URLs.

    Attributes
    ----------
    URLFeedBoletins : ``str``
        A URL do feed de boletins.
    URLsBoletins : ``list`` : ``str``
        Uma lista com URLs dos boletins (preenchida caso o método `extrai_todos_boletins` seja chamado).
    """

    def __init__(self,):
        self.URLFeedBoletins = DOMINIO_FEED
        self.URLsBoletins = None

    def carrega_html_feed(self, URLPagina):
        """Carrega o HTML de uma página do feed de boletins.

        Parameters
        ----------
        URLPagina : ``str``
            Página do feed a ser varrido.

        Returns
        ----------
        html : `BeautifulSoup` ou ``None``
            O objeto BeautifulSoup do HTML lido ou ``None`` se houver falha na requisição."""

        if URLPagina:
            req = requests.get(URLPagina)
        elif self.URLFeedBoletins:  # pragma: no cover
            req = requests.get(self.URLFeedBoletins)
        else:
            req = requests.get(
                "https://coronavirus.es.gov.br/Noticias")  # pragma: no cover
        if req.status_code == 200:
            mainLogger.info(f"Requisição bem sucedida para {req.url}")
            # Pega conteúdo (HTML) da requisição
            content = req.content
            html = BeautifulSoup(content, "html.parser")
            return html
        else:
            mainLogger.error(  # pragma: no cover
                f"Requisição falhou para {req.url}")

    def extrai_boletins_pagina(self, URLPagina=None, html=None):
        """Extrai as URLs dos boletins presentes em uma página do feed de boletins.

        Parameters
        ----------
        URLPagina : ``str``
            Página do feed a ser varrido.

        Returns
        ----------
        linksBoletins : ``list`` : ``str`` ou None
            Lista com URLs dos boletins da página do feed ou None se houver falha na requisição."""

        try:
            if not html:
                html = self.carrega_html_feed(URLPagina)
            articleNoticias = html.find_all(
                "article", class_="noticia list-content-item content-item"
            )
            linksBoletins = list(
                map(lambda article: article.find_all(
                    "a")[0]["href"], articleNoticias)
            )
            return linksBoletins
        except (AttributeError, TypeError) as err:
            raise BoletimError(
                f"Não foi possível extrair boletins da página de URL {URLPagina} ou do HTML {html}: {err}")
        except requests.exceptions.MissingSchema as err:  # pragma: no cover
            mainLogger.error(f"URL mal formada: {err}")
            raise err

    def extrai_todos_boletins(self):
        """Extrai as URLs de todos os boletins publicados até o momento.

        Returns
        ----------
        todosBoletins : ``list`` : ``str``
            Lista com URLs de todos os boletins publicados até o momento."""

        todosBoletins = []
        i = 1
        while True:
            boletinsPagina = self.extrai_boletins_pagina(
                f"https://coronavirus.es.gov.br/Noticias?page={i}"
            )
            if boletinsPagina:
                todosBoletins.extend(
                    self.extrai_boletins_pagina(
                        f"https://coronavirus.es.gov.br/Noticias?page={i}"
                    )
                )
                i += 1
            else:
                break
        self.URLsBoletins = todosBoletins
        return todosBoletins

    def url_ultimo_boletim(self, html=None):
        """Busca URL do último boletim e retorna-a.

        Returns
        ----------
        url : ``string`` ou ``None``
            URL do último boletim ou ``None`` se busca falhar."""

        if not html:
            html = self.carrega_html_feed(self.URLFeedBoletins)
        try:
            articleNoticia = html.find(
                "article", class_="noticia list-content-item content-item"
            )
            ultimaNoticia = articleNoticia.find("a")["href"]
            return urljoin(DOMINIO_BOLETINS, ultimaNoticia)
        except (TypeError, AttributeError) as err:
            mainLogger.error(f"Não foi possível ler o HTML: {err}")
            raise err

    def carrega_ultimo_boletim(self):
        """Busca a URL do último boletim e instancia objeto Boletim com esta.

        Returns
        ----------
        boletim : `Boletim`
            Objeto `Boletim` carregado com a URL do último boletim emitido."""

        urlBoletim = self.url_ultimo_boletim()
        return Boletim(urlBoletim)

    def pesquisa_boletim_data(self, data):
        """Realiza pesquisa de boletim por data de publicação.

        Parameters
        ----------
        data : ``str``
            A data de publicação do boletim a ser pesquisado.
            Formatos de data aceitos:
            "DD/MM/YYYY", "DD-MM-YYYY", "DD_MM_YYYY", "DD.MM.YYYY", "DDMMYYYY".

        Returns
        ----------
        Boletim : ``dict`` ou ``None``
            O boletim publicado na data especificada ou ``None`` se não houver."""

        dataArrow = arrow.get(
            data, ["DD/MM/YYYY", "DD-MM-YYYY",
                   "DD_MM_YYYY", "DD.MM.YYYY", "DDMMYYYY"]
        )
        dataAgora = arrow.get(
            arrow.now("America/Sao_Paulo").format("DD-MM-YYYY"), "DD-MM-YYYY"
        )

        if dataAgora >= dataArrow >= arrow.get("19/03/2020", "DD/MM/YYYY"):
            i = 1
            while True:
                req = requests.get(
                    f"https://coronavirus.es.gov.br/Noticias?page={i}")
                content = req.content
                html = BeautifulSoup(content, "html.parser")
                if req.status_code == 200:  # pragma: no cover
                    noticias = html.find_all(
                        "article", class_="noticia")

                    patternDatas = r"(\d{1,2}\/\d{1,2}\/\d{4})"
                    for noticia in noticias:
                        linkBoletim = noticia.find(
                            "h4", class_="title-list").find("a")["href"]

                        dataBoletim = noticia.find(
                            "div", class_="published").text
                        matchData = re.search(patternDatas, dataBoletim)
                        if matchData:
                            dataBoletim = arrow.get(
                                matchData.group(0), "DD/MM/YYYY")
                            if dataBoletim == dataArrow:
                                return Boletim(urljoin(DOMINIO_BOLETINS, linkBoletim))
                else:
                    mainLogger.error(  # pragma: no cover
                        f"Requisição falhou para {req.url}")
                i += 1
        return None


class Boletim:
    """
    Um objeto `Boletim` é capaz de extrair números de casos de um boletim.

    Parameters
    ----------
    URLBoletim : ``str``
        A URL do boletim a ser processado.

    Attributes
    ----------
    url : ``str``
        A URL do boletim.
    n : ``int``
        O número do boletim.
    titulo : ``str``
        Título do boletim.
    dataPublicacao : objeto ``Arrow``
        Objeto ``Arrow`` com a data de publicação do boletim.
    dataAtualizacao : objeto ``Arrow``
        Objeto ``Arrow`` com a data de atualização do boletim, se houver.
    corpo : ``str``
        Corpo de texto do boletim.
    html : `BeautifulSoup`
        O HTML lido como objeto BeautifulSoup.
    casos : ``dict``
        O dicionário de casos registrados nos municípios do ES.
    totalGeral : ``dict``
        O dicionário do total de casos registrados no ES.
    nMunicipiosComCasos : ``int``
        O número de municípios com algum caso, confirmado ou não.
    nMunicipiosInfectados : ``int``
        O número de municípios com algum caso confirmado.
    """

    def __init__(self, URLBoletim):
        self.url = URLBoletim
        self.n = self.extrai_numero_boletim()
        self.html = self.carrega_html_boletim()
        self.titulo = self.extrai_titulo_boletim()
        datas = self.extrai_datas_boletim()
        self.dataPublicacao = datas[0]
        self.dataAtualizacao = datas[1]
        self.corpo = self.extrai_corpo_boletim()
        self.casos = {}
        self.totalGeral = {}
        self.carrega_casos_boletim()
        self.nMunicipiosComCasos = self.conta_municipios_com_casos()
        self.nMunicipiosInfectados = self.conta_municipios_infectados()

    def __str__(self):
        return f"Boletim nº {self.n} - { self.pega_dataPublicacao_formatada()}.\nURL: {self.url}\n{self.nMunicipiosInfectados} municípios com casos confirmados.\nTotal ES: {self.totalGeral}"  # pragma: no cover

    def pega_dataPublicacao_formatada(self):
        """Formata o objeto Arrow com data de publicação para o formato usual dos boletins."""

        try:
            if self.dataPublicacao:
                return self.dataPublicacao.format("DD/MM/YYYY HH[h]mm")
        except AttributeError as err:
            mainLogger.error(f"Data {self.dataPublicacao} malformada: {err}")
            raise err

    def pega_dataAtualizacao_formatada(self):
        """Formata o objeto Arrow com data de atualização para o formato usual dos boletins."""

        try:
            if self.dataAtualizacao:
                return self.dataAtualizacao.format("DD/MM/YYYY HH[h]mm")
        except AttributeError as err:
            mainLogger.error(f"Data {self.dataAtualizacao} malformada: {err}")
            raise err

    def extrai_numero_boletim(self):
        """Extrai o número do boletim pela URL."""

        buscaPadrao = re.search(r"(\d+)o", self.url)
        if buscaPadrao:
            return int(buscaPadrao.group(1))

    def extrai_titulo_boletim(self):
        """Extrai título do HTML do boletim."""

        tituloBoletim = self.html.find("h2", class_="title-content")
        return tituloBoletim.text

    def extrai_datas_boletim(self):
        """Extrai as datas de publicação e atualização (esta se existir) do HTML do boletim."""

        datasBoletim = self.html.find("div", class_="published").text

        patternDatas = r"(\d{1,2}\/\d{1,2}\/\d{4}\s*\w+h\w*)"
        matchData = re.findall(patternDatas, datasBoletim)

        formatoData = "DD/MM/YYYY H[h]m"
        dataPublicacao = arrow.get(matchData[0], formatoData)

        try:
            dataAtualizacao = arrow.get(matchData[1], formatoData)
        except IndexError:
            dataAtualizacao = None

        return (dataPublicacao, dataAtualizacao)

    def extrai_corpo_boletim(self):
        """Extrai o corpo de texto do HTML do boletim."""

        corpo = self.html.find("div", class_="clearfix body-part")

        stringCorpo = ""
        for p in corpo.find_all("p"):
            if "13.709/2018" not in p.text:
                stringCorpo = f"{stringCorpo}\n{p.text}"
            else:
                break

        return stringCorpo

    def carrega_html_boletim(self):
        """Faz requisição para o boletim e retorna seu HTML como objeto `BeautifulSoup`."""

        req = requests.get(self.url)
        if req.status_code == 200:
            mainLogger.info(
                f"Requisição bem sucedida para {self.url}!")
            # Pega conteúdo (HTML) da requisição
            content = req.content
            html = BeautifulSoup(content, "html.parser")
            return html
        else:
            mainLogger.error(
                f"Requisição falhou para {self.url}.")

    def carrega_tabela_boletim(self):
        """Seleciona a tabela do boletim com número de casos no Estado."""

        return self.html.find(class_="clearfix body-part").find_all("tr")

    def carrega_casos_19_03(self):
        """Extrai número de casos das tabelas dos boletins tipo 1 (19/03/2020)."""

        tabela = self.carrega_tabela_boletim()

        regioes = ["Central", "Metropolitana", "Norte", "Sul"]
        # Exclui header (primeira linha) e total (última linha)
        for linha in tabela[1:-1]:
            dadosLinha = [
                elemento for elemento in list(
                    map(lambda linha: linha.text.strip(), linha.find_all("p"))
                )
                if elemento not in regioes
            ]
            dadosLinha = trata_entradas_tabela(dadosLinha)
            municipio = dadosLinha[0]

            self.casos[municipio] = {
                "casosConfirmados": unicodedata.normalize(
                    "NFKD", dadosLinha[4]
                ).replace(" ", "0"),
                "casosDescartados": unicodedata.normalize(
                    "NFKD", dadosLinha[3]
                ).replace(" ", "0"),
                "casosSuspeitos": unicodedata.normalize(
                    "NFKD", dadosLinha[2]
                ).replace(" ", "0"),
                "totalCasos": unicodedata.normalize("NFKD", dadosLinha[1]).replace(
                    " ", "0"
                ),
            }

        dadosTotalGeral = list(
            map(
                lambda linha: unicodedata.normalize("NFKD", linha.text),
                tabela[-1].find_all("p"),
            )
        )
        self.totalGeral = {
            "casosConfirmados": unicodedata.normalize("NFKD", dadosTotalGeral[4]),
            "casosDescartados": unicodedata.normalize("NFKD", dadosTotalGeral[3]),
            "casosSuspeitos": unicodedata.normalize("NFKD", dadosTotalGeral[2]),
            "totalCasos": unicodedata.normalize("NFKD", dadosTotalGeral[1]),
        }

    def carrega_casos_22_03(self):
        """Extrai número de casos da tabela do boletim tipo 2 (22/03/2020)."""

        tabela = self.carrega_tabela_boletim()

        # Exclui header (primeira linha) e total (última linha)
        for linha in tabela[2:-2]:
            dadosLinha = trata_entradas_tabela(
                map(lambda linha: linha.text.strip(), linha.find_all("td")))

            try:
                if dadosLinha[1].isdigit() and dadosLinha[0] != "Total":
                    municipio = dadosLinha[0]
                    self.casos[municipio] = {
                        "casosConfirmados": unicodedata.normalize(
                            "NFKD", dadosLinha[1]
                        ).replace(" ", "0"),
                        "casosDescartados": unicodedata.normalize(
                            "NFKD", dadosLinha[2]
                        ).replace(" ", "0"),
                        "casosSuspeitos": unicodedata.normalize(
                            "NFKD", dadosLinha[3]
                        ).replace(" ", "0"),
                        "totalCasos": unicodedata.normalize("NFKD", dadosLinha[4]).replace(
                            " ", "0"
                        ),
                    }
            except IndexError:
                pass

        dadosTotalGeral = list(
            map(
                lambda linha: unicodedata.normalize(
                    "NFKD", linha.text.strip()),
                tabela[-2].find_all("td"),
            )
        )
        self.totalGeral = {
            "casosConfirmados": unicodedata.normalize("NFKD", dadosTotalGeral[1]),
            "casosDescartados": unicodedata.normalize("NFKD", dadosTotalGeral[2]),
            "casosSuspeitos": unicodedata.normalize("NFKD", dadosTotalGeral[3]),
            "totalCasos": unicodedata.normalize("NFKD", dadosTotalGeral[4]),
        }

    def carrega_casos_23_03(self):
        """Extrai número de casos das tabelas dos boletins tipo 3 (23/03/2020)."""

        tabela = self.carrega_tabela_boletim()

        # Exclui header (primeira linha) e total (última linha)
        for linha in tabela[1:-1]:
            dadosLinha = trata_entradas_tabela(
                map(lambda linha: linha.text.strip(), linha.find_all("p")))
            municipio = dadosLinha[0]

            self.casos[municipio] = {
                "casosConfirmados": dadosLinha[1],
                "casosDescartados": dadosLinha[2],
                "casosSuspeitos": dadosLinha[3],
                "totalCasos": dadosLinha[4],
            }

        dadosTotalGeral = list(
            map(
                lambda linha: linha.text,
                tabela[-1].find_all("p"),
            )
        )
        self.totalGeral = {
            "casosConfirmados": dadosTotalGeral[1],
            "casosDescartados": dadosTotalGeral[2],
            "casosSuspeitos": dadosTotalGeral[3],
            "totalCasos": dadosTotalGeral[4],
        }

    def carrega_casos_04_04(self):
        """Extrai número de casos das tabelas dos boletins tipo 4 (04/04/2020)."""

        tabela = self.carrega_tabela_boletim()

        # Exclui header (primeira linha) e total (última linha)
        for linha in tabela[1:-1]:
            dadosLinha = trata_entradas_tabela(
                map(lambda linha: linha.text.strip(), linha.find_all("td")))
            municipio = dadosLinha[0]

            self.casos[municipio] = {
                "casosConfirmados": unicodedata.normalize(
                    "NFKD", dadosLinha[1]
                ).replace(" ", "0"),
                "casosDescartados": unicodedata.normalize(
                    "NFKD", dadosLinha[2]
                ).replace(" ", "0"),
                "casosSuspeitos": unicodedata.normalize(
                    "NFKD", dadosLinha[3]
                ).replace(" ", "0"),
                "totalCasos": unicodedata.normalize("NFKD", dadosLinha[4]).replace(" ", "0"),
                "obitos": unicodedata.normalize(
                    "NFKD", dadosLinha[5]
                ).replace(" ", "0")
            }

        dadosTotalGeral = list(
            map(
                lambda linha: unicodedata.normalize(
                    "NFKD", linha.text.strip()),
                tabela[-1].find_all("td"),
            )
        )
        self.totalGeral = {
            "casosConfirmados": unicodedata.normalize("NFKD", dadosTotalGeral[1]),
            "casosDescartados": unicodedata.normalize("NFKD", dadosTotalGeral[2]),
            "casosSuspeitos": unicodedata.normalize("NFKD", dadosTotalGeral[3]),
            "totalCasos": unicodedata.normalize("NFKD", dadosTotalGeral[4]),
            "totalObitos": unicodedata.normalize("NFKD", dadosTotalGeral[5]),
        }

    def carrega_casos_boletim(self):
        """Carrega tabela do boletim e extrai número de casos.
        Preenche os dicionários `casos` e `totalGeral`."""

        if 21 <= self.n < 24:
            self.carrega_casos_19_03()

        elif self.n == 24:
            self.carrega_casos_22_03()

        elif 24 < self.n < 37:
            self.carrega_casos_23_03()

        elif self.n >= 37:
            self.carrega_casos_04_04()

        else:
            mainLogger.error(
                f"O boletim de nº {self.n} (n < 21, anterior a 19/03/2020) não é suportado."
            )
            raise BoletimError(
                f"O boletim de nº {self.n} (n < 21, anterior a 19/03/2020) não é suportado."
            )

    def conta_municipios_com_casos(self):
        """Retorna o número de municípios com algum caso registrado, confirmado ou não."""

        municipiosComCasos = 0
        linhasTabela = self.casos.keys()

        for elemento in linhasTabela:
            if remove_caracteres_especiais(elemento).upper() in MUNICIPIOS:
                municipiosComCasos += 1

        return municipiosComCasos

    def conta_municipios_infectados(self):
        """Retorna o número de municípios com algum caso confirmado."""

        municipiosInfectados = 0
        linhasTabela = self.casos.keys()

        for elemento in linhasTabela:
            elementoTratado = remove_caracteres_especiais(elemento).upper()
            if (
                elementoTratado in MUNICIPIOS
                and int(self.casos[elemento]["casosConfirmados"]) > 0
            ):
                municipiosInfectados += 1

        return municipiosInfectados

    def pesquisa_casos_municipio(self, municipio):
        """Realiza pesquisa no boletim por casos registrados em um município.

        Parameters
        ----------
        municipio : ``str``
            O município a ser pesquisado.

        Raises
        ----------
        `BoletimError`
            Se o município não for encontrado na lista de casos.

        Returns
        ----------
        self.casos[municipio] : ``dict``
            O dicionário de casos registrados no município."""

        stringMunicipioTratada = remove_caracteres_especiais(
            municipio).lower().strip()
        stringsMunicipiosTratadas = list(
            map(
                lambda string: remove_caracteres_especiais(
                    string).lower().strip(),
                self.casos.keys(),
            )
        )
        try:
            indiceMunicipio = stringsMunicipiosTratadas.index(
                stringMunicipioTratada)
        except ValueError:  # O município não foi encontrado
            mainLogger.error(
                f"Município {municipio} não encontrado no boletim.")
            raise BoletimError(
                f'O município "{stringMunicipioTratada}" não foi encontrado no boletim. Pode ter ocorrido um erro de digitação ou o município não registrou casos de COVID-19.'
            )
        else:
            municipio = list(self.casos.keys())[indiceMunicipio]
            return self.casos[municipio]

    def filtra_municipios_com_casos_confirmados(self):
        """Filtra o dicionário de casos por municípios com casos confirmados.

        Returns
        ----------
        municipiosComCasosConfirmados : ``dict``
            O dicionário de municípios com casos confirmados no estado."""

        municipiosComCasosConfirmados = {
            municipio: self.casos[municipio]
            for (municipio, casos) in self.casos.items()
            if int(self.casos[municipio]["casosConfirmados"]) > 0
            and remove_caracteres_especiais(municipio).upper() in MUNICIPIOS
        }

        return municipiosComCasosConfirmados
