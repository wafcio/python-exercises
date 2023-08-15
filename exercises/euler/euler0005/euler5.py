from collections import Counter
import numpy

class Euler5:
    def run(self, n):
        factors = []

        for number in range(2, n):
            current_factors = self.prime_factors(number)
            missing_factors = self.list_difference(current_factors, factors)
            factors += missing_factors

        return numpy.prod(factors)

    def list_difference(self, a, b):
        diff = Counter(a) - Counter(b)
        return list(diff.elements())

    def prime_factors(self, number):
        m = 2
        numbers = []

        while number > 1:
            if number % m == 0:
                number = number / m
                numbers.append(m)
            else:
                m += 1

        return numbers
