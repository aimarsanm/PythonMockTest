from src.IsPrime import IsPrime

class PrimeService:

    def __init__(self, api):
        self.api = api

    def is_random_number_prime(self):
        number = self.api.get_number(1,10,1)
        return number, IsPrime(number)