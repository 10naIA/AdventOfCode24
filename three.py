# Advent of Code - day 3
# Task: Find all expressions with this pattern: mul(111,111) where the numbers are between 0-9 and can have 1-3 ints.
import re


class Mull:
    def __init__(self):
        self.expressions = []

    def read_file(self, file):
        with open(file, "r") as expressions:
            # Find all expressions and store them in list
            self.expressions = re.findall("mul\(\d{1,3},\d{1,3}\)", expressions.read())

    def multiply_all(self):
        sum = 0
        for item in self.expressions:
            # an item has two separate numbers, so we find these and store them in a list, and multiply them
            divided_list = re.findall("\d{1,3}", item)
            sum += int(divided_list[0]) * int(divided_list[1])
        return f"The result is {sum}"


mull = Mull()
mull.read_file("input3.txt")
print(mull.multiply_all())
