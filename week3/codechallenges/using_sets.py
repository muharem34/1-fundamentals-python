# numbers_set = {1, 2, 3, 4, 4} #canot use duplicate numbers, it will only show one of each

# print(numbers_set)

words_set = {"Alpha", "Bravo","Charlie"}
""" abcd = ""
for word in words_set:
    abcd += word
print(abcd)   """   

""" if "Alpha" in words_set:
    print("Alph is in set")
else:
    print("Alpha not in set")     """
    
words_set.add("Delta")    
print(words_set)
words_set.discard('Bravo')
print(words_set)