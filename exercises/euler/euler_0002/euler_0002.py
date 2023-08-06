class Euler2:
    def run(self):
        num1 = 1
        num2 = 2
        sum = num2
        value = -1

        while value < 4_000_000:
            value = num1 + num2

            if value % 2 == 0:
                sum += value

            num1 = num2
            num2 = value

        return sum
