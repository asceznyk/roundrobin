import json

import numpy as np


def round_robin(config_path:str):
    with open(config_path, 'r') as f:
        teams = json.load(f)['teams']

    n = len(teams)
    swap = 0
    robin = []

    assert n%2 == 0, "number of teams must be even!"

    print('')
    for i in range(1, n):
        robin = [teams[0]] + teams[i:] + teams[1:i]
        print(f"matchday: {i}")
        swap ^= 1
        for k in range(n//2):
            match = f"{robin[-k-1]} vs {robin[k]}"
            if swap: match = f"{robin[k]} vs {robin[-k-1]}"
            print(match)
        print('')


round_robin("config.json")
