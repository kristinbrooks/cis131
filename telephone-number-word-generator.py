"""
    script: telephone-number-word-generator.py
    action: gets a 7-digit phone number and generates every possible 7-letter word combination corresponding to that number
    author: Kristin Brooks
    date:   06/12/26
"""

keypad = {
    '2' : ['A', 'B', 'C'],
    '3' : ['D', 'E', 'F'],
    '4' : ['G', 'H', 'I'],
    '5' : ['J', 'K', 'L'],
    '6' : ['M', 'N', 'O'],
    '7' : ['P', 'R', 'S'],
    '8' : ['T', 'U', 'V'],
    '9' : ['W', 'X', 'Y']
}
possible_words = []

# get the phone number from the user
phone_number = input('Enter a 7 digit phone number: ')
phone_number = phone_number.replace('-', '')

# validation that the user entered an appropriate number
while '0' in phone_number or '1' in phone_number or len(phone_number) != 7 or not phone_number.isdigit():
    phone_number = input("Enter a 7 digit phone number with no 0's or 1's: ")
    phone_number = phone_number.replace('-', '')

# loop through all the possible letter combinations
for letter1 in keypad[phone_number[0]]:
    for letter2 in keypad[phone_number[1]]:
        for letter3 in keypad[phone_number[2]]:
            for letter4 in keypad[phone_number[3]]:
                for letter5 in keypad[phone_number[4]]:
                    for letter6 in keypad[phone_number[5]]:
                        for letter7 in keypad[phone_number[6]]:
                            possible_words.append(letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7)

# display the possible words
print(f'There are {len(possible_words)} possible words for this phone number.')
print('Here are all the possibilities:')
for index, word in enumerate(possible_words):
    print(word, end=' ')
    if (index + 1) % 9 == 0:
        print()
