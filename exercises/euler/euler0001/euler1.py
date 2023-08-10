class Euler1:
    def run(self, n):
        sum = 0

        for number in range(1, n):
            if number % 3 == 0:
                sum += number
            elif number % 5 == 0:
                sum += number

        return sum
