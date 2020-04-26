import os
from pathlib import Path
import arrow
from COVID19_ES_Py.relatorio import LeitorRelatorio

# Municípios que tiveram casos removidos (?)
MUNICIPIOS_MARCADOS = ["ALTO RIO NOVO", "VILA VALERIO"]
MUNICIPIOS_SEM_TRATAMENTO = [
    'Afonso Cláudio', 'Água Doce do Norte', 'Águia Branca', 'Alegre', 'Alfredo Chaves',
    'Alto Rio Novo', 'Anchieta', 'Apiacá', 'Aracruz', 'Atilio Vivacqua', 'Baixo Guandu',
    'Barra de São Francisco', 'Boa Esperança', 'Bom Jesus do Norte', 'Brejetuba',
    'Cachoeiro de Itapemirim', 'Cariacica', 'Castelo', 'Colatina', 'Conceição da Barra',
    'Conceição do Castelo', 'Divino de São Lourenço', 'Domingos Martins', 'Dores do Rio Preto',
    'Ecoporanga', 'Fundão', 'Governador Lindenberg', 'Guaçuí', 'Guarapari', 'Ibatiba', 'Ibiraçu',
    'Ibitirama', 'Iconha', 'Irupi', 'Itaguaçu', 'Itapemirim', 'Itarana', 'Iúna', 'Jaguaré',
    'Jerônimo Monteiro', 'João Neiva', 'Laranja da Terra', 'Linhares', 'Mantenópolis',
    'Marataízes', 'Marechal Floriano', 'Marilândia', 'Mimoso do Sul', 'Montanha', 'Mucurici',
    'Muniz Freire', 'Muqui', 'Nova Venécia', 'Pancas', 'Pedro Canário', 'Pinheiros', 'Piúma',
    'Ponto Belo', 'Presidente Kennedy', 'Rio Bananal', 'Rio Novo do Sul', 'Santa Leopoldina',
    'Santa Maria de Jetibá', 'Santa Teresa', 'São Domingos do Norte', 'São Gabriel da Palha',
    'São José do Calçado', 'São Mateus', 'São Roque do Canaã', 'Serra', 'Sooretama', 'Vargem Alta',
    'Venda Nova do Imigrante', 'Viana', 'Vila Pavão', 'Vila Valério', 'Vila Velha', 'Vitória'
]

START = arrow.get("2020-03-01")  # Início da planilha
END = arrow.now('America/Sao_Paulo')


# Cria toda a planilha com o último relatório disponível
def cria_planilha(path):
    dataRelatorio = END.format("DD_MM")
    # Intervalo de datas da planilha
    intervaloDatas = list(reversed(list(arrow.Arrow.span_range("day", START, END))))

    leitor = LeitorRelatorio()
    relatorio = leitor.carrega_ultimo_relatorio()
    relatorios = []  # Guarda relatórios de todas as datas
    for r in intervaloDatas:
        relatorio = leitor.filtra_casos_ate_dia(r[0].format("DD/MM/YYYY"))
        relatorios.append(relatorio)

    with open(Path(f"{path}/planilha_ES_{dataRelatorio}.csv".format(path)), "w+", encoding="utf-8") as f:
        # Preenche cabeçalho
        f.write("municipio|")
        for r in intervaloDatas:

            f.write(f"confirmados_{r[0].format('DD_MM')}|mortes_{r[0].format('DD_MM')}|")
        f.write("\n")

        # Preenche TOTAL NO ESTADO
        f.write(f"TOTAL NO ESTADO|")
        for i, r in enumerate(intervaloDatas):
            relatorio = relatorios[i]
            totalGeral = relatorio.totalGeral
            f.write(f"{totalGeral['casosConfirmados']}|{totalGeral['obitos']}|")
        f.write("\n")

        # Preenche IMPORTADOS/INDEFINIDOS
        f.write(f"Importados/Indefinidos|")
        for i, r in enumerate(intervaloDatas):
            relatorio = relatorios[i]
            totalGeral = relatorio.totalGeral
            f.write(
                f"{relatorio.importadosOuIndefinidos['casosConfirmados']}|{relatorio.importadosOuIndefinidos['obitos']}|")
        f.write("\n")

        # Preenche valores de municípios
        for municipio in MUNICIPIOS_SEM_TRATAMENTO:
            f.write(f"{municipio}|")
            for i, r in enumerate(intervaloDatas):
                relatorio = relatorios[i]
                objMunicipio = relatorio.busca_casos_municipio(municipio)

                casosConfirmados = objMunicipio.casosConfirmados if objMunicipio.casosConfirmados > 0 else ""
                obitos = objMunicipio.obitos if objMunicipio.obitos > 0 or casosConfirmados != "" else ""

                f.write(
                    f"{casosConfirmados}|{obitos}|")
            f.write("\n")


# Cria tabela com relatório para um dia apenas
def relatorio_para_tabela(path, data=None, caminhoCSV=None):
    if data:
        relatorio.rows = leitor.filtra_casos_ate_dia(data)
        dataRelatorio = arrow.get(data, "DD/MM/YYYY").format("DD_MM")
    else:
        dataRelatorio = END.format("DD_MM")

    if caminhoCSV:
        print(f"Lendo arquivo {os.path.basename(caminhoCSV)}")
        leitor = LeitorRelatorio(caminhoCSV)
        relatorio = leitor.relatorio
        arquivoCriado = Path(f"{path}/ES_{os.path.basename(caminhoCSV)[:5]}.csv")
    else:
        leitor = LeitorRelatorio()
        relatorio = leitor.carrega_ultimo_relatorio()
        arquivoCriado = Path(f"{path}/ES_{dataRelatorio}.csv")

    relatorio.popula_relatorio()

    totalGeral = relatorio.totalGeral
    print(f"Total geral: {totalGeral}")

    with open(arquivoCriado, "w+", encoding="utf-8") as f:
        f.write(
            f"municipio|confirmados|mortes\n")
        f.write(f"TOTAL NO ESTADO|{totalGeral['casosConfirmados']}|{totalGeral['obitos']}\n")
        f.write(
            f"Importados/Indefinidos|{relatorio.importadosOuIndefinidos['casosConfirmados']}|{relatorio.importadosOuIndefinidos['obitos']}\n")
        for i, (municipio, objMunicipio) in enumerate(sorted(relatorio.casosMunicipios.items())):
            casosConfirmados = objMunicipio.casosConfirmados if objMunicipio.casosConfirmados > 0 or municipio in MUNICIPIOS_MARCADOS else ""
            obitos = objMunicipio.obitos if objMunicipio.obitos > 0 or casosConfirmados != "" else ""
            f.write(f"{MUNICIPIOS_SEM_TRATAMENTO[i]}|{casosConfirmados}|{obitos}\n")
        print(f"Tabela do relatório salva em {arquivoCriado}.")


if __name__ == "__main__":
    relatorio_para_tabela(".", caminhoCSV="25_04_2020.csv")
