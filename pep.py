import requests 
from rich.console import Console
import argparse
import sys
import os
from pathlib import Path


console = Console()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

parser = argparse.ArgumentParser()

parser.add_argument("pep")

args = parser.parse_args()

pep = str(args.pep).zfill(4)

directory = Path.home() / ".peps"
directory.mkdir(exist_ok=True)
path = directory / f"pep_{pep}.txt"

if path.is_file():
    with open(f"{directory}/pep_{pep}.txt", mode="r") as file:
        display_text = file.read()
else:  
    url = f"https://raw.githubusercontent.com/python/peps/main/pep-{pep}.txt"
    response = requests.get(url)
    if response.status_code == 404:
        print()
        print()
        print("No pep found with that number.")
        print()
        print()
        sys.exit()
    else:
        display_text = response.text
        with open(f"{directory}/pep_{pep}.txt", mode="w") as file:
            file.write(display_text)
    

with console.pager(styles=True):
    console.print(display_text)

print()
print()
print("Bye")


