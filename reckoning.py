import os
from pathlib import Path
import shutil
import arrow
import subprocess

todayDate = arrow.now("America/Sao_Paulo")

# Get latest csv
latestCSV = max([file for file in os.listdir(".") if file.startswith("ES_")])

# Get due csvs
dueFiles = sorted(
    [os.path.join("due", file) for file in os.listdir("due") if file.endswith(".csv")]
)

print("Last csv:")
print(latestCSV)
print("Due csvs:")
print(dueFiles)
dueAnswer = input("Is this correct? [Y/N] ")

if dueAnswer.lower() in ["y", "s", "sim", "yes"]:
    yesterdayDate = todayDate.shift(days=-1)
    filenameYesterday = (
        f"ES_{yesterdayDate.format('DD')}-{yesterdayDate.format('MM')}.csv"
    )
    filenameToday = f"ES_{todayDate.format('DD')}-{todayDate.format('MM')}.csv"

    shutil.move(latestCSV, filenameYesterday)

    for file in dueFiles:
        # Copy oldest MICRODADOS to download folder (overwrite)
        currentCSV = dueFiles.pop(0)
        print("Arquivo:", currentCSV)
        shutil.copy(currentCSV, Path("/home/atilioa/Downloads/MICRODADOS.csv"))
        
        # Run posta_relatorio.py
        subprocess.run(["python", "posta_relatorio.py", "-d", "f"])
        
        # Rename desktop result file to actual day
        newCSVFilename = f'ES_{currentCSV[-6:-4]}-{yesterdayDate.format("MM")}.csv'
        print(currentCSV, newCSVFilename)
        
        os.rename(
            Path(os.path.join("/home/atilioa/Área de Trabalho", filenameToday)),
            Path(os.path.join("/home/atilioa/Área de Trabalho", newCSVFilename)),
        )
        
        try:
            os.remove(Path(os.path.join("/home/atilioa/Área de Trabalho", currentCSV)))
        except:
            pass
        
        # Rename current directory result file to yesterday (overwrite)
        shutil.copy(filenameToday, filenameYesterday)
