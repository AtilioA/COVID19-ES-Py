<h1 align="center">
  <br>
  <a href="https://pypi.org/project/COVID19-ES-Py/">
  <img src="https://raw.githubusercontent.com/AtilioA/COVID19-ES-Py/c28e8a1f8799d6a067d7c4587a9467d3bc595e9e/docs/logo_COVID19-ES-Py.png" width="30%"></a>
  <br>
  COVID19-ES-Py
  <br>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/05b810f70532448ea2c6da76b8dd5f17)](https://app.codacy.com/manual/atiliodadalto/COVID19-ES-Py?utm_source=github.com&utm_medium=referral&utm_content=AtilioA/COVID19-ES-Py&utm_campaign=Badge_Grade_Dashboard)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/COVID19-ES-Py.svg)](https://pypi.python.org/pypi/COVID19-ES-Py/) ![PyPI](https://img.shields.io/pypi/v/COVID19-ES-Py) ![Travis (.org)](https://img.shields.io/travis/AtilioA/COVID19-ES-Py) ![Read the Docs](https://img.shields.io/readthedocs/covid19-es-py) ![Codacy grade](https://img.shields.io/codacy/grade/2a7bb708cf374f2badcdbe30b5342377) ![Codecov](https://img.shields.io/codecov/c/github/atilioa/covid19-es-py)

[![HitCount](http://hits.dwyl.com/atilioa/COVID19-ES-Py.svg)](http://hits.dwyl.com/atilioa/COVID19-ES-Py) ![PyPI - Downloads](https://img.shields.io/pypi/dm/covid19-es-py) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-orange.svg)](https://www.gnu.org/licenses/gpl-3.0)

<h4 align="center">API em Python para consulta de casos de COVID-19 no estado do Espírito Santo.</h4>

<p align="center">
  <a href="#recursos">Recursos</a> |
  <a href="#instalação">Instalação</a> |
  <a href="#como-usar">Como usar</a> |
  <a href="#exemplos">Exemplos</a> |
  <a href="#documentação">Documentação</a> |
  <a href="#considerações-finais">Considerações finais</a>
</p>

# Recursos
* Extrai URLs de boletins emitidos pelo Governo do Estado do Espírito Santo
* Coleta título, datas, corpo de notícia, números de casos, etc, dos boletins
* Possibilita pesquisa de casos por município

# Instalação
Atualmente, o COVID19-ES-Py possui suporte para Python 3.6+.

### Pelo repositório PyPI
Utilize seu gerenciador de pacotes preferido para instalar o pacote. Com `pip`:

```shell
pip install COVID19-ES-Py
```

### Pelo código fonte
1. [Baixe a última release](https://github.com/AtilioA/COVID19-ES-Py/releases/latest) e extraia a pasta;
2. Entre no diretório raiz do pacote pelo terminal e rode o comando `python setup.py install`

# Como usar

A API possui duas classes: `ScraperBoletim` e `Boletim`. A primeira é capaz de extrair links de boletins e usa objetos `Boletim` para fazer a interface para o programador. A segunda pode ser utilizada para extrair informações de um boletim específico. Confira os exemplos a seguir:

## Exemplos
Inicializando o scraper e obtendo dados do último boletim:
```python
import COVID19_ES_Py

# Inicializando o scraper
scraper = COVID19_ES_Py.ScraperBoletim()

# Carregando objeto Boletim com último boletim emitido
boletim = scraper.carrega_ultimo_boletim()
boletim.casos
>>> {'Afonso Cláudio': {'casosConfirmados': '0', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '1',},
...
'Vitória': {'casosConfirmados': '18', 'casosDescartados': '96', 'casosSuspeitos': '142', 'totalCasos': '256'}}
```

Total de casos do boletim:
```python
boletim.totalGeral
>>> {'casosConfirmados': '53 + 1*', 'casosDescartados': '411', 'casosSuspeitos': '1.105', 'totalCasos': '1.570'}
```

Pesquisando casos por município:
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

## Documentação
Você pode aprender mais sobre a API lendo a [documentação oficial](https://covid19-es-py.readthedocs.io/pt_BR/latest/).

## Considerações finais
Encontrou algum erro? Tem alguma sugestão para melhorar a COVID19-ES-Py? [Crie uma issue!](https://github.com/atilioa/COVID19-ES-Py/issues) Contribuições são muito bem-vindas.

Os dados são disponibilizados pelo Governo do Estado do Espírito Santo com a Superintendência Estadual de Comunicação Social do Espírito Santo (SECOM).
