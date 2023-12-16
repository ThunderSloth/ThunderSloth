import requests
import os


class MT:
    def __init__(self, username="THUNDER-SLOTH", mode="time", mode2="15"):
        self._api_key = self.api_key()
        self._username = username
        self._mode = mode
        self._mode2 = mode2
        self._wpm, self._acc = self.get_pb()

    def api_key(self):
        key = ""
        file_path = "monkeytype_api_key.txt"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_contents = file.read()
            key = file_contents.strip()
        else:
            key = os.environ["MONKEYTYPE_API_KEY"]
        return key

    def get_pb(self):
        try:
            endpoint = "https://api.monkeytype.com/users/personalBests"
            headers = {"Authorization": f"ApeKey {self._api_key}"}
            params = {"mode": self._mode, "mode2": self._mode2}
            response = requests.get(endpoint, params=params, headers=headers)
            # check if the request was successful
            assert response.status_code == 200
            data = response.json()
            record = data.get("data", [[]])[0]
            # extract wpm and acc
            wpm = record.get("wpm", 0)
            acc = record.get("acc", 0)
            return (wpm, acc)
        except Exception as error:
             return (0, 0)

    @property
    def parameters(self):
        return [
            "monkeytype",
            "E2B714",
            f"{self._wpm:.0f} WPM",
            "black",
            "monkeytype",
            "black"
            "https://monkeytype.com/account",
        ]



