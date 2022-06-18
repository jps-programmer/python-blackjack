# Python BlackJack v0.1 Copyright Jameson Sisk © 2022

import random

ace_value = 0
player_money = 0
in_play = True

player_wins = False

card_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
ace_value_list = ["1", "11"]

cards = {
    "1": {
        "quantity": 4,
        "value": 1
    },
    "2": {
        "quantity": 4,
        "value": 2
    },
    "3": {
        "quantity": 4,
        "value": 3
    },
    "4": {
        "quantity": 4,
        "value": 4
    },
    "5": {
        "quantity": 4,
        "value": 5
    },
    "6": {
        "quantity": 4,
        "value": 6
    },
    "7": {
        "quantity": 4,
        "value": 7
    },
    "8": {
        "quantity": 4,
        "value": 8
    },
    "9": {
        "quantity": 4,
        "value": 9
    },
    "10": {
        "quantity": 4,
        "value": 10
    },
    "jack": {
        "quantity": 4,
        "value": 10
    },
    "queen": {
        "quantity": 4,
        "value": 10
    },
    "king": {
        "quantity": 4,
        "value": 10
    },
    "ace": {
        "quantity": 4,
        "value": ace_value
    }
}

print("Welcome to BlackJack! Good luck!")
def mainloop():
    house_total = 0
    player_total = 0
    while in_play:
        user_choice = input("Hit, stand, or fold?\n")
        if user_choice.lower() == "fold":
            print("Player folds!")
            break
        if user_choice.lower() == "hit":
            card_pick = random.choice(card_list)
            card_value = cards[card_pick]["value"]
            card_quantity = cards[card_pick]["quantity"]
            if player_total >= 22:
                print("Player busts!")
                player_wins == False
                break
            elif player_total == 21:
                print("Player wins!")
                player_wins == True
                break
            else:
                if card_quantity != 0:
                    if card_pick == "ace":
                        ace_choice = input("You have drawn an ace, would you like it to count as 1 or 11?\n")
                        if ace_choice == "1":
                            ace_value = 1
                        elif ace_choice == "11":
                            ace_value = 11
                        print(ace_value)
                        player_total += ace_value
                    else:
                        print(card_value)
                        card_quantity -= 1
                        player_total += card_value
                print(f"Player Total: {player_total}")
        if house_total < 15 or player_total > house_total:
            card_pick = random.choice(card_list)
            card_value = cards[card_pick]["value"]
            card_quantity = cards[card_pick]["quantity"]
            if house_total >= 22:
                print("House busts!")
                player_wins == True
                break
            elif house_total == 21:
                print("House wins!")
                player_wins == False
                break
            else:
                if card_quantity != 0:
                    if card_pick == "ace":
                        ace_choice = random.choice(ace_value_list)
                        if ace_choice == "1":
                            ace_value = 1
                        elif ace_choice == "11":
                            ace_value = 11
                        print(ace_value)
                        house_total += ace_value
                    else:
                        print(card_value)
                        card_quantity -= 1
                        house_total += card_value
                print(f"House Total: {house_total}")
        if house_total >= 22:
            print("House busts!")
            player_wins == True
            break
        elif house_total == 21:
            print("House wins!")
            player_wins == False
            break
        elif player_total >= 22:
            print("Player busts!")
            player_wins == False
            break
        elif player_total == 21:
            print("Player wins!")
            player_wins == True
            break

mainloop()

if player_wins == True:
    player_money += 50
elif player_wins == False:
    player_money -= 50

in_play = False

play_again = input("Would you like to play another game?\n")
if play_again.lower() == "yes":
    in_play = True
    mainloop()
