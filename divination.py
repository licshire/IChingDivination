import random
from math import floor

coin_toss = [[floor(random.random()*2) for j in range(3)] for i in range(6)]

print coin_toss

