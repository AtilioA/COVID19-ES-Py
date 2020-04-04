from COVID19_ES_Py import ScraperBoletim

scraper = ScraperBoletim()


def test_pega_dataPublicacao_formatada():
    boletimPesquisa = scraper.pesquisa_boletim_data("27/03/2020")
    assert(boletimPesquisa.pega_dataPublicacao_formatada() == "27/03/2020 19h12")

    boletimPesquisa = scraper.pesquisa_boletim_data("28/03/2020")
    assert(boletimPesquisa.pega_dataPublicacao_formatada() == "28/03/2020 19h01")

    boletimPesquisa = scraper.pesquisa_boletim_data("29/03/2020")
    assert(boletimPesquisa.pega_dataPublicacao_formatada() == "29/03/2020 19h25")


def test_pega_dataAtualizacao_formatada():
    boletimPesquisa = scraper.pesquisa_boletim_data("27/03/2020")
    assert(boletimPesquisa.pega_dataAtualizacao_formatada() == "28/03/2020 19h02")

    boletimPesquisa = scraper.pesquisa_boletim_data("28/03/2020")
    assert(boletimPesquisa.pega_dataAtualizacao_formatada() == "28/03/2020 19h14")

    boletimPesquisa = scraper.pesquisa_boletim_data("29/03/2020")
    assert(boletimPesquisa.pega_dataAtualizacao_formatada() == "30/03/2020 20h13")
