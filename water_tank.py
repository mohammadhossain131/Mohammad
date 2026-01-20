# TODO: Students, fill out statement of work header
# Student Name in Canvas: Mohammad Hossain
# Penn ID:
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials:
import random
# import statements
from random import shuffle

# TODO: Write the functions as described in the instructions

# Initial water is empty (placeholder)
water_cards_pile = []

# Values of water codes
water_1 = '1'
water_5 = '5'
water_10 = '10'

# Initial power is empty (placeholder)
power_cards_pile = []

# Values of power cards
power_soh = 'SOH'
power_dot = "DOT"
power_dmt = 'DMT'

player1_cards = []
player2_cards = []

# The player tank starts off empty
player_tank = 0

# The opponent tank starts off empty
opponent_tank = 0

# The maximum a tank can fill is 80
maximum_fill_value = 80

use_discard = ""


def get_user_input(question):

    answer = ""
    answer = input(question).strip()

    while len(answer) == 0:
        answer = input(question).strip()

    if answer in ('1','5','10'):
        answer = int(answer)
        return answer
    elif answer in (power_soh, power_soh.lower(), power_dot, power_dot.lower(), power_dmt, power_dmt.lower()):
        return answer.upper()
    else:
        return answer.lower()

def setup_water_cards():
    # Setups three lists of water cards whose quantities results from
    # multiplying that quantity with the value
    # Then adds the individual lists into one list
    value_1 = 30 * [1]
    value_5 = 15 * [5]
    value_10 = 8 * [10]

    water_cards = value_1 + value_5 + value_10
    random.shuffle(water_cards)
    return water_cards

def setup_power_cards():
    value_soh = 10 * [power_soh]
    value_dot = 2 * [power_dot]
    value_dmt = 3 * [power_dmt]

    power_cards = value_soh + value_dot + value_dmt
    random.shuffle(power_cards)
    return power_cards


def setup_cards():
    # Puts the lists in setup_water_cards() and setup_power_cards() in a tuple
    return (setup_water_cards(), setup_power_cards())

def get_card_from_pile(pile, index):
    return pile.pop(index)


## LOOK AT DIRECTIONS AND FIX THIS
def arrange_cards(cards_list):
    # Arranges the cards pile
    cards_list.sort()

# FIX THIS
def deal_cards(water_cards_pile, power_cards_pile):
    # Gets the water cards pile and power cards pile from the tuple in setup_cards() and
    # gets the first three elements from water pile and first two elements from power pile

    water_hand1 = []
    water_hand2 = []
    power_hand1 = []
    power_hand2 = []

    card = 0

    for i in range (0,3):
        water_hand1.append(water_cards_pile[card])
        get_card_from_pile(water_cards_pile, card)
        #print(water_cards_pile)
        #water_hand2.append(water_cards_pile[card])
        #get_card_from_pile(water_cards_pile, card)
        #print(water_cards_pile)
    #print(len(water_cards_pile))
    for i in range (0,2):
        power_hand1.append(power_cards_pile[card])
        get_card_from_pile(power_cards_pile, card)
        #print(power_cards_pile)
        #power_hand2.append(power_cards_pile[card])
        #get_card_from_pile(power_cards_pile, card)

    # Arranges the above shortened piles for Player 1 and Player 2
    arrange_cards(water_hand1)
    arrange_cards(power_hand1)

    arrange_cards(water_hand2)
    arrange_cards(power_hand2)

    player1_hand = water_hand1 + power_hand1
    player2_hand = water_hand2 + power_hand2


    # Adds together the newly sorted lists into one list
    return (player1_hand, player2_hand)


def apply_overflow(tank_level):
    global overflow

    # If he tank_level exceeds the maximum_fill_value (80)
    if tank_level > maximum_fill_value:
        overflow = abs(tank_level - maximum_fill_value)

    # Otherwise, return the tank_level
    else:
        return tank_level

    tank_level -= overflow

    return tank_level

def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    if card_to_use in player_cards:

        # If card_to_use is any water card, then add it to the player_tank
        if card_to_use in (1, 5, 10):
            player_tank += card_to_use



        if card_to_use in (power_soh, power_dot, power_dmt):
            # Steals half of the opponent_tank and gives it to player tank if SOH is drawn
            if card_to_use == power_soh:
                value_stolen = opponent_tank / 2
                opponent_tank -= value_stolen
                player_tank += value_stolen

            # Multiplies the opponent_tank by 0 (making it empty) if DOT is drawn
            if card_to_use == power_dot:
                opponent_tank *= 0

            # Multiplies the player_tank by 2 if DMT is drawn
            if card_to_use == power_dmt:
                player_tank *= 2
    #apply_overflow()
    return (player_tank, opponent_tank)

def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    if card_to_discard in player_cards:
        if card_to_discard in (1, 5, 10):
            player_cards.remove(card_to_discard)
            water_cards_pile.insert(0, card_to_discard)

        if card_to_discard in (power_soh, power_dot, power_dmt):
            player_cards.remove(card_to_discard)
            power_cards_pile.insert(0, card_to_discard)

def filled_tank(tank):
    if 75 <= tank <= 80:
        return True
    else:
        return False

def check_pile(pile, pile_type):
    if pile_type == "water":
        if len(pile) == 0:
            setup_water_cards()
    if pile_type == "power":
        if len(pile) == 0:
            setup_power_cards()

def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    pass

def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
    pass



def main():
    # TODO: Write your code as described in the instructions

    global player_tank, opponent_tank
    global player1_cards, player2_cards

    # Indicates that the game is running
    game_running = True

    while game_running:
        print("Welcome to the Water Tank Game where you get to play against a Computer!")
        print("The first player to fill their tank wins the game\n")

        heads_tails = random.randint(1, 2)
        if heads_tails == 1:
            print("The Human player will go first\n\n")
        else:
            print("The Computer player will go first\n\n")

        # Initializes water cards pile and power cards pile from setup_cards function
        water_cards_pile = setup_cards()[0]
        power_cards_pile = setup_cards()[1]

        # Initializes the player1 and player2 cards using deal_cards function
        player1_cards = deal_cards(water_cards_pile, power_cards_pile)[0]
        player2_cards = deal_cards(water_cards_pile, power_cards_pile)[1]

        # Human Player's Turn
        while heads_tails == 1:
            print("----- Human Player's Turn -----")
            print("Player's Water Level is currently at:", player_tank)
            print("Your hand consists of:", player1_cards)
            use_discard = get_user_input("Do you want to use or discard a card? (u/d): ")

            if use_discard in ('u','U'):
                card_use = get_user_input("Which card do you want to use: ")
                player_tank = use_card(player_tank, card_use, player1_cards, opponent_tank)[0]
                opponent_tank = use_card(player_tank, card_use, player1_cards, opponent_tank)[1]

                # Removes the element card_use appears in the list
                get_card_from_pile(player1_cards, player1_cards.index(card_use))

            elif use_discard in ('d', 'D'):
                card_discard = get_user_input("Which card do you want to discard: ")
                discard_card(card_discard, player1_cards, water_cards_pile, power_cards_pile)

            print("Your water level is now:", player_tank)
            print("The Computer's water level is now", opponent_tank)
            print("Your cards are now:", player1_cards,"\n\n")

            # Now it is the Computer's turn
            #heads_tails = 2

        #elif heads_tails == 2:




        '''if filled_tank(player_tank):
            game_running = False
            print("-----Game Over-----")
            print("The Human Player Wins!")'''

        #print(len(water_cards_pile))

        #print(deal_cards(water_cards_pile, power_cards_pile))
        #print(len(water_cards_pile))
        #print(get_user_input("L: "))






if __name__ == '__main__':
    main()

'''if domain_letter.islower():
    for number in digits:
        if number in line:
            num = number
    if num:
        return ""
    else:
        return line'''