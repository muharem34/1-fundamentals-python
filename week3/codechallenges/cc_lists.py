import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    user_input = input(
        "Press 'enter' to pick a card or 'Q' then enter to quit: ")

    if user_input == "Q" or user_input == "q":
        break
    else:

        random_card = random.choice(diamonds)
        # print("Your random card is: ", random_card)
        hand.append(random_card)
        # print(len(diamonds))
        diamonds.remove(random_card)
        print(diamonds)
        print("Your hand: ", hand)
        print("Remaining Cards: ", diamonds)

if not diamonds:
    if diamonds == []:
        print("There are no more cards to pick.")
