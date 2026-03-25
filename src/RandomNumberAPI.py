import requests

class RandomNumberAPI:

    BASE_URL = "https://www.randomnumberapi.com/api/v1.0/random"

    def get_number(self, min_value, max_value, count_value):
        params = {
            "min": min_value,
            "max": max_value,
            "count": count_value
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")

        data = response.json()  # devuelve una lista
        return data