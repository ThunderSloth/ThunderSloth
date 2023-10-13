# This script creates a markdown badge using the lichess and shields.io APIs to display my current chess rating
# Eli Bell
# 2023-10-10

import requests
import os

class Lichess():
    def __init__(self, username='elib', time_format='blitz'):
        self._api_key = self.api_key()
        self._username = username
        self._time_format = time_format
        self._rating = self.rating()
        self._shield = self.shield()
    def api_key(self):
        key = ''
        file_path = "lichess_api_key.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                file_contents = file.read()
            key = file_contents.strip()
        else:
            key = os.environ['LICHESS_API_KEY']
        return key    
    def rating(self):
        unknown = '%3F'*4 # encoding for 4 question marks "????" 
        try:
            endpoint = f"https://lichess.org/api/user/{self._username}"
            headers = {"Authorization": f"Bearer {self._api_key}"}
            response = requests.get(endpoint, headers=headers)
            assert response.status_code == 200  # check if the request was successful
            data = response.json()
            perfs = data.get("perfs", {})
            return perfs.get(self._time_format, {}).get("rating", unknown)  # extract rating for the specified time format
        except Exception as e:
            print(e)
            return unknown # return a default value in case of an error
    def shield(self):
        return "https://img.shields.io/badge/-{}%3A%20{}-gray?style=plastic&logo=lichess&label={}&labelColor=black&color=gray".format(self._time_format, self._rating, self._username)
    def __repr__(self):
        return ("Lichess(self._'{self._username}', '{self._time_format}')")
    def __str__(self):
        return self._shield
