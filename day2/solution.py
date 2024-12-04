reports = []
with open('input.txt', 'r') as file:
    for line in file:
        reports.append(line.split())

"""
Part 1

    Condition 1 logic: iterate through reports and check if necessary conditions are met
    if we reach the end of a report and safe_report boolean is still True
    we increment our safe report counter
"""
safe_report_counter = 0

for report in reports:
    safe_report = True

    for index, level in enumerate(report):
        if safe_report is False:
            break
        if safe_report is True and index == len(report) - 1:
            safe_report_counter += 1
            break

        level_difference = abs(int(level) - int(report[index + 1]))

        if level_difference == 0 or level_difference > 3:
            safe_report = False
            break

        """
            Condition 2 logic: check if report is consistently increasing or decreasing
            a report is deemed to be increasing or decreasing by comparing the first two levels. 
            if subsequent levels are found to change, then the safe_report boolean is set to False,
            which will cause a break to the next report
        """
        if index == 0:
            if int(level) < int(report[index + 1]):
                report_is = "increasing"
            else:
                report_is = "decreasing"
        elif int(level) < int(report[index + 1]) and report_is != "increasing":
            safe_report = False
            can_report_become_safe(report)
            break
        elif int(level) > int(report[index + 1]) and report_is != "decreasing":
            safe_report = False
            can_report_become_safe(report)
            break

print(f"\n*** Total safe reports: {safe_report_counter} ***")


""" 
Part 2 
    If a report is unsafe, can it be made safe by removing a level? 
    Reports can only tolerate a single bad level and no more 
"""
def can_report_become_safe(report):
    print(f"A bad report has been found: {report}")

