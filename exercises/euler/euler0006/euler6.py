class Euler6:
    def run(self, n):
        num1 = 0
        num2 = 0

        for m in range(1, n+1):
            num1 += pow(m, 2)
            num2 += m

        num2 = pow(num2, 2)

        return num2 - num1
