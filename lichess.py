# This script creates a markdown badge using the lichess and shields.io APIs to display my current chess rating
# Eli Bell
# 2023-10-10

import requests
import os

class Lichess():
    def __init__(self, username='elib', time_format='blitz'):
        self._username = username
        self._time_format = time_format
        self._unknown = '%3F'*4 # encoding for 4 question marks "????" 
    @property
    def username(self):
        return self._username
    @property
    def time_format(self):
        return self._time_format
    @property
    def rating(self):
        try:
            api_key = os.environ.get['LICHESS_API_KEY']
            assert(api_key, "no key?")
            endpoint = f"https://lichess.org/api/user/{self._username}"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(endpoint, headers=headers)
            assert response.status_code == 200  # check if the request was successful
            data = response.json()
            perfs = data.get("perfs", {})
            return perfs.get(self._time_format, {}).get("rating", self._unknown)  # extract rating for the specified time format
        except Exception as e:
            return self._unknown # return a default value in case of an error
