s = "That I ever did see. Dusty as the handle on the door"
index = s.find("Dusty")
print(index)
index2 = s.find("ASd")
print(index2)

if "Dusty" in s:
    print("query found")
if "Dsfdg" in s:
    print("second query found")

print("Dusty" in s)
print("Dsfdg" in s)

# Find out if string find is case sensitive
s2 = "fInd"
if "find" in s2:
    print("find is case insensitive")
if "fInd" in s2:
    print("find is case sensitive")
# What if a query string appers twice in the string?
s3 = "hello, how are you, hello"
print(s3.find("hello")) # will return an index of the first found substring
# Write a program that asks console input and searches for a query.
myInput = input("Enter smth plz: ")
query = input("Enter what u want to find plz: ")
if query in myInput:
    print("Found '%s' at a position %d" % (query, myInput.find(query)))
else:
    print("Nothing found! :(")