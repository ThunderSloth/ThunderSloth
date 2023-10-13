# This script creates a markdown badge using the lichess and shields.io APIs to display my current chess rating
# Eli Bell
# 2023-10-10

import requests
import os

class Lichess():
    def __init__(self, username='elib', time_format='blitz'):
        self._username = username
        self._time_format = time_format
        self._rating = self.rating()
        self._shield = self.shield()
    def rating(self):
        unknown = '%3F'*4 # encoding for 4 question marks "????" 
        try:
            api_key = os.environ['LICHESS_API_KEY']
            endpoint = f"https://lichess.org/api/user/{self._username}"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(endpoint, headers=headers)
            assert response.status_code == 200  # check if the request was successful
            data = response.json()
            perfs = data.get("perfs", {})
            return perfs.get(self._time_format, {}).get("rating", unknown)  # extract rating for the specified time format
        except Exception as e:
            return unknown # return a default value in case of an error
    def shield(self):
       return "https://img.shields.io/badge/-{}%3A%20{}-gray?style=plastic&logo=lichess&label={}&labelColor=black&color=gray".format(self._format, self._rating, self_.username)
    def __repr__(self):
        return ("Lichess(self._'{self._username}', '{self._time_format')")
    def __str__(self):
        return self._shield
           
