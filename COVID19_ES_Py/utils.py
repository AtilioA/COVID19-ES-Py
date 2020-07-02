"""O módulo `utils.py` contém funções e constantes auxiliares."""

import unicodedata
import re
import arrow


MUNICIPIOS = [
    'AFONSO CLAUDIO',
    'AGUIA BRANCA',
    'AGUA DOCE DO NORTE',
    'ALEGRE',
    'ALFREDO CHAVES',
    'ALTO RIO NOVO',
    'ANCHIETA',
    'APIACA',
    'ARACRUZ',
    'ATILIO VIVACQUA',
    'BAIXO GUANDU',
    'BARRA DE SAO FRANCISCO',
    'BOA ESPERANCA',
    'BOM JESUS DO NORTE',
    'BREJETUBA',
    'CACHOEIRO DE ITAPEMIRIM',
    'CARIACICA',
    'CASTELO',
    'COLATINA',
    'CONCEICAO DA BARRA',
    'CONCEICAO DO CASTELO',
    'DIVINO DE SAO LOURENCO',
    'DOMINGOS MARTINS',
    'DORES DO RIO PRETO',
    'ECOPORANGA',
    'FUNDAO',
    'GOVERNADOR LINDENBERG',
    'GUACUI',
    'GUARAPARI',
    'IBATIBA',
    'IBIRACU',
    'IBITIRAMA',
    'ICONHA',
    'IRUPI',
    'ITAGUACU',
    'ITAPEMIRIM',
    'ITARANA',
    'IUNA',
    'JAGUARE',
    'JERONIMO MONTEIRO',
    'JOAO NEIVA',
    'LARANJA DA TERRA',
    'LINHARES',
    'MANTENOPOLIS',
    'MARATAIZES',
    'MARECHAL FLORIANO',
    'MARILANDIA',
    'MIMOSO DO SUL',
    'MONTANHA',
    'MUCURICI',
    'MUNIZ FREIRE',
    'MUQUI',
    'NOVA VENECIA',
    'PANCAS',
    'PEDRO CANARIO',
    'PINHEIROS',
    'PIUMA',
    'PONTO BELO',
    'PRESIDENTE KENNEDY',
    'RIO BANANAL',
    'RIO NOVO DO SUL',
    'SANTA LEOPOLDINA',
    'SANTA MARIA DE JETIBA',
    'SANTA TERESA',
    'SAO DOMINGOS DO NORTE',
    'SAO GABRIEL DA PALHA',
    'SAO JOSE DO CALCADO',
    'SAO MATEUS',
    'SAO ROQUE DO CANAA',
    'SERRA',
    'SOORETAMA',
    'VARGEM ALTA',
    'VENDA NOVA DO IMIGRANTE',
    'VIANA',
    'VILA PAVAO',
    'VILA VALERIO',
    'VILA VELHA',
    'VITORIA'
]


def trata_dados_linha(linha):
    """ Trata e corrige os valores das linhas dos arquivos csv de relatórios."""

    for i in range(0, 6):
        try:
            linha[i] = arrow.get(linha[i])
        except arrow.ParserError:
            linha[i] = arrow.get(linha[i], ["DD/MM/YYYY", "DD-MM-YYYY",
                                            "DD_MM_YYYY", "DD.MM.YYYY", "DDMMYYYY"])

    if linha[8] in ["Ignorado", "-"]:
        linha[8] = None
    if "-" in linha[9]:
        linha[9] = None
    if "Encontrado" in linha[12]: # "Não Encontrado"
        linha[12] = None
    if "Ignorado" in linha[15]:
        linha[15] = None
    if "Ignorado" in linha[16]:
        linha[16] = None

    stringParaBool = {
        "Sim": True,
        "Não": False,
        "Ignorado": None,
        "Não Informado"
        "-": None,
        "": None,
        1: True,
        2: None,
    }
    for i, campo in enumerate(linha[17:]):
        linha[i + 17] = stringParaBool.get(linha[i + 17], None)

    return linha


def remove_caracteres_especiais(stringEntrada):
    """Remove caracteres especiais (acentos, etc) de uma string."""

    formaNFKD = unicodedata.normalize('NFKD', stringEntrada)
    return u"".join([c for c in formaNFKD if not unicodedata.combining(c)])
