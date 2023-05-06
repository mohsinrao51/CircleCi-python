import unittest
from main import to_upper


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Umaima"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "Umaima")


if __name__ == '__main__':
    unittest.main()