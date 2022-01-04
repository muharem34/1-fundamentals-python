import random

high_score = 0
print("Current High Score: ", high_score)


def dice_game():

    print("1) Roll Dice")
    print("2) Leave Game")
    enter_choice = input("Enter Your choice: ")
    print()
    while True:
        if enter_choice == "1":

            random_number = random.randint(1, 6)
            print("You roll a...", random_number)
            random_number2 = random.randint(1, 6)
            print("You roll a...", random_number2, "\n")

            total_score = random_number + random_number2
            print("You have rolled a total of: ", total_score, "\n")

            print("New high score!", "\n")

            print("Current High Score: ", total_score)

            # run the dicegame() function again to start over
            dice_game()
            break

        elif enter_choice == "2":
            print("Goodbye!")
            break


dice_game()


