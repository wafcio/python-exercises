from exercises.utils.prime import is_prime

class Euler7:
    index = 0
    number = 2

    def run(self, max_number):
        while True:
            if is_prime(self.number):
                self.index += 1

            if self.index == max_number:
                break

            self.number += 1

        return self.number
