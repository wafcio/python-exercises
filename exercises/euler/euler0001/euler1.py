class Euler1:
    total = 0

    def run(self, max_number):
        for number in range(1, max_number):
            if number % 3 == 0:
                self.total += number
            elif number % 5 == 0:
                self.total += number

        return self.total
