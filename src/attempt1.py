"""
Here we go
"""

import pprint
from greedy_alg import greed_alg
from dataparser import getData

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(greed_alg(getData('kittens')))