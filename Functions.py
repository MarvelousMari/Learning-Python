def my_function():
    print("Hello, from 'my_function'")

def my_greeting_function(username, greeting):
    print("Hello, ", username, "From my_greeting_function, I wish you ", greeting)

def sum_of_remainder_nuemerator(denominator, numerator):
    return ((numerator%denominator) + numerator)

print("a simple greeting")
my_function()

print("my greeting function")
my_greeting_function("Mariella Page", "a wonderful day!")

x = sum_of_remainder_nuemerator(4, 6)
print(x)

print("exercise:")

def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",\
        "Allowing programmers to share and connect code together"]

def finish_sentance(benefit):
    return (benefit + " is a benefit of functions!")

def naming_function_benefits():
    for benefit in list_benefits():
        print(finish_sentance(benefit))

naming_function_benefits()
