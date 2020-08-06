# To do

# Ask user for budget (and check this number that is more than 4)
# Ask user for item price(check if this is a number)
# Calculate the price and budget
# Warn the user if numbers are more than 4 or less than 4


# Function go here

# Number checking function
def num_check(question, low_num):

    error = "Please enter a number that is more than or equal to {}".format(low_num)

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response < low_num:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

budget = num_check("How much: ", 4)

# Main Routine go here.

item_cost = float(input("What is the item cost?"))
item_weigh = float(input("How many items needed?"))

Get_budget = item_cost/item_weigh

print("get budget:".format(Get_budget))