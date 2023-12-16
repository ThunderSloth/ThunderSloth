# This script creates a markdown badge using the lichess and shields.io APIs
# to display my current chess rating
# Eli Bell
# 2023-10-10

import requests
import os


class LC:
    def __init__(self, username="elib", time_format="blitz"):
        self._api_key = self.api_key()
        self._username = username
        self._time_format = time_format
        self._rating = self.get_rating()

    def api_key(self):
        key = ""
        file_path = "lichess_api_key.txt"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_contents = file.read()
            key = file_contents.strip()
        else:
            key = os.environ["LICHESS_API_KEY"]
        return key

    def get_rating(self):
        try:
            endpoint = f"https://lichess.org/api/user/{self._username}"
            headers = {"Authorization": f"Bearer {self._api_key}"}
            response = requests.get(endpoint, headers=headers)
            # check if the request was successful
            assert response.status_code == 200
            data = response.json()
            perfs = data.get("perfs", {})
            # extract rating for the specified time format
            return perfs.get(self._time_format, {}).get("rating", "????")
        except Exception as error:
            return error

    @property
    def parameters(self):
        return [
            "lichess",
            "333333",
            f"{self._time_format}: {self._rating}",
            "D3D3D3",
            "lichess",
            "white",
            "https://lichess.org/@/" + self._username,
        ]
