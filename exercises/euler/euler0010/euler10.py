import math

class Euler10:
    def run(self, n):
        sum = 0
        for number in range(2, n):
            if self.is_prime(number):
                sum += number

        return sum

    def is_prime(self, number):
        sq = int(math.sqrt(number))

        for factor in range(2, sq+1):
            if number % factor == 0:
                return False

        return True
