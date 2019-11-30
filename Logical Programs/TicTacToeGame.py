"""Build Tic-Tac-Toe Game"""
import random


def show_values():              # fn shows current state of the game in 3*3 matrix
    for i in range(3):
        for j in range(3):
            print(f'{positions[i][j]}:{values[i][j]}', end=' ')
        print()
    print()


def fill_value(pos, usr_sign):      # fn fills given position with user's input/ computers's input
    for i in range(3):
        for j in range(3):
            if positions[i][j] == pos:
                values[i][j] = usr_sign


def check_position(pos):            # fn checks whether given position is vacant or not
    for i in range(3):
        for j in range(3):
            if positions[i][j] == pos:
                if values[i][j] != ' ':
                    return f'{pos} already filled'

    return False


def check_end(sign):               # fn checks whether game has been won by user or computer
    for i in range(3):                     # it takes user's sign or computer's sign after his/it's turn
        for j in range(3):
            if values[i][j] != sign:
                break
        else:
            return True                              # total 8 conditions to be checked for winning conditions

    for j in range(3):
        for i in range(3):
            if values[i][j] != sign:
                break
        else:
            return True

    for i in range(3):
        if values[i][i] != sign:
            break
    else:
        return True

    if values[0][2] == values[2][0] == values[1][1] == sign:
        return True


# Program starts executing from here


pos = 1
positions = [[0 for j in range(3)] for i in range(3)]           # shows positions of matrix in game
values = [[' ' for j in range(3)] for i in range(3)]            # accepts signs of players for given position

for i in range(3):
    for j in range(3):
        positions[i][j] = pos
        pos += 1

show_values()                                   # shows blank matrix with positions
print("Let's play tic tac toe game")
while True:
    try:
        usr_sign = input("Choose 'X' or  'O'  sign:")      # defining sign for players user and computer
        assert usr_sign in 'oOxX'
        usr_sign = usr_sign.upper()
        print(usr_sign)
        break
    except AssertionError:
        print('Invalid sign declaration')

if usr_sign == 'X':
    comp_sign = 'O'
else:
    comp_sign = 'X'

s = random.randint(1, 10)
comp_pos = [i for i in range(1, 10)]                # computer uses values from this list for playing it's turn
count = 0                                       # counts total turns in the game

while True:
    while True:                       # checking whether given position is appropriate to move forward
        try:
            pos = int(input('Enter position to fill:'))
            assert 0 < pos < 10
            if not check_position(pos):
                break
            else:
                print(check_position(pos))
        except(ValueError, AssertionError):
            print('Only integers in range 1-9 are allowed')

    fill_value(pos, usr_sign)                              # fills user's sign in values's matrix
    show_values()                                  # after each turn check whether game ends or not
    sign = usr_sign
    check_end(sign)
    if check_end(sign):
        print('You won')
        break
    count += 1
    if count == 9:                                 # condition for tie
        print('Game tie')
        break

    input()
    comp_pos.remove(pos)                          # removes filled positions for computer
    random.seed(s)
    pos = random.choice(comp_pos)
    fill_value(pos, comp_sign)                  # fills position for computer's turn
    random.seed(s)
    comp_pos.remove(pos)
    s += 1
    show_values()
    sign = comp_sign                           # after each turn  checks game ends or not
    if check_end(sign):
        print('comp won')
        break
    count += 1

