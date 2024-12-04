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

# List of reports
reports = [
    [7, 6, 4, 2, 1], 
    [1, 2, 7, 8, 9], 
    [9, 7, 6, 2, 1], 
    [1, 3, 2, 4, 5], 
    [8, 6, 4, 4, 1], 
    [1, 3, 6, 7, 9]
]

safe_count = 0
for report in reports:
    if is_safe_report(report) or can_be_safe_by_removing_one(report):
        safe_count += 1

print("Number of safe reports:", safe_count)
