x = 42
print("'x = 42'")
print("'x == 42' returns: ", (x == 42))
print("'x == 420' returns: ", (x == 420))

name = "Mariella"
age = 22
if name == "Mariella" and age == 22:
    print("we got here because 'if name == \"Mariella\" and age = 22' is true")

if name == "Mariella" or name == "Mari":
    print("we bot here because 'if name = \"Mariella\" or name == \"Mari\"' is true")

if name in ["Mariella", "Mari"]:
    print("we got here because 'if name in [\"Mariella\", \"Mari\"]:' is true")

if x >= 1312:
    print ("x is >+ 1312")
else:
    print("x isn't >= 1312, we got here by '\
    if x >= 1312:\
        print (\"x is >+ 1312\")\
    else:\
        \"we're here\"")

a = [1,2,3]
b = a
print("'a = [1,2,3]'\
    'b = a'")
print("'b is a' returns: ", (b is a))
print("'b == a' returns: ", (b == a))
b = [1,2,3]
print("'b = [1,2,3]'")
print("'b is a' returns: ", (b is a))
print("'b == a' returns: ", (b == a))

print("'not False' returns: ", (not False))
print("'True != False' returns: ", (True != False))
