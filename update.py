# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11

from shields import shields
from lichess import LC 
from monkeytype import MT 
from discogs import DC

STYLE = "plastic"

badges = [
    LC(),
    MT(),
    DC(),
]

for badge in badges:
    print(shields(*badge.parameters, STYLE))

