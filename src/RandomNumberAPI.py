import requests

class RandomNumberAPI:

    def get_number(self, min_value, max_value, count_value):
       
        response = requests.get(f"https://www.randomnumberapi.com/api/v1.0/random?min={min_value}&max={max_value}&count={count_value}")

        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")

        data = response.json()  # devuelve una lista
        return data[0]