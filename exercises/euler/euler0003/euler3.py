class Euler3:
    def run(self, n):
        m = 2

        while n > 1:
            if n % m == 0:
                n = n / m
            else:
                m += 1

        return m
