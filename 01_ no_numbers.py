# iterate through float

# ask user for float
item_name =("What is the item name? ")

error = "your item name got number in it"
has_errors = ""

# look at each character in float and if it number,complain
for letter in item_name:
  if letter.isdigit()== True:
      print(error)
      has_errors = "yes"
      break

# gives us feedback...
if has_errors != "yes":
    print("you are OK")