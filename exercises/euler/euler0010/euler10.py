from exercises.utils.prime import is_prime

class Euler10:
    total = 0

    def run(self, max_number):
        for number in range(2, max_number):
            if is_prime(number):
                self.total += number

        return self.total
