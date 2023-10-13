# This script generates new markdown content for my GitHub profile README
# Eli Bell
# 2023-10-11
import lichess

class Badge():
    def __init__(self, name, url):
        self._name = name
        self._url = url
        self._badge = f"![{name.upper()}]({url})"
    @property
    def badge(self):
        return self._badge

print(Badge("lichess", Lichess.shield).badge)
