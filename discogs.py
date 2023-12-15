
#/users/{username}/collection/value
#https://api.discogs.com/
import requests
import json
import os


class DC:
    def __init__(self, username="THUNDER-SLOTH"):
        self._api_key = self.api_key()
        self._username = username
        self._worth = self.get_worth()

    def api_key(self):
        key = ""
        file_path = "discogs_api_key.txt"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_contents = file.read()
            key = file_contents.strip()
        else:
            key = os.environ["DISCOGS_API_KEY"]
        return key

    def get_worth(self):
        try:
            endpoint = f"https://api.discogs.com/users/{self._username}/collection/value"
            headers = {"Authorization": f"Discogs token={self._api_key}"}
            response = requests.get(endpoint, headers=headers)
            # check if the request was successful
            assert response.status_code == 200
            data = response.json()
            worth = data.get("maximum", 0)
            return float(worth[1:].replace(",", ""))
        except Exception as error:
            return error

    @property
    def parameters(self):
        return [
            f"{self._username}",
            "#333333",
            f"${(self._worth/1000):.1f}k",
            "#000000",
            "discogs",
        ]

