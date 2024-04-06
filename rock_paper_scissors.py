import random 

user_win = 0
computer_win = 0

options = ["rock","paper","scissors"] 

rounds = input('Enter the number of matches you want to play')
rounds = int(rounds)

while (rounds):
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock : 0, paper : 1, scissors : 2
    computer_guess = options[random_number]
    print('Computer picked',computer_guess+".")

    if user_input == "rock" and computer_guess == "scissors":
        print("you won!")
        user_win += 1 
        rounds -= 1 

    elif user_input == "paper" and computer_guess == "rock":
        print("you won!")
        user_win += 1 
        rounds -= 1 

    elif user_input == "scissors" and computer_guess == "paper":
        print("you won!")
        user_win += 1  
        rounds -= 1

    elif user_input == computer_guess:
        print("You and computer both picked",user_input)
        print('Draw')
        rounds -= 1

    else:
        print("You lost")
        computer_win += 1
        rounds -= 1

print("You won",user_win,"times")
print("Computer won",computer_win,"times")
print('Goodbye!')