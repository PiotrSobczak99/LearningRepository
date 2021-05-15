import random


def circle_or_cross():
    while True:
        decision = input("Player, do you want to play as cross or circle?: ")
        if decision.lower() == "circle":
            return "O"  
        elif decision.lower() == "cross":  
            return "X"
        else:
            print("You have to choose between circle or cross")

def does_player_start():
    while True:
        decision = input("Do you want to go first? Type yes or no: ")
        if decision.lower() == "yes":
            return True
        elif decision.lower() == "no":
            return False
        else:
            print("You have to type 'yes' or 'no'")


def print_instruction_board():
    # print("0 | 1 | 2")
    # print("---------")
    # print("3 | 4 | 5")
    # print("---------")
    # print("6 | 7 | 8\n")
    pass



def print_current_board(fields_array):
    print("{} | {} | {}".format(fields_array[0],fields_array[1],fields_array[2]))
    print("---------")
    print("{} | {} | {}".format(fields_array[3],fields_array[4],fields_array[5]))
    print("---------")
    print("{} | {} | {}\n".format(fields_array[6],fields_array[7],fields_array[8]))

def get_player_move():
    print_instruction_board()
    while True:
        player_move = input("choose a number from 0 to 8 where you want to move: ")
        player_move = int(player_move)
        if player_move <= 8 and player_move >= 0:
            return player_move
        else:
            print("You have choosen wrong number. Choose a number from 0 to 8: ")

def get_ai_move(fields_array):
    while True:
        random_number = random.randint(0,8)
        if fields_array[random_number] == " ":
            return random_number
    
        
def ai_symbol_set(user_symbol):
    if user_symbol == "X":
        return "O"
    else:
        return "X"
        
def winning_conditions(fields_array):
    global round_counter
    #print(fields_array)
    if fields_array[0] == "X" and fields_array[1] == "X" and fields_array[2] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter
    elif fields_array[3] == "X" and fields_array[4] == "X" and fields_array[5] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter  
    elif fields_array[6] == "X" and fields_array[7] == "X" and fields_array[8] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter
    elif fields_array[0] == "X" and fields_array[3] == "X" and fields_array[6] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter
    elif fields_array[1] == "X" and fields_array[4] == "X" and fields_array[7] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter
    elif fields_array[2] == "X" and fields_array[5] == "X" and fields_array[8] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter
    elif fields_array[0] == "X" and fields_array[4] == "X" and fields_array[8] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter
    elif fields_array[2] == "X" and fields_array[4] == "X" and fields_array[7] == "X":
        round_counter = 10
        return print("Contgratulations Player X won"), round_counter
    elif fields_array[0] == "O" and fields_array[1] == "O" and fields_array[2] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter
    elif fields_array[3] == "O" and fields_array[4] == "O" and fields_array[5] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter  
    elif fields_array[6] == "O" and fields_array[7] == "O" and fields_array[8] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter
    elif fields_array[0] == "O" and fields_array[3] == "O" and fields_array[6] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter
    elif fields_array[1] == "O" and fields_array[4] == "O" and fields_array[7] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter
    elif fields_array[2] == "O" and fields_array[5] == "O" and fields_array[8] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter
    elif fields_array[0] == "O" and fields_array[4] == "O" and fields_array[8] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter
    elif fields_array[2] == "O" and fields_array[4] == "O" and fields_array[7] == "O":
        round_counter = 10
        return print("Contgratulations Player O won"), round_counter
    elif round_counter == 9:
        print("Its a draw")

def round(fields_array, user_symbol):
    global round_counter
    print_current_board(fields_array)    
    
    if round_counter < 10:
        while True:
            player_move = get_player_move()
            if fields_array[player_move] == " ":
                fields_array[player_move] = user_symbol
                round_counter = round_counter + 1
                break
            elif fields_array[player_move] == "O" or fields_array[player_move] == "X":
                print("this square is taken, please choose another one ")
        
        
        winning_conditions(fields_array)
        print_current_board(fields_array)
        
    if round_counter < 10:    
        while True:
            ai_move = get_ai_move(fields_array)
            fields_array[ai_move] = ai_symbol_set(user_symbol)
            round_counter = round_counter + 1
            break
        

    try:    
        print("AI moved to square {}:\n".format(ai_move))        
    except:
        pass
    
    winning_conditions(fields_array)
    print_current_board(fields_array)
    



if __name__ == '__main__':
    
    fields_array=[" "," "," "," "," "," "," "," "," "]
    user_symbol = circle_or_cross()
    player_starts = does_player_start()
    ai_move = get_ai_move(fields_array)
    
    round_counter = 0

    if player_starts:
        string = "does"
    else:
        string = "doesn't"
    
    print("Player {} start and his symbol is {}".format(string, user_symbol))


    while round_counter < 10:
        round(fields_array, user_symbol)

    
