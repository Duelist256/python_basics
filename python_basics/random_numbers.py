import random
from typing import List
from collections import defaultdict



print(random.random())
print(random.random())
print(random.randrange(0, 10))  # integer number [0, 10)
print(random.uniform(0, 10))  # floating number [0, 10] (is 10 included ?)

# Exercise 1. Make a program that creates a random number and stores it into x.
x = random.random()
print(x)
# Exercise 2. Make a program that prints 3 random numbers.
(a, b, c) = (random.random(), random.random(), random.random())
print(a, b, c)


# Exercise 3. Create a program that generates 100 random numbers and find the frequency of each number.
def generateN(n):
    result: List[int] = []
    for i in range(0, n + 1):
        result.append(random.randrange(0, n + 1))
    return result

numbers = generateN(100)
print(numbers)


def frequency(iterable):
    res = {}
    for k in iterable:
        if k not in res:
            res[k] = 1
        else:
            res[k] = res[k] + 1
    return res


print(frequency(numbers))