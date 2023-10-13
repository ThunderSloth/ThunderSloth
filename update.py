# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11
import Lichess from lichess as lc

class Badge():
    def __init__(self, name, url):
        self._name = name
        self._url = url
        self._markdown = f"![{name.upper()}]({url})"
    @property
    def markdown(self):
        return self._badge

print(Badge("lichess", lc.shield).markdown)
