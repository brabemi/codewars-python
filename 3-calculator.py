from decimal import Decimal
import re

class Calculator(object):
    def evaluate(self, string):
        # parts = ['Decimal(' + part + ')' if re.fullmatch(r'\d+(\.\d+)?', part) else part for part in string.split(' ')]
        parts = map(lambda p: "Decimal('" + p + "')" if re.fullmatch(r'\d+(\.\d+)?', p) else p , string.split(' '))
        code = ' '.join(parts)
        print(code)

        return float(eval(code))


print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))
print(Calculator().evaluate("1.1 * 2.2 * 3.3"))
