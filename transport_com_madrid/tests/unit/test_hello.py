import unittest
from transport_com_madrid import hello

class TestHelloWorld(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(True, True, 'I leave Python!')

if __name__ == '__main__':
    unittest.main()

