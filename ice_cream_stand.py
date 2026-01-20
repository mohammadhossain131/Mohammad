"""
STARTER CODE
Homework 2: Ice Cream Stand
Topics Covered:
- Lists (append, pop)
- For and while loops
- Getting user inputs
- Validating user inputs
- Functions and helper functions
- Formatted Strings
"""
from operator import index
from os import error
# TODO: Students, fill out statement of work header
# Student Name in Canvas: Mohammad Hossain
# Penn ID: 86691517
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: W3 School

# import statements
#Note we use from ... import ... 
#This means you can use randint directly without random.randint()
from random import randint, choice

from pandas.core.computation.ops import isnumeric
from soupsieve.util import lower


def print_welcome_and_menu(list_of_flavors, list_of_sizes, list_of_prices):
    """
    Prints the following:
    1. Welcome message (Must contain word 'welcome')
    2. Message on what flavors are available in the ice cream store.
        Hint: Loop through the list_of_flavors
    3. Message on how much each size cost.
        Hint: Loop through the list_of_sizes, list_of_prices
        Format should be: Our {size} ice cream is ${price}.
    """
    # TODO: Write your code here
    print("Welcome to Desago's Ice Cream Stand!\n")
    print("The flavors we are currently offering today are:")

    # Iterates through list_of_flavors and prints out each 'flavor'
    for flavor in list_of_flavors:
        print(flavor)

    print()
    # Variable to indicate index for list_of_prices
    price_index = 0
    for size in list_of_sizes:
        print("Our {} ice cream is ${}".format(size, list_of_prices[price_index]))
        price_index += 1
    #pass    # TODO: Remove the pass statement once you have your code written


def get_order_qty(customer_name):
    """
    Ask the customer how many orders of ice cream they want.
    Valid order quantity should be an integer 1-5 inclusive. If outside the range or non-int, re-prompt.
    Hint: When asking for user input, cast it to an integer. If the input cannot be cast-ed to an integer, re-prompt.
    "2.55", "abc", "   ", are a few examples of what should all re-prompt the user.
    Returns: How many orders of ice cream the customer wants.
    """
    order_qty = 0
    # TODO: Write your code here

    print("Welcome", customer_name, end=", ")

    # Uses Try/Except to test for errors (e.g. strings, blanks, etc) in order_qty
    try:
        while order_qty not in range(1, 6):
            order_qty = int(input("how many ice creams will you be ordering today (1 to 5)? "))

    except ValueError as e:
        print("Please enter a valid integer")
        while order_qty not in range(1, 6):
            order_qty = int(input("How many ice creams will you be ordering today (1 to 5)? "))


    return order_qty


def get_ice_cream_flavor(ice_cream_flavors):
    """
    Ask the customer 'Which flavor would you like (v/c/s)? '
    Then, processes and cleans the input and returns the equivalent flavor from ice_cream_flavors list.
    Hint:   Use the indices set in the main function for the flavors.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Cookies and Cream'
            will be considered as 'c' which corresponds to 'Chocolate'.
            Ask again if it is not a valid flavor.
    Returns: String of ice cream flavor picked (e.g "Vanilla")
    """
    flavor_picked = ""
    # TODO: Write your code here

    # Sets flavor_picked to the output of get_first_letter_of_user_input function (v/c/s)
    flavor_picked = get_first_letter_of_user_input("Which flavor would you like (v/c/s)? ")

    # While loop for input that does not equal 'v', 'c', 's'
    # If anything else, then re-prompt
    while flavor_picked not in ('v','c','s'):
        flavor_picked = get_first_letter_of_user_input("Which flavor would you like (v/c/s)? ")

    # Iterates over the list of flavors
    # If variable flavor_picked is equal to the first letter of one of the flavors ice_cream_flavors
    # then set flavor_picked to that item
    for flavor in ice_cream_flavors:
        if flavor_picked == flavor.lower()[0]:
            flavor_picked = flavor

    return flavor_picked


def get_ice_cream_size(ice_cream_sizes):
    """
    Ask the customer 'Which size would you like (s/m/l)? '
    Then, processes and cleans the input and returns the equivalent size from ice_cream_sizes list.
    Hint:   Use the indices set in the main function for the sizes.
            Call the get_first_letter_of_user_input function to get and process inputs.
            Note: Only the first letter of the input will be considered so an input of 'Super Large'
            will be considered as 's' which corresponds to 'Small'.
            Ask again if it is not a valid size.
    Returns: String of Size picked (e.g "Small")
    """
    size_picked = ""
    # TODO: Write your code here

    # Output of get_first_letter_of_user_input function
    size_picked = get_first_letter_of_user_input("Which size would you like (s/m/l)? ")

    # While loop for input that does not equal 's', 'm', 'l'
    # If anything else, then re-prompt
    while size_picked not in ('s','m','l'):
        size_picked = get_first_letter_of_user_input("Which size would you like (s/m/l)? ")

    # Iterates over the list of sizes
    # If variable size_picked is equal to the first letter of one of the flavors of ice_cream_sizes
    # then set size_picked to that item
    for size in ice_cream_sizes:
        if size_picked == size.lower()[0]:
            size_picked = size

    return size_picked


def get_ice_cream_order_price(ice_cream_size, ice_cream_prices, ice_cream_sizes):
    """
    Hint:   Use the indices set in the main function for the prices of Small, Medium and Large.
    Returns: The equivalent price of an ice cream size. Example: Returns 4.99 if ice_cream_size is 'Small'
    """

    # TODO: Write your code here

    # Gets the index of ice_cream_size in ice_cream_sizes and stores it in size_index
    size_index = ice_cream_sizes.index(ice_cream_size)

    # Returns the price in ice_cream_prices at index size_index
    return ice_cream_prices[size_index]


def take_customer_order(customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices):
    """
    This function runs when a customer reaches the front of the queue. It should print
    the current customer's name being served, and take their order(s).
    If the customer can pay for their order, returns the amount of revenue from the sale.
    If the customer cancels their order, returns 0.
    Hint: Use other helper functions we required you to write whenever needed here.
    This includes the use of help functions like get_first_letter_of_user_input
    Returns: Amount of Revenue from the sale with customer
    """

    total_bill = 0

    # TODO: Print a message "Now serving customer: X" where X is the current customer's name

    print("\nNow serving customer:", customer_name)

    # TODO: Call the get_order_qty and save the value to order_qty
    order_qty = get_order_qty(customer_name)

    # TODO: For Each order you need to get a flavor, and size
    for order in range(order_qty):
        print("Order No.:", order + 1)
        # TODO: Write code to get the ice cream flavor for this order
        flavor = get_ice_cream_flavor(ice_cream_flavors)
        # TODO: Write code to get the ice cream size for this order
        size = get_ice_cream_size(ice_cream_sizes)
        # TODO: Write code to get the price for this order
        price = get_ice_cream_order_price(size, ice_cream_prices, ice_cream_sizes)

        # TODO: Update the total_bill
        total_bill += price
        # TODO: Print the details for this order
        #   Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places

        print(f"You ordered a {size} {flavor} for ${price}")
            # TODO: Remove the pass statement once you have your code written

    # TODO: Print the customer's total_bill

    print(f"Your total bill is: ${total_bill}\n")
    # TODO: Once orders are all taken, the customer should be asked if they still want to Pay or Cancel
    #  "Would you like to pay or cancel the order (p/c)? "
    #   Hint: Use the get_first_letter_of_user_input() Re-prompt if answer does not start with 'p' or 'c'

    pay_cancel = get_first_letter_of_user_input("Would you like to pay or cancel the order (p/c)? ")

    # While loop for input that does not equal 'p' or 'c
    # If anything else, then re-prompt
    while pay_cancel not in ('p','c'):
        pay_cancel = get_first_letter_of_user_input("Would you like to pay or cancel the order (p/c)? ")

    # If pac_cancel is equal to 'c', then the customer has canceled their order and total_bill is 0
    if (pay_cancel == 'c'):
        total_bill = 0

    return total_bill


def get_first_letter_of_user_input(question):
    """
    Takes in a string as its argument, to be used as the question you want the user to be asked.
    Gets input from the user, you must use input() inside this function to pass tests
    Removes whitespace and makes all letters lowercase
    Hint: Use the strip() and lower() functions.
    Note: The question paramter is a string, such as "Which size would you like (s/m/l)?"
    Returns: The first letter of the input the user provides. Ask again if the input is empty.
    """

    first_letter = ""
    # TODO: Write your code here

    # This variable contains the input to ask the question while stripping the whitespace and
    # lowercases all of the characters in the string
    # Contains the first letter of the modified string
    first_letter = input(question).strip().lower()[0]
    return first_letter


def are_all_customers_served(customer_queue_length):
    """
    If there are no customers in the queue, returns True, and all customers have been served.
    Otherwise, returns False.
    Hint: The parameter customer_queue_length is of type int.
    Returns: True or False
    """
    # TODO: Write your code here
    if (customer_queue_length == 0):
        return True
    else:
        return False

def print_current_status(customers_served, tracking_revenue):
    """
    Prints a message of how many customers have been served and the total sales of the ice cream stand.
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here
    print("\nWe have served ", customers_served, " customer(s) and have earned a total of $", tracking_revenue,"\n", sep = "")
        # TODO: Remove the pass statement once you have your code written


def print_sales_summary(customers_served, tracking_revenue):
    """
    Takes in the arguments customers_served and tracking_revenue. Prints both
    arguments as strings to let the user know what those values are.
    Output should look something like:
        Total customers served: 3
        Total sales           : $xx.xx
    Hint: See https://www.w3schools.com/python/python_string_formatting.asp for string formatting examples on rounding to 2 decimal places
    No Return, only print statements
    """
    # TODO: Write your code here

    # Prints the total number of customers served and the total revenue
    print("Total customers served:", customers_served)
    print("Total sales: $", round(tracking_revenue, 2), sep=" ")
        # TODO: Remove the pass statement once you have your code written


def random_queue_length():
    """
    Takes no arguments.
    Uses the imported randint function to generate a random integer between 2 and 5 inclusive.
    Hint: See https://www.w3schools.com/python/ref_random_randint.asp
    Returns: The resulting random integer.
    """
    # TODO: Write your code here
    number_of_cust = randint(2,5)
    # TODO: Remove the pass statement once you have your code written
    return number_of_cust


def main():
    """
    Lists of available flavors, sizes and prices. DO NOT CHANGE.
    For sizes and prices, we will use the following convention:
    Index 0 for Small
    Index 1 for Medium
    Index 2 for Large
    """
    ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    ice_cream_sizes = ['Small', 'Medium', 'Large']
    ice_cream_prices = [4.99, 7.49, 8.49]

    #List of names of possible customers
    customer_names = ["Alice", "Bob", "Charlie", "Dan", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    program_running = True
    while program_running:
        # set shop to open
        input('Press enter to open the shop! ')
        queue_is_open = True

        # TODO: Call the print_welcome_and_menu function with the parameters in the following order -
        #  ice_cream_flavors, ice_cream_sizes, ice_cream_prices
        print_welcome_and_menu(ice_cream_flavors, ice_cream_sizes, ice_cream_prices)

        # set initial values
        tracking_revenue = 0

        # will hold the list of names of the customers in the queue
        customers_in_queue = []
        customers_served = 0

        # TODO: Call the random_queue_length function and save the result to num_of_customers_in_queue
        num_of_customers_in_queue = random_queue_length()

        # TODO: Print how many customers are in the queue
        print("\nNumber of customers in the queue:", num_of_customers_in_queue)

        # TODO: Call the imported choice function to generate a random name from customer_names.
        #   Then, append each name to the end of the customers_in_queue list.
        #   The total number of customer names added should be equal to num_of_customers_in_queue
        #   Hint: See https://www.w3schools.com/python/ref_random_choice.asp
        #   Note: It is OK to have duplicate names in the queue.

        for customer in range(0, num_of_customers_in_queue):
            customers_in_queue.append(choice(customer_names))


        while queue_is_open:
            # TODO: Extract the first customer (index 0) from the customers_in_queue and save it to
            #  the current_customer_name variable.
            #  After extraction, the customer should now be removed from the customers_in_queue list.
            #  Hint: Use the pop function with an index argument
            current_customer_name = customers_in_queue[0]
            customers_in_queue.pop(0)


            # TODO: Take a customer at the window and update the revenue by calling the take_customer_order function
            customer_bill = take_customer_order(current_customer_name, ice_cream_flavors, ice_cream_sizes, ice_cream_prices)
            tracking_revenue += customer_bill

            # TODO: Update the customers_served variable
            customers_served += 1
            # TODO: Call the print_current_status
            print_current_status(customers_served, tracking_revenue)

            # TODO: Call the are_all_customers_served(customer_queue_length) function to check if there are any more
            #  customers in the queue.
            if (are_all_customers_served(len(customers_in_queue)) == True):
                print_sales_summary(customers_served, tracking_revenue)
                queue_is_open = False
            else:
                queue_is_open = True
            #  If False, continue the loop.
            #  If True, call the print_sales_summary(customers_served, tracking_revenue) and close the queue
                # TODO: Remove the pass statement once you have your code written


        # TODO: Ask if you want to open the ice cream stand again "Do you want to open again (y/n)? "
        #  Hint: Use the get_first_letter_of_user_input function
        #  Update the program_running variable if you get a valid answer either 'y' or 'n'
        #  Otherwise, re-prompt until a valid answer is given

        # Asks the use if they want to open the store again
        open_store = get_first_letter_of_user_input("Do you want to open again (y/n)? ")

        # Will ask again if there is no valid answer

        while open_store not in ('y', 'n'):
            open_store = get_first_letter_of_user_input("Do you want to open again (y/n)? ")

        # If open_store is 'y', then the program remains open
        # Else, the program closes
        if (open_store == 'y'):
            program_running = True
        else:
            program_running = False


if __name__ == '__main__':
    main()