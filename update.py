# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11

from shields import shields
from lichess import LC
from monkeytype import MT
from discogs import DC

STYLE = "plastic"

dynamic = [
    LC(),
    MT(),
    DC(),
]

static = [
    "[!python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)",
    "[!java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)",
    "[!lua](https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white)",
    "[!sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)",
    "[!nvim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white)",
    "[!git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)",
    "[!ai](https://img.shields.io/badge/Adobe%20Illustrator-FF9A00?style=for-the-badge&logo=adobe%20illustrator&logoColor=white)",
]

[print(badge) for badge in static]

[print(shields(*badge.parameters, STYLE)) for badge in dynamic]
