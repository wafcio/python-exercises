class Euler6:
    number_1 = 0
    number_2 = 0

    def run(self, number):
        for num in range(1, number+1):
            self.number_1 += pow(num, 2)
            self.number_2 += num

        self.number_2 = pow(self.number_2, 2)

        return self.number_2 - self.number_1
