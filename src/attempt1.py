"""
Here we go
"""

import pprint
from greedy_alg import greed_alg
from dataparser import getData, setData

pp = pprint.PrettyPrinter(indent=4)

for name in ['kittens', 'me_at_the_zoo', 'trending_today', 'videos_worth_spreading']:
    setData(greed_alg(getData(name)), name)