from functools import total_ordering

import rows
import arrow

from utils import MUNICIPIOS, remove_caracteres_especiais


def trata_dados_linha(linha):
    linha = list(map(lambda x: x.strip(), linha))
    linha[0] = arrow.get(linha[0], 'd/m/YYYY')

    if "Ignorado" in linha[4]:
        linha[4] = None
    if "Ignorado" in linha[5]:
        linha[5] = None
    if linha[7] in ["Ignorado", "-"]:
        linha[7] = None
    if "-" in linha[8]:
        linha[8] = None

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
    def __init__(self, data=None, semanaAno=None, faixaIdade=None, sexo=None, raçaCor=None, escolaridade=None, classificacao=None, evolucao=None, criterio=None, status_notificacao=None, municipio=None, bairro=None, sintomas=None, comorbidades=None, ficouInternado=None, viagemBrasil=None, viagemInternacional=None):
        self.data = data
        self.semanaAno = semanaAno
        self.faixaIdade = faixaIdade
        self.sexo = sexo
        self.raçaCor = raçaCor
        self.escolaridade = escolaridade
        self.classificacao = classificacao
        self.evolucao = evolucao
        self.criterio = criterio
        self.statusNotificacao = status_notificacao
        self.municipio = municipio
        self.bairro = bairro
        self.sintomas = sintomas
        self.comorbidades = comorbidades
        self.ficouInternado = ficouInternado
        self.viagemBrasil = viagemBrasil
        self.viagemInternacional = viagemInternacional

    def __str__(self):
        return "{}, {}, {}".format(self.data, self.classificacao, self.municipio)

    def carrega_dados_linha(self, linha):
        linha = trata_dados_linha(linha)

        self.data = linha[0]
        self.semanaAno = linha[1]
        self.faixaIdade = linha[2]
        self.sexo = linha[3]
        self.raçaCor = linha[4]
        self.escolaridade = linha[5]
        self.classificacao = linha[6]
        self.evolucao = linha[7]
        self.criterio = linha[8]
        self.statusNotificacao = linha[9]
        self.municipio = linha[10]
        self.bairro = linha[11]
        self.sintomas = {
            "cefaleia": linha[12],
            "coriza": linha[13],
            "diarreia": linha[14],
            "dificuldadeRespiratoria": linha[15],
            "dorGarganta": linha[16],
            "febre": linha[17],
            "tosse": linha[18]
        }
        self.comorbidades = {
            "comorbidadeCardio": linha[19],
            "comorbidadeDiabetes": linha[20],
            "comorbidadePulmao": linha[21],
            "comorbidadeRenal": linha[22],
            "comorbidadeTabagismo": linha[23],
            "comorbidadeObesidade": linha[24]
        }
        self.ficouInternado = linha[25]
        self.viagemBrasil = linha[26]
        self.viagemInternacional = linha[27]


class Boletim():
    def __init__(self, caminhoCSV):
        self.csv = caminhoCSV
        self.rows = rows.import_from_csv(self.csv)
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
        for linha in self.rows:
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


boletim = Boletim("./data.csv")
boletim.popula_boletim()
print(len(boletim.filtra_data('4/15/2020')))
for key in sorted(boletim.casosMunicipios.values()):
    print(key.nome, key.casosConfirmados, key.obitos)
print(boletim.totalGeral)
