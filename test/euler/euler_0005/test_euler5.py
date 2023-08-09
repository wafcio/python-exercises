from exercises.euler.euler_0005.euler5 import Euler5
import unittest

class TestEuler5(unittest.TestCase):
    def test_euler5_first_example(self):
        result = Euler5().run(10)
        assert(result == 2520)

    def test_euler5_second_example(self):
        result = Euler5().run(20)
        assert(result == 232792560)

if __name__ == "__main__":
    unittest.main()
