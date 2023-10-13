# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11
from lichess import Lichess as li
class Badge():
    def __init__(self, name, url):
        self._name = name
        self._url = url
    def __repr__(self):
        return f"Badge('{self._name}', '{self._url}')"
    def __str__(self):
        return f"![{self._name.upper()}]({self._url})"
print(Badge("lichess", str(li())))
