astring = "Hello world!"
print("the length of 'Hello world!' is ", len(astring), " characters")
print("the location of the letter 'o' in 'Hello world!' is an index of: ", astring.index("o"))
print("'string.index()' returns only the first index of the character")
print("the count of 'l's in the string is: ", astring.count("l"))
print("to return a subset of a string use 'string[startIndex:endIndex]' 'astring[3:7]' returns: '", astring[3:7])
print("to reverse a string or work backwards from the end you can use negative numbers, to reverse a string use\
    'astring[::-1]' which returns: ", astring[::-1])
print("to covert a string to upper case or lower case use 'astring.upper()' or .lower(), ex: ", astring.upper() ,\
    " ", astring.lower())
print("to test for starts with and ends with use 'astring.startswith()' or .endswith() returns bool T/F \
    ex. 'astring.startswith(\"Hello\")'', and 'astring.endswith(\"asdf\")' ", astring.startswith("Hello"), " ",\
    astring.endswith("asdf"))
print("to split a string on spaces just use 'newstring = asting.split(\" \")'\
    the newstring will be an array of strings'")
newstring = astring.split(" ")
print("'newstring' = : ", newstring)
