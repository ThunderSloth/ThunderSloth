#n [Lichess(username='elib', time_format='blitz'),]: This class constructs a url for the shields.io api that creates a
# custom mark-down badge given text, color, logo and style parameters.
# Eli Bell
# 2023-10-11
from urllib.parse import urlencode, quote


class Shields():
    def __init__(self, text1, color1, text2, color2, logo, style):
        self._title = logo.upper()
        self._base_url = "https://img.shields.io/badge/"
        self._message = quote("-".join(["", text2, color1]))+"?"
        self._query_params = {"style": style,
                              "logo": logo,
                              "label": text1,
                              "labelColor": color1,
                              "color": color2,
                              }
        self._query_string = urlencode(self._query_params)
        self._full_url = f"{self._base_url}{self._message}{self._query_string}"

    @property
    def url(self):
        return self._full_url

    @property
    def badge(self):
        return f"![{self._title}]({self._full_url})"
