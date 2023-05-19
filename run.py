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
        for k in range(n//2):
            t = (k, -k-1)
            print(f"{robin[t[swap]]} vs {robin[t[1-swap]]}")
        print('')
        swap ^= 1


round_robin("config.json")
