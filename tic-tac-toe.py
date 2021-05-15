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
    print("Use indices as shown below:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")
    print()


def print_current_board(fields_array):
    print("{} | {} | {}".format(fields_array[0], fields_array[1], fields_array[2]))
    print("---------")
    print("{} | {} | {}".format(fields_array[3], fields_array[4], fields_array[5]))
    print("---------")
    print("{} | {} | {}".format(fields_array[6], fields_array[7], fields_array[8]))
    print()

def get_player_move():
    while True:
        player_move = input("Choose a number from 0 to 8 where you want to move: ")
        try:
            player_move = int(player_move)
        except ValueError:
            print("Input must be a number!")
            continue
        if player_move <= 8 and player_move >= 0:
            return player_move
        else:
            print("You have choosen wrong number. Choose a number from 0 to 8: ")

def get_ai_move(fields_array):
    while True:
        random_number = random.randint(0,8)
        if fields_array[random_number] == " ":
            return random_number
        
def get_ai_symbol(user_symbol):
    if user_symbol == "X":
        return "O"
    else:
        return "X"

def check_result_winner(result):
    if result == "XXX":
        return "X"
    elif result == "OOO":
        return "O"
    else:
        return None

def get_game_winner(fields_array):
    #Checking rows
    for row in range(0, 3):
        field_array_start_idx = row * 3
        result = fields_array[field_array_start_idx] + fields_array[field_array_start_idx + 1] + fields_array[field_array_start_idx + 2]
        winner = check_result_winner(result)
        if winner != None:
            return winner

    #Checking columns
    for column in range(0, 3):
        result = fields_array[column] + fields_array[column + 3] + fields_array[column + 6]
        winner = check_result_winner(result)
        if winner != None:
            return winner

    #Checking right cross
    result = fields_array[0] + fields_array[4] + fields_array[8]
    winner = check_result_winner(result)
    if winner != None:
        return winner

    #Checking left cross
    result = fields_array[2] + fields_array[4] + fields_array[6]
    winner = check_result_winner(result)
    if winner != None:
        return winner

    for cell in fields_array:
        if cell == " ":
            return None 
    return "D"

def game_round(fields_array, user_symbol):
    while True:
        player_move = get_player_move()
        if fields_array[player_move] == " ":
            fields_array[player_move] = user_symbol
            break
        elif fields_array[player_move] == "O" or fields_array[player_move] == "X":
            print("this square is taken, please choose another one ")
    
    winner = get_game_winner(fields_array)
    if winner != None:
        return winner

    ai_move = get_ai_move(fields_array)
    fields_array[ai_move] = get_ai_symbol(user_symbol)
    print("AI moved to square {}: ".format(ai_move))        
    
    winner = get_game_winner(fields_array)
    if winner != None:
        return winner

    print_current_board(fields_array)
    return None

if __name__ == '__main__':
    #player_starts = does_player_start()
    #print("Player {} start and his symbol is {}".format(string, user_symbol))
    
    user_symbol = circle_or_cross()
    print_instruction_board()
    fields_array = [" "," "," "," "," "," "," "," "," "]
    winner = None
    while winner == None:
        winner = game_round(fields_array, user_symbol)
        if winner != None:
            if winner == "D":
                print("It's a draw!")
            else:
                print("Player {} won!".format(winner))
            break
        

    
