import math

class Euler20:
    total = 0

    def run(self, number):
        result = math.factorial(number)
        result_str = str(result)

        for _i, char in enumerate(result_str):
            self.total += int(char)

        return self.total
