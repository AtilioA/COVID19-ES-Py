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


# Cria tabela com relatório para um dia apenas
def relatorio_para_tabela(path, data=None, caminhoCSV=None):
    if data and caminhoCSV:
        leitor = LeitorRelatorio(caminhoCSV)
        relatorio = leitor.filtra_casos_ate_dia(data)
        dataRelatorio = arrow.get(data, "DD/MM/YYYY").format("DD_MM")
    elif data:
        dataRelatorio = END.format("DD_MM")
        relatorio = leitor.filtra_casos_ate_dia(dataRelatorio)

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
    print(f"Municípios infectados: {relatorio.nMunicipiosInfectados}")
    print(f"Total geral: {totalGeral}")

    with open(arquivoCriado, "w+", encoding="utf-8") as f:
        f.write(
            f"municipio|confirmados|mortes\n")
        f.write(f"TOTAL NO ESTADO|{totalGeral['casosConfirmados']}|{totalGeral['obitos']}\n")
        f.write(
            f"Importados/Indefinidos|{relatorio.importadosOuIndefinidos['casosConfirmados']}|{relatorio.importadosOuIndefinidos['obitos']}\n")
        for i, (municipio, objMunicipio) in enumerate(sorted(relatorio.casosMunicipios.items())):
            casosConfirmados = objMunicipio.casosConfirmados
            obitos = objMunicipio.obitos
            f.write(f"{MUNICIPIOS_SEM_TRATAMENTO[i]}|{casosConfirmados}|{obitos}\n")
        print(f"Tabela do relatório salva em {arquivoCriado}.")


if __name__ == "__main__":
    relatorio_para_tabela(".", caminhoCSV=f"{END.format('DD-MM-YYYY')}.csv")
