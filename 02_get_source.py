# Gets source of item name and check if it not blank

# To do
# Allow user to specify customer area
# Allow user weather numbers are allowed

# Not blank function goes here
def not_blank (question,error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in float and if it number,complain
            for letter in response:
                if letter.isdigit() == True:
                  has_errors = "yes"
                  break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# main routine goes here

source = not_blank("what is the item name?",
                      "The item source cant be blank",
                      "yes")

print("the item name {} ".format(source))