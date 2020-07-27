import argparse
import subprocess
import sys
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--download", "-d", action='store_true',
    help="download covid-19 data.")
parser.add_argument("--telegram", "-t", action='store_true',
    help="post results on telegram.")

args = parser.parse_args()

if __name__ == "__main__":
    stringArgs = ' '.join(sys.argv[1:])
    python_bin = os.path.abspath("/home/atilioa/.virtualenvs/covid19-es-py/bin/python3.8")
    print(f'posta_relatorio.py {stringArgs}')
    os.system(f'{python_bin} posta_relatorio.py {stringArgs}')
