class Euler1:
    def run(self):
        sum = 0

        for number in range(1, 1000):
            if number % 3 == 0:
                sum += number
            elif number % 5 == 0:
                sum += number

        return sum