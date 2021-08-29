import unittest
from main import NumberFormatter


class TestNumberFormatter(unittest.TestCase):

    def test_number_formatter(self):
        self.assertEqual(NumberFormatter().parse_int('124'), 124)
        self.assertEqual(NumberFormatter().parse_int('-123'), -123)
        self.assertEqual(NumberFormatter().parse_int('+123'), 123)
        self.assertEqual(NumberFormatter().parse_int('12/3'), 'Wrong symbol in string')
        self.assertEqual(NumberFormatter().parse_int(''), 'The argument cannot be an empty string')
        self.assertEqual(NumberFormatter().parse_int(12), 'The argument must only be a string')
