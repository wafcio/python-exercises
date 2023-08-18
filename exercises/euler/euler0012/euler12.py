import math

class Euler12:
    triangle_number_p = 0
    triangle_number = 0
    divisor_count = 0

    def run(self, limit_divisor_count):
        while self.divisor_count <= limit_divisor_count:
            self.triangle_number_p += 1
            self.triangle_number += self.triangle_number_p
            divisors = []
            for factor in range(1, int(math.sqrt(self.triangle_number))):
                if self.triangle_number % factor == 0:
                    divisors.append(factor)
            self.divisor_count = len(divisors) * 2

        return self.triangle_number
