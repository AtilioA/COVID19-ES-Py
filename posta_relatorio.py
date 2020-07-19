import os
import signal
from automatiza_subida_dados_brasil_io import automatiza_subida
from pathlib import Path
import arrow
import telegram
from telegram.ext import Updater
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# CREDENTIALS
token = os.getenv("TELEGRAM_INMETBOT_APIKEY")


# TELEGRAM CONFIG
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
bot = telegram.Bot(token)


def constroi_mensagem_relatorio(relatorio, confirmadosOntem, obitosOntem):
    data = arrow.now("America/Sao_Paulo").format("DD/MM/YYYY")

    diffConfirmados = relatorio.totalGeral['casosConfirmados'] - confirmadosOntem
    diffMortes = relatorio.totalGeral['obitos'] - obitosOntem

    stringRelatorio = f"""*RELATÓRIO DE {data}*

*Casos confirmados*: {relatorio.totalGeral["casosConfirmados"]} (*+{diffConfirmados}*).
*Óbitos*: {relatorio.totalGeral["obitos"]} (*+{diffMortes}*).
*Todos os municípios* ({relatorio.nMunicipiosInfectados}) possuem casos confirmados.

Mais informações no [painel sobre COVID-19](https://coronavirus.es.gov.br/painel-covid-19-es).
"""

    return stringRelatorio


def envia_relatorio():
    """Send message with latest relatorio information."""

    dataHoje = arrow.utcnow().to("Brazil/East")
    dataOntem = dataHoje.shift(days=-1)

    with open(f"ES_{dataOntem.format('DD-MM')}.csv", encoding="utf-8") as dadosOntem:
        totalNoEstado = [next(dadosOntem) for x in range(2)]
    totalNoEstado = totalNoEstado[1].split("|")[1:]

    confirmadosOntem = int(totalNoEstado[0])
    obitosOntem = int(totalNoEstado[1])

    ultimoRelatorio = automatiza_subida()

    stringRelatorio = constroi_mensagem_relatorio(
        ultimoRelatorio, confirmadosOntem, obitosOntem)

    updater.bot.send_message(chat_id="@BoletimCOVID19ES", text=stringRelatorio,
                             parse_mode="markdown", disable_web_page_preview=True)
    updater.bot.send_message(chat_id="-1001308085632", text=stringRelatorio,
                             parse_mode="markdown", disable_web_page_preview=True)

    # Send MICRODADOS.csv for the current day
    dadosPath = Path(f"C:\\Users\\Casa\\Desktop\\ES_{dataHoje.format('DD-MM')}.csv")

    updater.bot.send_document(chat_id='467672701', document=open(dadosPath, 'rb'))


if __name__ == "__main__":
    envia_relatorio()
    os.kill(os.getppid(), signal.SIGHUP)
