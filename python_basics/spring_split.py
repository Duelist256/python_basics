s = "It's too easy\nyou\tknow  "
words = s.split()
print(words)
print(len(words))
print(len(s))
print(" ".join(words))

print("list():")
print(list("Easy"))
# print("Easy".split("")) # will return ValueError: empty separator

# Exercise 1. Can a string be split on multiple characters?
print("Y e p".split(" "))
# Exercise 2. Can you split this string: World,Earth,America,Canada ?
print("World,Earth,America,Canada".split(","))
# Exercise 3. Given an article, can you split it based on phrases?
print("This is an article. It's just. An experiment. Thanks!".split(". ")) # why not