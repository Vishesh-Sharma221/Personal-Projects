import time 
import random 
import sys

ask = input("The Default Goal Score is 100, Do u want to change it ? (yes/no) \n")

try:
    if ask.lower() == "yes":
        MAX_VALUE = int(input("Enter the Goal Score: "))
    elif ask.lower() == "no":
        MAX_VALUE = 100
except:
    print("Wrong Input! Goal Score set to 100 (default)")


MAX_DICE_TURNS = 6
SLEEP_TIME = 1

snakes = {
    12:7,
    23:13,
    34:10,
    55:33,
    79:55,
    99:2
}

ladders = {
    7:32,
    12:22,
    34:44,
    43:56,
    66:77,
    78:96
}

def welcome_msg():
    print("Welcome to the Snake and Ladders game made by vishesh")
    print(f''' THE RULES ARE SIMPLE : 
            1. HIT ENTER TO ROLL THE DICE 
            2. PLAY THIS WITH YOUR FRIEND !
            3. THE FIRST ONE TO REACH THE GOAL SCORE ({MAX_VALUE}) WINS! \n''')

def get_dice_value():
    time.sleep(SLEEP_TIME)
    dice_num = random.randint(1,MAX_DICE_TURNS)
    print("\n Anddd... its a " + str(dice_num) )
    return dice_num

def get_player():
    player1 = None
    while not player1:
        player1 = input("Player 1 : ").strip()

    player2 = None
    while not player2:
        player2 = input("Player 2 : ").strip()

    print("\n" + player1 + " VS " + player2 + "\n")
    return player1, player2

def got_snake_bite(old_value, current_value, player_name):
    print("\n" + player_name + " gets a snake bite !! " + str(old_value) + " -------------> " + str(current_value))

def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + player_name + " Climbes the Ladder !! " + str(old_value) + " --------------> " + str(current_value) + "!")


def game(player_name , current_value , dice_value):
    time.sleep(SLEEP_TIME)
    old_value = current_value
    current_value = current_value + dice_value


    if current_value > MAX_VALUE:
        print("\n" + player_name + " Moves! " + str(old_value) + " -----------> " + str(current_value))
        print("\n" + "Well played! " + player_name + " won the game!")  
        print("\n" + "Thank you for playing the game! Press Enter key to exit")  
        last_input = input(" : ")
        sys.exit(1)
        return old_value

    print("\n" + player_name + " Moves! " + str(old_value) + " -----------> " + str(current_value))

    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def start():
    welcome_msg()
    time.sleep(SLEEP_TIME)
    player1,player2 = get_player()
    time.sleep(SLEEP_TIME)

    player1_position = 0
    player2_position = 0

    while True:
        time.sleep(SLEEP_TIME)
        input_1 = input("Your turn " + player1 + " Hit enter to roll the dice!")
        print("Rolling the dice . . .")
        dice_value = get_dice_value()
        time.sleep(SLEEP_TIME)

        player1_position = game(player1,player1_position,dice_value)

        input_2 = input("Your turn " + player2 + " Hit enter to roll the dice!")
        print("Rolling the dice . . .")
        dice_value = get_dice_value()
        time.sleep(SLEEP_TIME)

        player2_position = game(player2,player2_position,dice_value)


start()