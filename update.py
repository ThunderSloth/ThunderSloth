# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11

from shields import Shields
from lichess import Lichess 

STYLE = "plastic"

shields = [Lichess(username='elib', time_format='blitz'),]

for shield in shields:
    print(Shields(*shield.parameters, STYLE).badge)

