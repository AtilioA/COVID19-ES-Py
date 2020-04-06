.. COVID19-ES-Py documentation master file, created by
   sphinx-quickstart on Sun Mar 29 15:33:52 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Início
=========================================

Índices
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. raw:: html

   <h1 align="center">
     <br>
     <a href="https://pypi.org/project/COVID19-ES-Py/">
     <img src="https://raw.githubusercontent.com/AtilioA/COVID19-ES-Py/master/docs/logo_COVID19-ES-Py.png" width="40%"></a>
     <br>
     COVID19-ES-Py
     <br>
   </h1>

.. image:: https://img.shields.io/pypi/pyversions/COVID19-ES-Py.svg
   :target: https://pypi.python.org/pypi/COVID19-ES-Py/
   :alt: PyPI pyversions

.. image:: https://img.shields.io/pypi/v/COVID19-ES-Py
   :target: https://img.shields.io/pypi/v/COVID19-ES-Py
   :alt: PyPI

.. image:: https://img.shields.io/travis/AtilioA/COVID19-ES-Py
   :target: https://img.shields.io/travis/AtilioA/COVID19-ES-Py
   :alt: Travis (.org)

.. image:: https://img.shields.io/readthedocs/covid19-es-py
   :alt: Read The Docs

.. image:: https://img.shields.io/codecov/c/github/atilioa/covid19-es-py
   :alt: Codecov
.. image:: https://img.shields.io/codacy/grade/fcb128b62ff64a8ab51da5629bb11556
   :alt: Codacy grade

.. image:: https://img.shields.io/pypi/dm/covid19-es-py
   :target: https://img.shields.io/pypi/dm/covid19-es-py
   :alt: PyPI - Downloads

.. image:: https://img.shields.io/badge/License-GPLv3-orange.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
   :alt: License: GPL v3


.. raw:: html

   <h4 align="center">API em Python para consulta de casos de COVID-19 no estado do Espírito Santo.</h4>


.. raw:: html

   <p align="center">
     <a href="#recursos">Recursos</a> |
     <a href="#instalacao">Instalação</a> |
     <a href="#como-usar">Como usar</a> |
     <a href="#exemplos">Exemplos</a> |
     <a href="#consideracoes-finais">Considerações finais</a>
   </p>


Recursos
========


* Extrai URLs de boletins emitidos pelo Governo do Estado do Espírito Santo
* Coleta título, datas, corpo de notícia, números de casos, etc, dos boletins
* Possibilita pesquisa de casos por município

Instalação
==========

Atualmente, o COVID19-ES-Py possui suporte para Python 3.6+.

Pelo repositório PyPI
^^^^^^^^^^^^^^^^^^^^^

Utilize seu gerenciador de pacotes preferido para instalar o pacote. Com ``pip``\ :

.. code-block:: shell

   pip install COVID19-ES-Py

Pelo código fonte
^^^^^^^^^^^^^^^^^


#. Clone/baixe o repositório ou `baixe a última release <https://github.com/AtilioA/COVID19-ES-Py/releases>`_\ ;
#. Entre no diretório raiz do pacote pelo terminal e rode o comando ``python setup.py install``

Como usar
=========

A API possui duas classes: ``ScraperBoletim`` e ``Boletim``. A primeira é capaz de extrair links de boletins e usa objetos ``Boletim`` para fazer a interface para o programador. A segunda pode ser utilizada para extrair informações de um boletim específico. Confira os exemplos a seguir:


Exemplos
^^^^^^^^


Inicializando o scraper e obtendo dados do último boletim:

.. code-block:: python

   import COVID19_ES_Py

   # Inicializando o scraper
   scraper = COVID19_ES_Py.ScraperBoletim()

   # Carregando objeto Boletim com último boletim emitido
   boletim = scraper.carrega_ultimo_boletim()
   boletim.casos
   >>> {'Afonso Cláudio': {'casosConfirmados': '0', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '1',},
   ...
   'Vitória': {'casosConfirmados': '18', 'casosDescartados': '96', 'casosSuspeitos': '142', 'totalCasos': '256'}}

Total de casos do boletim:

.. code-block:: python

   boletim.totalGeral
   >>> {'casosConfirmados': '53 + 1*', 'casosDescartados': '411', 'casosSuspeitos': '1.105', 'totalCasos': '1.570'}

Pesquisando casos por município:

.. code-block:: python

   boletim.pesquisa_casos_municipio("Vitória")
   >>> {'casosConfirmados': '18', 'casosDescartados': '96', 'casosSuspeitos': '142', 'totalCasos': '256'}

   # A busca ignora espaços extras e capitalização
   boletim.pesquisa_casos_municipio("  santa teresa ")
   >>> {'casosConfirmados': '1', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '2'}

   # Também ignora caracteres especiais
   boletim.pesquisa_casos_municipio("AFONSO CLAUDIO")
   >>> {'casosConfirmados': '0', 'casosDescartados': '1', 'casosSuspeitos': '0', 'totalCasos': '1'}

   boletim.pesquisa_casos_municipio("arapiraca")
   >>> exceptions.BoletimError: O município "arapiraca" não foi encontrado no boletim.
   Pode ter ocorrido um erro de digitação ou o município não registrou casos de COVID-19.


Considerações finais
====================

Encontrou algum erro? Tem alguma sugestão para melhorar a COVID19-ES-Py? `Crie uma issue! <https://github.com/atilioa/COVID19-ES-Py/issues>`_ Contribuições são muito bem-vindas.

Os dados são disponibilizados pelo Governo do Estado do Espírito Santo com a Superintendência Estadual de Comunicação Social do Espírito Santo (SECOM).
