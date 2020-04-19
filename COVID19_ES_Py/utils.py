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

    linha[0] = arrow.get(linha[0])

    if linha[2] in ["Ignorado", "-"]:
        linha[2] = None
    if "-" in linha[3]:
        linha[3] = None
    if linha[6] in ["Não encontrado", "NULL"]:
        linha[6] = None
    if "Ignorado" in linha[9]:
        linha[9] = None
    if "Ignorado" in linha[10]:
        linha[10] = None

    stringParaBool = {
        "Sim": True,
        "Não": False,
        "-": None,
        "": None,
        1: True,
        2: None,
    }
    for i, campo in enumerate(linha[11:]):
        linha[i + 11] = stringParaBool.get(linha[i + 11], None)

    return linha


def trata_dados_tabela(linha):
    """ Substitui caracteres vazios de uma lista por zeros.
    Utilizada para tratar valores das colunas das tabelas dos boletins."""

    patternEntradasInvalidas = re.compile(r"\xa0|&nbsp;|^\s*$|\s*-\s*")
    linha = map(lambda coluna: re.sub(
        patternEntradasInvalidas, "0", coluna), linha)
    return list(linha)


def remove_caracteres_especiais(stringEntrada):
    """Remove caracteres especiais (acentos, etc) de uma string."""

    formaNFKD = unicodedata.normalize('NFKD', stringEntrada)
    return u"".join([c for c in formaNFKD if not unicodedata.combining(c)])
