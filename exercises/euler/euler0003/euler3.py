class Euler3:
    factor = 2

    def run(self, number):
        while number > 1:
            if number % self.factor == 0:
                number = number / self.factor
            else:
                self.factor += 1

        return self.factor
