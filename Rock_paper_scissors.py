#Rock Paper Scissors game
import random

while True:
    user_action = input( 'Enter a choice ("rock", "paper", "scissors"): ')

    while user_action != "rock" and user_action != "paper" and user_action != "scissors":
        user_action = input("Please input either rock, paper, or scissors")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        print(f"Both players picked {user_action}. It's a tie!")   
        print("\t**********Do you want to continue playing? **********")

        chance = input("\t\t********Type 'Y' to conitnue and 'q' to quit***********: ")
        if chance == 'Y':
            continue
            
        elif chance == "q":
                print('**********************GoodBye :)***************')
                break

#if Player wins and Computer looses
    if user_action == "rock" and computer_action == "scissors":
            print('Rock smashes scissors')
            print('Player wins!')

            chance = input("\t\t********Type 'Y' to conitnue and 'q' to quit***********: ")
            if chance == 'Y':
                continue
            elif chance == "q":
                print('**********************GoodBye :)***************')
                break
    if user_action == "scissors" and computer_action == "paper":
        print('Scissors cuts paper')
        print('Player wins!')
        chance = input("\t\t********Type 'Y' to conitnue and 'q' to quit***********: ")
        if chance == 'Y':
            
            continue 
        elif chance == "q":
                print('**********************GoodBye :)***************')
                break
    if user_action == "paper" and computer_action == "rock":
        print('Paper covers rock')
        print('Player wins')

        chance = input("\t\t********Type 'Y' to conitnue and 'q' to quit***********: ")
        if chance == 'Y':
            
            continue 
        elif chance == "q":
                print('**********************GoodBye :)***************')
                break

 #If Computer wins and Player looses
    if user_action == "paper" and computer_action == "scissors":
        print('scissors cuts paper')
        print('Computer wins')

        chance = input("\t\t********Type 'Y' to conitnue and 'q' to quit***********: ")
        if chance == 'Y':
                continue
        elif chance == "q":
                print('**********************GoodBye :)***************')
                break

    if user_action == "rock" and computer_action == "paper":
        print('paper covers rock')
        print('Computer wins, Player looses')

        chance = input("\t\t********Type 'Y' to conitnue and 'q' to quit***********: ")
        if chance == 'Y':
            
            continue 
        elif chance == "q":
                print('**********************GoodBye :)***************')
                break
    if user_action == "scissors" and computer_action == "rock":
        print('rock smashes scissors')
        print('Computer wins')

        chance = input("\t\t********Type 'Y' to conitnue and 'q' to quit***********: ")
        if chance == 'Y':
                continue
        elif chance == "q":
                print('**********************GoodBye :)***************')
                break
