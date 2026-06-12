"""
    While exercising, you can use a heart-rate monitor to see that your heart rate stays within a safe range suggested by
    your doctors and trainers. According to the American Heart Association (AHA) (http://bit.ly/AHATargetHeartRates), the
    formula for calculating your maximum heart rate in beats per minute is 220 minus your age in years. Your target heart
    rate is 50–85% of your maximum heart rate. Write a script that prompts for and inputs the user’s age and calculates
    and displays the user’s maximum heart rate and the range of the user’s target heart rate.
"""

# prompt the user for their age
age = int(input('Please enter your age: '))

# calculate maximum heart rate
max_rate = 220 - age

# calculate target heart rate range
range_min = max_rate * 0.5
range_max = max_rate * 0.85

# print results
print('Your maximum heart rate is:', max_rate)
print('Your target heart rate is between', range_min, 'and', range_max)
