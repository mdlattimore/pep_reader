import requests 
# from bs4 import BeautifulSoup
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

def get_pep(url):
    url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        results = soup.find(id="pep-content")
        return results.text
    except AttributeError:
        print()
        print("There is no pep with that number.")
        print()
        sys.exit()

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
    display_text = response.text
    with open(f"{directory}/pep_{pep}.txt", mode="w") as file:
        file.write(display_text)

with console.pager(styles=True):
    console.print(display_text)

print()
print()

