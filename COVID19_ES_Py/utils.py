"""O módulo `utils.py` contém funções e constantes auxiliares."""

import unicodedata
import re


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


def trata_entradas_tabela(linha):
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
