"""
    script: towers-of-hanoi.py
    action: recursive solution to the Towers of Hanoi problem
    author: Kristin Brooks
    date:   07/14/26
"""

def move_disks(num_disks, starting_peg, destination_peg, holding_peg):
    # base case
    if num_disks == 1:
        print(f'{starting_peg} --> {destination_peg}')
    else:
        # now move the remaining disks using the original destination peg as the holding peg
        move_disks(num_disks - 1, starting_peg, holding_peg, destination_peg)
        print(f'{starting_peg} --> {destination_peg}')
        # now move the remaining disks using the original starting peg as the holding peg
        move_disks(num_disks - 1, holding_peg, destination_peg, starting_peg)

def main():
    print('This is the solution to Towers of Hanoi with 4 disks on the starting post (post 1).')
    move_disks(4, 1, 3, 2)

if __name__ == '__main__':
    main()
