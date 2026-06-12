"""
    script: miles-per-gallon.py
    action: Develop a sentinel-controlled-repetition script that prompts the user to input the miles driven and gallons
     used for each tankful. The script should calculate and display the miles per gallon obtained for each tankful.
     After processing all input information, the script should calculate and display the combined miles per gallon
     obtained for all tankfuls (that is, total miles driven divided by total gallons used).
    author: Kristin Brooks
    date:   06/04/26
"""

# initialize variables
miles = 0
total_gallons = 0
total_miles = 0

# get first input to enter loop or not
gallons = float(input('Enter the gallons used (-1 to end): '))

# loop to get info from user and present them with results
while gallons != -1:
    miles = float(input('Enter the miles driven: '))
    total_gallons += gallons
    total_miles += miles
    print('The miles/gallon for this tank was', miles/gallons)
    gallons = float(input('Enter the gallons used (-1 to end): '))

# display final results
if total_gallons != 0:
    print('The overall average miles/gallon was', total_miles/total_gallons)
else:
    print('No tanks were entered.')
    