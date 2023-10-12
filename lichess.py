# This script creates a markdown badge using the lichess and shields.io APIs to display my current chess rating
# Eli Bell
# 2023-10-10

import requests
import json
import os

class Lichess():
    def __init__(self, username='elib', time_format='blitz'):
        self.username = username
        self.time_format = time_format
        self._rating = '????'
    @property
    def username(self):
        return self.username
    @property
    def time_format(self):
        return self.time_format
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self):
        try:
            api_key =  os.environ['LICHESS_API_KEY']
            endpoint = "https://lichess.org/api/user/"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(f"{endpoint}{USER}", headers=headers)
            assert(response.status_code == 200) # check id successful 
            data = response.json()
            perfs = data.get("perfs", {})
            self._rating = perfs[FORMAT]['rating'] # extract rating for specified time-format
        except:
            pass
