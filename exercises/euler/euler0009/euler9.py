import math

class Euler9:
    def run(self, n):
        a = 1
        b = 2

        while True:
            pow_a = pow(a, 2)
            pow_b = pow(b, 2)
            c = math.sqrt(pow_a + pow_b)
            sum = a + b + c

            if a + b > n:
                break

            if sum < n:
                b += 1

            if sum > n:
                a += 1
                b = a + 1

            if sum == n:
                return a * b * c

        return 0
