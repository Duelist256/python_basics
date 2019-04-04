string = "Hekko"
replaced = string.replace("k", "l")
print(string)
print(replaced)

oldValue = "Hello World World World"
newValue = oldValue.replace("World", "Universe", 2)
print(newValue)

# Exercise 1. Try the replace program ???
# Exercise 2. Can a string be replaced twice?
print()
string2 = "Hello"
print(string2.replace("l", "k").replace("k", "w")) # it can be
# Exercise 3. Does replace only work with words or also phrases?
print("Hello Matt, whacha doin?".replace("whacha doin", "how is it going")) # works with phrases
