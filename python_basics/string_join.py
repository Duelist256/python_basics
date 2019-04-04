firstName = "Bugs"
secondName = "Bunny"

tuple = (firstName, secondName)
name = " ".join(tuple)
print(name)

words = ["How", "are", "you", "doing", "?"]
sentence = ' '.join(words)
print(sentence)

# Exercise 1. Create a list of words and join them, like the example above.
words2 = ["Hello", "world!"]
sentence2 = ", ".join(words2)
print(sentence2)
# Exercise 2. Try changing the separator string from a space to an underscore.
sentence3 = "_".join(words2)
print(sentence3)
