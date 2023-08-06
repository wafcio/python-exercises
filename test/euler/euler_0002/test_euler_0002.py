from exercises.euler.euler_0002.euler_0002 import Euler2
import unittest

class TestEuler2(unittest.TestCase):
    def test_euler2(self):
        result = Euler2().run()
        assert(result == 4_613_732)

if __name__ == "__main__":
    unittest.main()
