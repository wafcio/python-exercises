import math

class Euler7:
    def run(self, n):
        i = 0
        number = 2

        while True:
            if self.is_prime(number):
                i += 1

            if i == n:
                break

            number += 1

        return number

    def is_prime(self, number):
        sq = int(math.sqrt(number))

        for factor in range(2, sq+1):
            if number % factor == 0:
                return False

        return True
