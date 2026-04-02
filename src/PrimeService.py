from IsPrime import IsPrime

class PrimeService:

    def __init__(self, api):
        self.api = api

    def is_random_number_prime(self):
        # 1. Obtenemos el número de la API
        number = self.api.get_number(1, 100, 1)
        
        # 2. Llamamos a la clase -> método estático -> pasamos el número
        # ESTA ES LA LÍNEA CLAVE:
        result = IsPrime.is_prime(number)
        
        return number, result