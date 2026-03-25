from src.Exception import MissingArgumentException, Only1ArgumentException, NoPositiveNumberException

class IsPrime:
    @staticmethod
    def is_prime(args):
        if args is None or len(args) == 0:
            raise MissingArgumentException()
        elif len(args) > 1:
            raise Only1ArgumentException()
        else:
            try:
                num_f = float(args[0])
                num = int(num_f) # Igual que cast de float a int en Java
                if num <= 0:
                    raise NoPositiveNumberException()
                if num == 1:
                    return False
            except (ValueError, TypeError, OverflowError):
                raise NoPositiveNumberException()
            for i in range(2, num):
                if num % i == 0:
                    return False
        return True
