    # Dictionaries
state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}
# print(len(state_capitals))

# print(state_capitals["Washington"])

state_capitals["Washington"] = "Aberdeen"
    # since there is no key value for Texas, it will be added to the end of the dictionary
state_capitals["Texas"] = "Austin"

# print(state_capitals)

    # We can us del or pop() to remove key value pairs.  You will use pop() if you want to preserve a value, you can assign it to a variable, del you cant presercve
del state_capitals["California"]
print(state_capitals)

state_capitals.pop("Oregon")
print(state_capitals)

