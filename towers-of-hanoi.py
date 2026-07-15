"""
    script: towers-of-hanoi.py
    action: recursive solution to the Towers of Hanoi problem
    author: Kristin Brooks
    date:   07/14/26
"""

def move_disks(num_disks, starting_peg, destination_peg, holding_peg):
    if num_disks == 1:
        print(f'{starting_peg} --> {destination_peg}')
    else:
        move_disks(num_disks - 1, starting_peg, holding_peg, destination_peg)
        print(f'{starting_peg} --> {destination_peg}')
        move_disks(num_disks - 1, holding_peg, destination_peg, starting_peg)

def main():
    move_disks(3, 1, 3, 2)

if __name__ == '__main__':
    main()
