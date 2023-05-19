from typing import List

import math
import json
import random

import numpy as np


def round_robin(config_path:str):
    with open(config_path, 'r') as f:
        teams = json.load(f)['teams']

    n = len(teams)
    swap = 0
    robin = []
    matches = []

    assert n%2 == 0, "number of teams must be even!"

    print('')
    for i in range(1, n):
        robin = [teams[0]] + teams[i:] + teams[1:i]
        print(f"matchday: {i}")
        swap ^= 1
        for k in range(n//2):
            match = f"{robin[-k-1]} vs {robin[k]}"
            if swap:
                match = f"{robin[k]} vs {robin[-k-1]}"

            if match in matches:
                raise Exception("Repetitive Matches")

            matches.append(match)
            print(match)
        print('')


#class RoundRobinTournament:
#    def __init__(self, config_path):
#        self.teams = teams
#        self.latestarr = []
#
#    def print_round(self, index:int, totarr:List, swap:bool):
#        print('Matchday '+str(index))
#        printteams = []
#        for i in range(len(totarr)):
#                printteams.append(self.teams[totarr[i]])
#
#        for k in range():
#            match = printteams[-k-1] + ' vs ' + printteams[k]
#            if swap:
#                match = printteams[k] + ' vs ' + printteams[-k-1]
#
#            print(match)
#
#        print(' ')
#
#    def circle_method(self, index:int, altbool:bool):
#        altbool ^= 1
#
#        if index > len(indices)-1: return None
#
#        latestnum = indices[-index]
#        self.latestarr = [latestnum] + self.latestarr
#        restnum = [i for i in range(1, latestnum)]
#        zeroarr = [0]
#        totarr = zeroarr + self.latestarr + restnum
#        self.print_round(index, totarr, altbool)
#        self.circle_method(indices, index+1, altbool)

round_robin("config.json")


