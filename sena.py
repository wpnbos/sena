from pathlib import Path
from random import randint

hiragana = {
    line.split(',')[0]: line.split(',')[1]
    for line in Path(__file__).parent.joinpath("hiragana.csv").read_text().splitlines()
}

while True:
    i = randint(0, 15)
    query = list(hiragana.keys())[i]
    answer = input(f'{query}: ').strip()
    while answer != hiragana[query]:
        print("WRONG!!! try again")
        answer = input(f'{query}: ').strip()
