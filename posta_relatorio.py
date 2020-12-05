#!/usr/bin/python3.8

from automatiza_subida_dados_brasil_io import automatiza_subida

import argparse

# Parse cli arguments
parser = argparse.ArgumentParser(description="Process args.")


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


parser.add_argument(
    "--download",
    "-d",
    type=str2bool,
    nargs="?",
    const=True,
    default=True,
    help="download covid-19 data.",
)

args = parser.parse_args()
shouldDownload = args.download


def envia_relatorio():
    ultimoRelatorio = automatiza_subida(download=shouldDownload)


if __name__ == "__main__":
    envia_relatorio()
