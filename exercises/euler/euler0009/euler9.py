import math

class Euler9:
    number_a = 1
    number_b = 2

    def run(self, number):
        while True:
            pow_a = pow(self.number_a, 2)
            pow_b = pow(self.number_b, 2)
            number_c = math.sqrt(pow_a + pow_b)
            total = self.number_a + self.number_b + number_c

            if self.number_a + self.number_b > number:
                break

            if total < number:
                self.number_b += 1

            if total > number:
                self.number_a += 1
                self.number_b = self.number_a + 1

            if total == number:
                return self.number_a * self.number_b * number_c

        return 0
