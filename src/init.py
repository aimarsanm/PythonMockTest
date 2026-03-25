import RandomNumberAPI
from PrimeService import PrimeService


api = RandomNumberAPI()
service = PrimeService(api)

number, result = service.is_random_number_prime()

print(f"{number} es primo: {result}")