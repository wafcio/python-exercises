import datetime

class Euler19:
    sundays = 0

    def run(self):
        for year in range(1901, 2001):
            for month in range(1, 13):
                if datetime.date(year, month, 1).weekday() == 6:
                    self.sundays += 1

        return self.sundays
