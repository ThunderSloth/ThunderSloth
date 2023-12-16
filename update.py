# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11

from shields import shields
from lichess import LC
from monkeytype import MT
from discogs import DC

STYLE = "for-the-badge"

dynamic = [
    LC(),
    MT(),
    DC(),
]

static = [
    "![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)",
    "![java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)",
    "![lua](https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white)",
    "![git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)",
    "![sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)",
    "![LaTeX](https://img.shields.io/badge/LaTeX-008080.svg?style=for-the-badge&logo=LaTeX&logoColor=white)",
    "![nvim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white)",
    "![wezterm](https://img.shields.io/badge/WezTerm-4E49EE.svg?style=for-the-badge&logo=WezTerm&logoColor=white)"
    "![ai](https://img.shields.io/badge/Adobe%20Illustrator-FF9A00.svg?style=for-the-badge&logo=Adobe-Illustrator&logoColor=white)",
]

[print(badge) for badge in static]

[print(shields(*badge.parameters, STYLE)) for badge in dynamic]
