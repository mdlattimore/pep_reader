# TODO provide path to PEP index. It's not on GitHub, so will need to scrape it from peps.python.org

import requests 
from rich.console import Console
import argparse
import sys
import os
from pathlib import Path


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


console = Console()

clear()

parser = argparse.ArgumentParser(
    description="A simple cli to retrieve Python PEPs",
    prog="PEP Reader"
)

parser.add_argument("pep",
                    help="Enter the number of the desired PEP. Enter 0 for the PEP index."
                    )

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
        print("\n" * 2)
        print("No PEP found. Check the index at https://peps.python.org/pep-0000 for a list of valid PEPS.")
        print("\n" * 2)
        sys.exit()
    else:
        display_text = response.text
        with open(f"{directory}/pep_{pep}.txt", mode="w") as file:
            file.write(display_text)
    
with console.pager(styles=True):
    console.print(display_text)

print("\n" * 2)


