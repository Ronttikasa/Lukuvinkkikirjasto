# pylint: disable=invalid-name
import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, kayttajatunnus, salasana):
        data = {
            "tunnus": kayttajatunnus,
            "salasana": salasana,
        }

        requests.post(f"{self._base_url}/rekisteroidu", data=data)
