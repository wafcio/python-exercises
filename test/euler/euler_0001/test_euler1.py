from exercises.euler.euler_0001.euler1 import Euler1
import unittest

class TestEuler1(unittest.TestCase):
    def test_euler1(self):
        result = Euler1().run()
        assert(result == 233_168)

if __name__ == "__main__":
    unittest.main()
