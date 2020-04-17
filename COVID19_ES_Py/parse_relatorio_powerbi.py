from functools import total_ordering

from io import BytesIO
import requests
import rows
import arrow

from utils import MUNICIPIOS, remove_caracteres_especiais

URL_RELATORIO_CSV = "https://bi.static.es.gov.br/covid19/MICRODADOS.csv"


def trata_dados_linha(linha):
    linha = list(map(lambda x: x.strip(), linha))
    linha[0] = arrow.get(linha[0], 'DD/MM/YYYY')

    if linha[2] in ["Ignorado", "-"]:
        linha[2] = None
    if "-" in linha[3]:
        linha[3] = None
    if "Não encontrado" in linha[6]:
        linha[6] = None
    if "Ignorado" in linha[9]:
        linha[9] = None
    if "Ignorado" in linha[10]:
        linha[10] = None
    if "-" in linha[11]:
        linha[11] = None

    stringParaBool = {
        "Sim": True,
        "Não": False,
        "-": None,
        "": None
    }
    for i, campo in enumerate(linha[12:]):
        linha[i + 12] = stringParaBool[linha[i + 12]]

    return linha


@total_ordering
class Municipio():
    def __init__(self, nome):
        self.nome = nome
        self.casos = []
        self.casosConfirmados = 0
        self.obitos = 0

    def __eq__(self, other):
        return (self.nome.lower() == other.nome.lower())

    def __lt__(self, other):
        return (self.nome.lower() < other.nome.lower())


class Caso():
    def __init__(self, data=None, faixaEtaria=None, sexo=None, racaCor=None, escolaridade=None, classificacao=None, evolucao=None, criterioClassificacao=None, statusNotificacao=None, municipio=None, bairro=None, sintomas=None, comorbidades=None, ficouInternado=None, viagemBrasil=None, viagemInternacional=None):
        self.data = data
        self.classificacao = classificacao
        self.evolucao = evolucao
        self.criterioClassificacao = criterioClassificacao
        self.statusNotificacao = statusNotificacao
        self.municipio = municipio
        self.bairro = bairro
        self.faixaEtaria = faixaEtaria
        self.sexo = sexo
        self.racaCor = racaCor
        self.escolaridade = escolaridade
        self.sintomas = sintomas
        self.comorbidades = comorbidades
        self.ficouInternado = ficouInternado
        self.viagemBrasil = viagemBrasil
        self.viagemInternacional = viagemInternacional

    def __str__(self):
        return f"Caso de {self.data} - {self.classificacao} em {self.municipio}"

    def carrega_dados_linha(self, linha):
        linha = trata_dados_linha(linha)

        self.data = linha[0]
        self.classificacao = linha[1]
        self.evolucao = linha[2]
        self.criterioClassificacao = linha[3]
        self.statusNotificacao = linha[4]
        self.municipio = linha[5]
        self.bairro = linha[6]
        self.faixaEtaria = linha[7]
        self.sexo = linha[8]
        self.racaCor = linha[9]
        self.escolaridade = linha[10]
        self.sintomas = {
            "cefaleia": linha[11],
            "coriza": linha[12],
            "diarreia": linha[13],
            "dificuldadeRespiratoria": linha[14],
            "dorGarganta": linha[15],
            "febre": linha[16],
            "tosse": linha[17]
        }
        self.comorbidades = {
            "comorbidadeCardio": linha[18],
            "comorbidadeDiabetes": linha[19],
            "comorbidadePulmao": linha[20],
            "comorbidadeRenal": linha[21],
            "comorbidadeTabagismo": linha[22],
            "comorbidadeObesidade": linha[23]
        }
        self.ficouInternado = linha[24]
        self.viagemBrasil = linha[25]
        self.viagemInternacional = linha[26]


class Boletim():
    def __init__(self, caminhoCSV=None):
        if caminhoCSV:
            self.csv = caminhoCSV
            self.rows = rows.import_from_csv(self.csv)
        else:
            self.csv = requests.get(URL_RELATORIO_CSV).content
            self.rows = rows.import_from_csv(BytesIO(self.csv))
        self.casosMunicipios = {}
        self.totalGeral = {
            "casosConfirmados": 0,
            "obitos": 0
        }
        self.nMunicipiosInfectados = 0

    def filtra_data(self, data):
        filtrado = []

        for caso in self.rows[1:]:
            if data in caso[0] and "Confirmados" in caso[6]:
                casoObj = Caso()
                casoObj.carrega_dados_linha(caso)
                filtrado.append(casoObj)

        return filtrado

    def popula_boletim(self):
        for linha in self.rows[1:]:
            caso = Caso()
            caso.carrega_dados_linha(linha)
            if remove_caracteres_especiais(caso.municipio.upper()) in MUNICIPIOS:
                if caso.classificacao == "Confirmados":
                    self.totalGeral['casosConfirmados'] += 1
                    try:
                        if (caso.evolucao == "Óbito pelo COVID-19"):
                            self.totalGeral['obitos'] += 1
                            self.casosMunicipios[caso.municipio].obitos += 1
                        self.casosMunicipios[caso.municipio].casos.append(caso)
                        self.casosMunicipios[caso.municipio].casosConfirmados += 1
                    except KeyError:
                        self.casosMunicipios[caso.municipio] = Municipio(
                            caso.municipio)
                        if (caso.evolucao == "Óbito pelo COVID-19"):
                            self.casosMunicipios[caso.municipio].obitos += 1
                        self.casosMunicipios[caso.municipio].casos.append(caso)
                        self.casosMunicipios[caso.municipio].casosConfirmados += 1
                        self.nMunicipiosInfectados += 1

    def __str__(self):
        return "Boletim do arquivo '{}'\nTotal geral: {}\n{} municípios infectados.".format(self.csv, self.totalGeral, self.nMunicipiosInfectados)


boletim = Boletim()
boletim.popula_boletim()
# print(len(boletim.filtra_data('4/15/2020')))
for key in sorted(boletim.casosMunicipios.values()):
    print(key.nome, key.casosConfirmados, key.obitos)
print(boletim.totalGeral)