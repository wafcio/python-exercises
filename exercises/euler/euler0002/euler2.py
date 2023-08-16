class Euler2:
    number_1 = 1
    number_2 = 2
    total = 2
    value = -1

    def run(self, number):
        while self.value < number:
            self.value = self.number_1 + self.number_2

            if self.value % 2 == 0:
                self.total += self.value

            self.number_1 = self.number_2
            self.number_2 = self.value

        return self.total
