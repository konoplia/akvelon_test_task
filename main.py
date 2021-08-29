class NumberFormatter:

    ALLOWED_SYMBOLS = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]

    def __init__(self):
        self.unicode_of_zero = ord('0')

    def parse_int(self, number_as_string):

        if type(number_as_string) != str:
            return 'The argument must only be a string'

        length_string = len(number_as_string)
        result = 0

        if length_string == 0:
            return 'The argument cannot be an empty string'
        for symbol in range(length_string):
            if symbol == 0 and (number_as_string[symbol] == '-' or
                                number_as_string[symbol] == '+'):
                length_string -= 1
                continue
            if number_as_string[symbol] not in self.ALLOWED_SYMBOLS:
                return 'Wrong symbol in string'
            number_from_unicode = ord(number_as_string[symbol]) - self.unicode_of_zero
            result += number_from_unicode * (10 ** (length_string - 1))
            length_string -= 1
        if number_as_string[0] == '-':
            result *= -1
        return result


n = NumberFormatter()
# print(n.parse_int(''))
# print(n.parse_int('123-23'))
# print(n.parse_int('+123-23'))
# print(n.parse_int('123'))
print(n.parse_int('-123'))
# print(n.parse_int('+213'))
# print(n.parse_int('+21-3'))
# print(n.parse_int('dhfjh'))
# print(n.parse_int('123445dhfjh'))
# print(n.parse_int(223))
# print(n.parse_int([1, 2]))
# print(n.parse_int(''))
