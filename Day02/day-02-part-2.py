def is_safe_report(report):
    increasing = decreasing = True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
    return increasing or decreasing

def can_be_safe_by_removing_one(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False

def read_reports_from_file(filename):
    reports = []
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            reports.append(report)
    return reports


filename = 'D:/Advent-of-code-2024/Advent-of-Code-2024/Day02/input.txt'  
reports = read_reports_from_file(filename)

safe_count = 0
for report in reports:
    if is_safe_report(report) or can_be_safe_by_removing_one(report):
        safe_count += 1

print("Number of safe reports:", safe_count)
