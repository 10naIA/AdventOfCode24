# Advent of Code - day 1.
# Task a: Compare two and two numbers from two lists, from smallest to biggest, and calculate their difference. In the end,
# calculate the total difference.
# Task b: Calculate how many times each nr in list 1 occur in list 2, and find the total similarity score.

class IdNumbers:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.tot_distance = 0
        self.tot_score = 0

    def read_input(self, file):
        with open(file, "r") as ids:
            for line in ids:
                # Input-file looks like this: 11  12, so we split on whitespace, and put them in two lists
                divided = line.split()
                self.list1.append(int(divided[0]))
                self.list2.append(int(divided[1]))

    def calc_distances(self):
        # Sort lists from smallest to biggest
        self.list1.sort()
        self.list2.sort()
        for nr in range(0, len(self.list1)):
            diff = abs(self.list1[nr] - self.list2[nr])
            # Add the difference to the total sum
            self.tot_distance += diff

    def get_tot_distance(self):
        return f"Total distance: {self.tot_distance}"

    def calc_similarity_score(self):
        for nr in self.list1:
            # Count how many times each nr in list1 occur in list2. Add the product to total score
            amount = self.list2.count(nr)
            self.tot_score += amount * nr

    def get_similarity_score(self):
        return f"The similarity score is: {self.tot_score}"


def distances():
    numbers = IdNumbers()
    numbers.read_input("input1.txt")
    numbers.calc_distances()
    print(numbers.get_tot_distance())


def similarity_score():
    numbers = IdNumbers()
    numbers.read_input("input1.txt")
    numbers.calc_similarity_score()
    print(numbers.get_similarity_score())


distances()
similarity_score()
