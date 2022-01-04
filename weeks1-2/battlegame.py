wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

#hp - hitpoiings, health
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 175
dragon_hp = 300

# damage - how hard they hit
wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 30
dragon_damage = 50


while True:
    # prompt player to choose from a list of options
    print("1) " + wizard)
    print("2) " + elf)
    print("3) " + human)
    print("4) " + orc)

    # prompt player to choose character from list
    character = input("Choose your character: ")

    if character == "1" or character == "Wizard" or character == "wizard" or character == "WIZARD" or character == "WIZard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        #print("You are a Wizzard")
        break

    elif character == "2" or character == "Elf" or character == "elf" or character == "ELF" or character == "ELf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        #print("You are an Elf")
        break

    elif character == "3" or character == "Human" or character == "human" or character == "HUMAN" or character == "HUMan":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        #print("You are a Human")
        break

    elif character == "4" or character == "Orc" or character == "orc" or character == "ORC" or character == "ORc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        #print("You are an Orc")
        break

    else:
        print("Uknown character")
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        print()

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)
    print()
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print()
    print("The Dragon strikes back at ", character)
    print("The", character + "'s hitpoints are now:", my_hp)
    print()
    if my_hp <= 0:
        print("The ", character, "has lost the battle.")
        print()
        break

    # Exit game
exit_game = input(
    "Exit The Game: Type 'Y' or 'y' for Yes or 'N' or 'n' for No?  ")
while True:
    if exit_game == "Y" or exit_game == 'y':
        if character == "1" or character == "Wizard" or character == "wizard" or character == "WIZARD" or character == "WIZard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            #print("You are a Wizzard")
            break

        elif character == "2" or character == "Elf" or character == "elf" or character == "ELF" or character == "ELf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            #print("You are an Elf")
            break

        elif character == "3" or character == "Human" or character == "human" or character == "HUMAN" or character == "HUMan":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            #print("You are a Human")
            break

        elif character == "4" or character == "Orc" or character == "orc" or character == "ORC" or character == "ORc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            #print("You are an Orc")
            break

        else:
            print("Uknown character")
            print("You have chosen the character: " + character)
            print("Health: " + str(my_hp))
            print("Damage: " + str(my_damage))
            print()

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp)
        print()
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break

        my_hp = my_hp - dragon_damage
        print()
        print("The Dragon strikes back at ", character)
        print("The", character + "'s hitpoints are now:", my_hp)
        print()
        if my_hp <= 0:
            print("The ", character, "has lost the battle.")
            print()
            break
    exit_game = input(
        "Exit The Game: Type 'Y' or 'y' for Yes or 'N' or 'n' for No?  ")
    # play again
play_again = input(
    "Do you want to play again? Yes type 'y' or 'Y' for No type 'n' or 'N'")
while True:
    if play_again == "Y" or play_again == "y":
        # prompt player to choose from a list of options
        print("1) " + wizard)
        print("2) " + elf)
        print("3) " + human)
        print("4) " + orc)

    # prompt player to choose character from list
    character = input("Choose your character: ")

    if character == "1" or character == "Wizard" or character == "wizard" or character == "WIZARD" or character == "WIZard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        #print("You are a Wizzard")
        break

    elif character == "2" or character == "Elf" or character == "elf" or character == "ELF" or character == "ELf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        #print("You are an Elf")
        break

    elif character == "3" or character == "Human" or character == "human" or character == "HUMAN" or character == "HUMan":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        #print("You are a Human")
        break

    elif character == "4" or character == "Orc" or character == "orc" or character == "ORC" or character == "ORc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        #print("You are an Orc")
        break

    else:
        print("Uknown character")
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        print()

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)
    print()
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print()
    print("The Dragon strikes back at ", character)
    print("The", character + "'s hitpoints are now:", my_hp)
    print()
    if my_hp <= 0:
        print("The ", character, "has lost the battle.")
        print()
        break

    # Exit game
exit_game = input("Exit The Game: Yes or No? For Yes type 'y' or 'Y'")
while True:
    if exit_game == "Y" or exit_game == 'y':
        if character == "1" or character == "Wizard" or character == "wizard" or character == "WIZARD" or character == "WIZard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            #print("You are a Wizzard")
            break

        elif character == "2" or character == "Elf" or character == "elf" or character == "ELF" or character == "ELf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            #print("You are an Elf")
            break

        elif character == "3" or character == "Human" or character == "human" or character == "HUMAN" or character == "HUMan":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            #print("You are a Human")
            break

        elif character == "4" or character == "Orc" or character == "orc" or character == "ORC" or character == "ORc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            #print("You are an Orc")
            break

        else:
            print("Uknown character")
            print("You have chosen the character: " + character)
            print("Health: " + str(my_hp))
            print("Damage: " + str(my_damage))
            print()

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp)
        print()
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break

        my_hp = my_hp - dragon_damage
        print()
        print("The Dragon strikes back at ", character)
        print("The", character + "'s hitpoints are now:", my_hp)
        print()
        if my_hp <= 0:
            print("The ", character, "has lost the battle.")
            print()
            break
    exit_game = input(
        "Exit The Game: Type 'Y' or 'y' for Yes or 'N' or 'n' for No?  ")
play_again = input("Do you want to play again? ")
