# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

print("Hello, welcome to All You can Eat Groceries!")

# Lists out the prices of the four items to the customer
print("We have a wide variety of items, including:\n",
    "- Apples at $", constant_apple_unit_price,
    " each\n- Canned beans at $",constant_canned_beans_unit_price,
    " each\n- Soda at $", constant_soda_unit_price,
    " each\n- Lottery tickets at $", constant_lottery_unit_price, sep = "")

# Prints the current budget the customer has
print("\nYou currently have $", round(money, 2)," as your budget.", sep="")

# Asks the customer if they would like to purchase a lottery ticket
purchase_ticket = input("Would you like to purchase a lottery ticket for a chance to win $2-$10? (Y/N) ")

if (purchase_ticket == 'y' or purchase_ticket == 'Y'):

    # Variable for the outcome of the lottery ticket
    # Chances of winning is 33%
    win_or_lose = random.randint(0,2)

    if (win_or_lose == 1):

        # The winnings amount will be randomly generated between $2 and $10
        winnings = random.randint(2,10)
        print("Congratulations! You won $", winnings,"!", sep = "")

        # Adds the winning amount to the initial money balance
        money += winnings

    else:
        print("Sorry... You did not win. Too bad, better luck next time")

    # Deducts the cost of the lottery ticket from the initial money balance
    money -= 2

else:
    print("No lottery tickets were purchased")


# Tells the customer how much money they have left
print("\nYou currently have $", round(money, 2), " available", sep="")

# Asks if they would like to buy apples
purchase_apples = input("Would you like to buy apples? (Y/N) ")

if (purchase_apples == "y" or purchase_apples == "Y"):
    try:
        #Asks how many apples they would like to buy
        number_of_apples = int(input("How many apple(s) would you like to buy? "))
        total_cost_of_apples = number_of_apples * constant_apple_unit_price
        # Confirms the number of apples bought and the total cost
        print("You would like to buy ", number_of_apples," apple(s). This will cost $",
              round(total_cost_of_apples, 2), sep="")

        # Sees if the customer has enough money
        if (money >= total_cost_of_apples):
            apple_amount += number_of_apples
            money -= total_cost_of_apples
        else:
            print("Not enough money")
    except:
        # If anything other than integers
        print("Only integers are accepted")

else:
    print("No apple(s) were purchased")


# Tells the customer how much money they have left
print("\nYou currently have $", round(money, 2), " available", sep="")

# Asks if they would like to buy canned beans
purchase_canned_beans = input("Would you like to buy canned beans? (Y/N) ")

if (purchase_canned_beans == "y" or purchase_canned_beans == "Y"):
    try:
        # Asks how many canned beans they would like to buy
        number_of_canned_beans = int(input("How many can(s) of beans would you like to buy? "))
        total_cost_of_beans = number_of_canned_beans * constant_canned_beans_unit_price
        # Confirms the number of canned beans bought and the total cost
        print("You would like to buy ", number_of_canned_beans," can(s) of beans. This will cost $",
              round(total_cost_of_beans, 2), sep="")

        # Sees if the customer has enough money
        if (money >= total_cost_of_beans):
            canned_beans_amount += number_of_canned_beans
            money -= total_cost_of_beans
        else:
            print("Not enough money")
    except:
        # If anything other than integers
        print("Only integers are accepted")

else:
    print("No canned beans were purchased")


# Tells the customer how much money they have left
print("\nYou currently have $", round(money, 2), " available", sep="")

# Asks if they would like to buy soda
purchase_soda = input("Would you like to buy soda? (Y/N) ")

if (purchase_soda == "y" or purchase_soda == "Y"):
    try:
        # Asks how many soda cans (or bottles) they would like to buy
        number_of_soda = int(input("How many can(s) of soda would you like to buy? "))
        total_cost_of_soda = number_of_soda * constant_soda_unit_price
        # Confirms the number of soda bought and the total cost
        print("You would like to buy ", number_of_soda," can(s) of soda. This will cost $",
              round(total_cost_of_soda, 2), sep="")

        # Sees if the customer has enough money
        if (money >= total_cost_of_soda):
            soda_amount += number_of_soda
            money -= total_cost_of_soda
        else:
            print("Not enough money")
    except:
        # If anything other than integers
        print("Only integers are accepted")

else:
    print("No soda was purchased")


# Summarizes the money left and the amounts of items purchased
print("\nYou now have $", round(money, 2)," left", sep="")
print("You bought:\n",
      lottery_amount, " ticket(s)\n",
      apple_amount, " apple(s)\n",
      canned_beans_amount, " can(s) of beans\n",
      soda_amount, " can(s) of soda", sep="")

print("\nThank you for shopping with us! Have a good day!")