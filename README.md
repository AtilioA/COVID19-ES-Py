<h1 align="center">
  <br>
  <a href="https://pypi.org/project/COVID19-ES-Py/">
  <img src="https://raw.githubusercontent.com/AtilioA/COVID19-ES-Py/c28e8a1f8799d6a067d7c4587a9467d3bc595e9e/docs/logo_COVID19-ES-Py.png" width="30%"></a>
  <br>
  COVID19-ES-Py
  <br>
</h1>

<h4 align="center">API em Python para consulta de casos de COVID-19 no estado do Espírito Santo.</h4>

<h5 align="center">

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/COVID19-ES-Py.svg)](https://pypi.python.org/pypi/COVID19-ES-Py/) ![PyPI](https://img.shields.io/pypi/v/COVID19-ES-Py) ![Travis (.org)](https://img.shields.io/travis/AtilioA/COVID19-ES-Py) ![Read the Docs](https://img.shields.io/readthedocs/covid19-es-py) ![Codecov](https://img.shields.io/codecov/c/github/atilioa/covid19-es-py) ![Codacy grade](https://img.shields.io/codacy/grade/fcb128b62ff64a8ab51da5629bb11556)

![PyPI - Downloads](https://img.shields.io/pypi/dm/covid19-es-py) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-orange.svg)](https://www.gnu.org/licenses/gpl-3.0)

</h5>

<p align="center">
  <a href="#recursos">Recursos</a> |
  <a href="#instalação">Instalação</a> |
  <a href="#como-usar">Como usar</a> |
  <a href="#exemplos">Exemplos</a> |
  <a href="#documentação">Documentação</a> |
  <a href="#considerações-finais">Considerações finais</a>
</p>

# Recursos
* Extração de URLs de boletins emitidos pela Secretaria de Estado da Saúde (SESA)
* Extração de título, datas, corpo de notícia, números de casos e óbitos, etc, dos boletins
* Pesquisa de casos por município
* Pesquisa de boletim por data
* Filtro de municípios com casos confirmados

# Instalação
Atualmente, o COVID19-ES-Py possui suporte para Python 3.6+. Uma mesma release é feita ao PyPI e ao GitHub ao mesmo tempo, portanto use a fonte que achar mais conveniente.

## Pelo repositório PyPI
Utilize seu gerenciador de pacotes preferido para instalar o pacote. Com `pip`:

```shell
pip install COVID19-ES-Py
```

## Pelo código fonte
1. [Baixe a última release](https://github.com/AtilioA/COVID19-ES-Py/releases/latest) e extraia a pasta;
2. Entre no diretório raiz do pacote pelo terminal e rode o comando `python setup.py install`

# Como usar

A API possui duas classes: `ScraperBoletim` e `Boletim`. A primeira é capaz de extrair links de boletins, buscar boletins por data, etc, usando objetos `Boletim` para fazer a interface para o programador. A segunda pode ser utilizada para extrair informações de um boletim específico. Confira os exemplos a seguir:

## Exemplos

### Inicializando o scraper e obtendo dados do último boletim:
```python
import COVID19_ES_Py

# Inicializando o scraper
scraper = COVID19_ES_Py.ScraperBoletim()

# Carregando objeto Boletim com último boletim emitido
boletim = scraper.carrega_ultimo_boletim()  # Boletim do dia 27/03/2020
boletim.casos
>>> {'Afonso Cláudio': {'casosConfirmados': '0', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '1'},
...
'Vitória': {'casosConfirmados': '18', 'casosDescartados': '96', 'casosSuspeitos': '142', 'totalCasos': '256'}}
```

Total de casos do boletim:
```python
boletim.totalGeral
>>> {'casosConfirmados': '53 + 1*', 'casosDescartados': '411', 'casosSuspeitos': '1.105', 'totalCasos': '1.570'}
```

### Pesquisando casos por município:
Retorna dicionário de casos do município no boletim:
```python
boletim.pesquisa_casos_municipio("Vitória")
>>> {'casosConfirmados': '18', 'casosDescartados': '96', 'casosSuspeitos': '142', 'totalCasos': '256'}

# A busca ignora espaços extras e capitalização
boletim.pesquisa_casos_municipio("  santa teresa ")
>>> {'casosConfirmados': '1', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '2'}

# Também ignora caracteres especiais
boletim.pesquisa_casos_municipio("AFONSO CLAUDIO")
>>> {'casosConfirmados': '0', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '1'}

boletim.pesquisa_casos_municipio("arapiraca")
>>> exceptions.BoletimError: O município "arapiraca" não foi encontrado no boletim. Pode ter ocorrido um erro de digitação ou o município não registrou casos de COVID-19.
```

### Pesquisando boletim por data:
Retorna o boletim da data de entrada, se houver:
```python
boletim29_03 = scraper.pesquisa_boletim_data("29/03/2020")
boletim29_03.pega_dataPublicacao_formatada()
>>> "29/03/2020 19h25"
```
A data de entrada [pode ser formatada de várias formas](https://covid19-es-py.readthedocs.io/pt_BR/latest/COVID19_ES_Py.html#COVID19_ES_Py.boletim.ScraperBoletim.pesquisa_boletim_data).

### Filtrando municípios com casos confirmados:
Retorna dicionário de dicionários com municípios com casos confirmados:
```python
boletim05_04 = scraper.pesquisa_boletim_data("05/04/2020")

municipiosFiltrados = boletim05_04.filtra_municipios_com_casos_confirmados()
municipiosFiltrados
>>> {'Afonso Cláudio': {"casosConfirmados": '1', "casosDescartados": "3", "casosSuspeitos": "3", "totalCasos": "7", "obitos": "0"},
...
'Vitória': {'casosConfirmados': '62', 'casosDescartados': '252', 'casosSuspeitos': '58', 'totalCasos': '372', 'obitos': '2'}}

boletim05_04.nMunicipiosInfectados
>>> 18
len(municipiosFiltrados)
>>> 18
```

## Documentação
Você pode aprender mais sobre a API lendo a [documentação oficial](https://covid19-es-py.readthedocs.io/pt_BR/latest/).

## Considerações finais
Encontrou algum erro? Tem alguma sugestão para melhorar a COVID19-ES-Py? [Crie uma issue!](https://github.com/atilioa/COVID19-ES-Py/issues) Contribuições são muito bem-vindas.

Os dados são disponibilizados pelo Governo do Estado do Espírito Santo com a Superintendência Estadual de Comunicação Social do Espírito Santo (SECOM).
