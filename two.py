# Advent of Code - day 2
# Task: Find reports that only have increasing/decreasing numbers, and where the numbers adjacent to each other have a difference
# between 1 and 3.

class SafeReports:
    def __init__(self):
        self.reports = []

    def read_input(self, file):
        with open(file, "r") as ids:
            for line in ids:
                # Turn elements from string to int
                divided = line.split()
                int_divided = list(map(int, divided))
                self.compare_levels(int_divided)
        ids.close()

    def compare_levels(self, report):
        # Check if report has only increasing/decreasing numbers
        if all(report[i] > report[i+1] for i in range(0, len(report) - 1)) or \
                all(report[i] < report[i+1] for i in range(0, len(report) - 1)):
            # Check if the levels(numbers) differences are between 1 & 3
            if all(1 <= (abs(report[j] - report[j+1])) <= 3 for j in range(0, len(report) - 1)):
                self.reports.append(report)

    def get_nr_safe_reports(self):
        return f"There are {len(self.reports)} safe reports."


def get_tot_safe_reports():
    safe_reports = SafeReports()
    safe_reports.read_input("input2.txt")
    print(safe_reports.get_nr_safe_reports())


get_tot_safe_reports()
