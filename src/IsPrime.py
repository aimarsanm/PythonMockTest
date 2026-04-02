from src.Exception import MissingArgumentException, Only1ArgumentException, NoPositiveNumberException

class IsPrime:
    
    @staticmethod
    def is_prime(number): # Mantenemos el nombre exacto
        # Validamos el argumento directamente
        if number is None:
            raise MissingArgumentException()
        
        try:
            num = int(float(number))
            if num <= 0:
                raise NoPositiveNumberException()
            if num == 1:
                return False
            
            # Lógica de número primo
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
            
        except (ValueError, TypeError, OverflowError):
            raise NoPositiveNumberException()