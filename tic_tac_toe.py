from random import randint

print("TIC-TAC-TOE")
print("------------")

def show_board(): #display board
    zero = 'X' if x_state[0] else ('O' if o_state[0] else 0) 
    one = 'X' if x_state[1] else ("O" if o_state[1] else 1) 
    two = 'X' if x_state[2] else ("O" if o_state[2] else 2) 
    three = 'X' if x_state[3] else ("O" if o_state[3] else 3) 
    four = 'X' if x_state[4] else ("O" if o_state[4] else 4)
    five = 'X' if x_state[5] else ("O" if o_state[5] else 5)
    six = 'X' if x_state[6] else ("O" if o_state[6] else 6) 
    seven = 'X' if x_state[7] else ("O" if o_state[7] else 7)  
    eight = 'X' if x_state[8] else ("O" if o_state[8] else 8)  

    print(f" {zero} | {one} | {two}")
    print(f"---|---|---")
    print(f" {three} | {four} | {five}")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight}")

def first_turn(): #first person to take a turn (1 for 'X' and 0 for 'O')
    turn = randint(0, 1)
    return turn

def sum(a, b, c): #sum for combination to win for player
    return a + b + c

def win_check(x_state, o_state): #function to identify the winner
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
    for combination in win:
        if sum(x_state[combination[0]], x_state[combination[1]], x_state[combination[2]]) == 3:
            return 1
        elif sum(o_state[combination[0]], o_state[combination[1]], o_state[combination[2]]) == 3:
            return 0
    return -1

x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
o_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

turn = first_turn()
count = 0
while True:
    show_board()
    if turn == 1:
        print (" ")
        print("X's Turn:")
        while True:
            value = int(input("Enter the position you want to mark (0-8): "))
            if x_state[value] == 1 or o_state[value] == 1:
                print("Invalid Option! That position is already marked.")
            else:
                x_state[value] = 1
                count += 1
                break
        
    else:
        print (" ")
        print("O's Turn: ")
        while True:
            value = int(input("Enter the position you want to mark (0-8): "))
            if x_state[value] == 1 or o_state[value] == 1:
                print("Invalid Option! That position is already marked.")
            else:
                o_state[value] = 1
                count += 1
                break

    winner = win_check(x_state, o_state)
    if winner == 1:
        print("---X wins!---")
        break
    elif winner == 0:
        print("---O wins!---")
        break
    elif count == 9:
        print("---Match Draw!---")
        break

    turn = 1 - turn


