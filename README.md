<h1 align="center">
  <br>
  <a href="https://pypi.org/project/pycep-correios/">
  <img src="docs/logo_COVID19-ES-Py.png" width="30%"></a>
  <br>
  COVID19-ES-Py
  <br>
</h1>

<h4 align="center">API em Python para consulta de casos de COVID-19 no estado do Espírito Santo.</h4>

<p align="center">
  <a href="#recursos">Recursos</a> |
  <a href="#instalação">Instalação</a> |
  <a href="#como-usar">Como usar</a> |
  <a href="#exemplos">Exemplos</a> |
  <a href="#considerações-finais">Considerações finais</a>
</p>

# Recursos
* Extrai URLs de boletins emitidos pelo Governo do Estado do Espírito Santo;
* Coleta números de casos dos boletins;
* Possibilita pesquisa de casos por município.

# Instalação
Utilize seu gerenciador de pacotes preferido para instalar o pacote. Com `pip`:

```shell
pip install covid19-es-py
```

Atualmente, o COVID19-ES-Py possui suporte para Python 3.5+.

# Como usar

A API possui duas classes: `ScraperBoletim` e `Boletim`. A primeira é capaz de extrair links de boletins e usa objetos `Boletim` para fazer a interface para o programador. A segunda pode ser utilizada para extrair informações de um boletim específico.

## Exemplos
```python
import covid19_es_py

# Inicializando o scraper
scraper = covid19_es_py.ScraperBoletim()

# Carregando objeto Boletim com último boletim emitido
boletim = scraper.carrega_ultimo_boletim()
boletim.casos
>>> {'Afonso Cláudio': {'casosConfirmados': '0', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '1',},
...
'Vitória': {'casosConfirmados': '18', 'casosDescartados': '96', 'casosSuspeitos': '142', 'totalCasos': '256'}}

boletim.totalGeral
>>> {'casosConfirmados': '53 + 1*', 'casosDescartados': '411', 'casosSuspeitos': '1.105', 'totalCasos': '1.570'}

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

<!-- ## Documentação
Você pode aprender mais sobre a API lendo a [documentação oficial](https://www.google.com.br). -->

## Considerações finais
Encontrou algum erro? Tem alguma sugestão para melhorar a COVID19-ES-Py? [Crie uma issue!](https://github.com/atilioa/covid19-es-py/issues) Contribuições são muito bem-vindas.

Os dados são disponibilizados pelo Governo do Estado do Espírito Santo com a Superintendência Estadual de Comunicação Social do Espírito Santo (SECOM).
