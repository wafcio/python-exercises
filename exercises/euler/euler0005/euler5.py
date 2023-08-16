from collections import Counter
import numpy

class Euler5:
    factors = []

    def run(self, max_number):
        for number in range(2, max_number):
            current_factors = Euler5.prime_factors(number)
            missing_factors = Euler5.list_difference(current_factors, self.factors)
            self.factors += missing_factors

        return numpy.prod(self.factors)

    @staticmethod
    def list_difference(list_a, list_b):
        diff = Counter(list_a) - Counter(list_b)
        return list(diff.elements())

    @staticmethod
    def prime_factors(number):
        factor = 2
        numbers = []

        while number > 1:
            if number % factor == 0:
                number = number / factor
                numbers.append(factor)
            else:
                factor += 1

        return numbers
