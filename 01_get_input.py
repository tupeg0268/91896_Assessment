# Get item name and check if it not blank

# not blank function goes here
def not_blank(question):
    error = "your item name got number in it"

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""
        # look at each character in float and if it number,complain
        for letter in response:
            if letter.isdigit() == True:
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# main routine goes here

item_name = not_blank("what is the item name?")

print("the item name {} ".format(item_name))