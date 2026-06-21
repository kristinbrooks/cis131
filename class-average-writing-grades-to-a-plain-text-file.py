"""
    script: class-averge-writing-grades-to-a-plain-text-file.py
    action: allow user to enter any number of grades that are written to a file
    author: Kristin Brooks
    date:   06/21/26
"""

with open('grades.txt', mode='w') as grades_file:
    while True:
        try:
            grade = int(input('Enter grade, -1 to end: ')) # get one grade
            break
        except ValueError:
            print('Invalid input. Please enter an integer.')
    while grade != -1:
        grades_file.write(str(grade) + '\n') # write the current grade to the file
        while True:
            try:
                grade = int(input('Enter grade, -1 to end: ')) # get additional grades
                break
            except ValueError:
                print('Invalid input. Please enter an integer.')
