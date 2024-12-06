# Advent of Code - day 1.
# Task: Compare two and two numbers from two lists, from smallest to biggest, and calculate their difference. In the end,
# calculate the total difference.

class IdNumbers:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.sum = 0

    def read_input(self, file):
        ids = open(file, "r")
        for line in ids:
            # Input-file looks like this: 11  12, so we split on whitespace, and put them in two lists
            divided = line.split()
            self.list1.append(int(divided[0]))
            self.list2.append(int(divided[1]))
        ids.close()

    def calc_distances(self):
        # Sort lists from smallest to biggest
        self.list1.sort()
        self.list2.sort()
        for nr in range(0, len(self.list1)):
            diff = abs(self.list1[nr] - self.list2[nr])
            # Add the difference to the total sum
            self.sum += diff

    def get_tot_distance(self):
        print("Total distance: ", self.sum)


def calc_all_distances():
    numbers = IdNumbers()
    numbers.read_input("input.txt")
    numbers.calc_distances()
    numbers.get_tot_distance()


calc_all_distances()
