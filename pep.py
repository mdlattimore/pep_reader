# TODO provide path to PEP index. It's not on GitHub, so will need to scrape it from peps.python.org

import requests 
from rich.console import Console
from rich import print as rprint
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

# *** This Works -- Keep while testing ***
# else:  
#     url = f"https://raw.githubusercontent.com/python/peps/main/pep-{pep}.txt"
#     response = requests.get(url)
#     if response.status_code == 404:
#         print("\n" * 2)
#         rprint("No PEP found. Check the PEP Index at [link=https://peps.python.org/pep-0000]https://peps.python.org/pep-0000[/link] for a list of valid PEPS (to follow link, CMD-click on Mac, Ctrl-click on Windows).")
#         print("\n" * 2)
#         sys.exit()
#     else:
#         display_text = response.text
#         with open(f"{directory}/pep_{pep}.txt", mode="w") as file:
#             file.write(display_text)
# *** End of This Works Keep while testing ***

# *** Added to check for PEPs that are available only in .rst format ***
else:  
    url = f"https://raw.githubusercontent.com/python/peps/main/pep-{pep}.txt"
    response = requests.get(url)
    if response.status_code == 404:
        url = f"https://raw.githubusercontent.com/python/peps/main/pep-{pep}.rst"
        response = requests.get(url)
        if response.status_code == 404:
            print("\n" * 2)
            rprint("No PEP found. Check the PEP Index at [link=https://peps.python.org/pep-0000]https://peps.python.org/pep-0000[/link] for a list of valid PEPS (to follow link, CMD-click on Mac, Ctrl-click on Windows).")
            print("\n" * 2)
            sys.exit()
        else:
            display_text = response.text
            with open(f"{directory}/pep_{pep}.txt", mode="w") as file:
                file.write(display_text)
    else:
            display_text = response.text
            with open(f"{directory}/pep_{pep}.txt", mode="w") as file:
                file.write(display_text)
# *** End of rst checking code

with console.pager(styles=True):
    console.print(display_text)

print("\n" * 2)


