import random

loop = True
match = 0
no_matches = 0
Rewards = 0
match_in_order = 0

while loop == True :
    match = 0
    no_matches = 0    
    Rewards = 0
    match_in_order = 0


    random_value1 = random.randint(0, 9)
    random_value2 = random.randint(0, 9)
    random_value3 = random.randint(0, 9)

    print("Guess three values between 0 and 9:")
    guess_value1 = int(input("Please insert your first value: \n"))
    guess_value2 = int(input("\nPlease insert your second value: \n"))
    guess_value3 = int(input("\nPlease insert your third Value: \n"))

    random_list = [random_value1, random_value2, random_value3]
    guess_list = [guess_value1, guess_value2, guess_value3]

    if random_list[0] == guess_list[0] : match = match + 1
    elif random_list[0] == guess_list[1] : match = match + 1
    elif random_list[0] == guess_list[2] : match = match + 1

    if random_list[1] == guess_list[0] : match = match + 1
    elif random_list[1] == guess_list[1] : match = match + 1
    elif random_list[1] == guess_list[2] : match = match + 1

    if random_list[2] == guess_list[0] : match = match + 1
    elif random_list[2] == guess_list[1] : match = match + 1
    elif random_list[2] == guess_list[2] : match = match + 1
    
    if random_list[0] == guess_list[0] : match_in_order = match_in_order + 1
    if random_list[1] == guess_list[1] : match_in_order = match_in_order + 1
    if random_list[2] == guess_list[2] : match_in_order = match_in_order + 1

    if match == 0 : Reward = 0
    if match == 1 : Reward = 10
    if match == 2 : Reward = 100
    if match == 3 : Reward = 1000
    if match_in_order == 3 : Reward = 1000000

    print("==================================================")
    print("Values you have guessed were:")
    print(guess_value1, guess_value2, guess_value3)
    print()
    print("Correct Values were:")
    print(random_value1, random_value2, random_value3)
    print()
    print("You have won: $" + str(Reward))
    print("==================================================")
    
    try_again = input("Do you want to try again y/n? \n")
    if try_again.lower() == "n" :
        loop = False
        break
    elif try_again.lower() == "y" :
        print("\n")
        loop == True
        continue
    
    