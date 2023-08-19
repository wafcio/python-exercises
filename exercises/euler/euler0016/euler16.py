class Euler16:
    total = 0

    def run(self, power):
        number = pow(2, power)
        number_str = str(number)

        for _i, char in enumerate(number_str):
            self.total += int(char)

        return self.total
