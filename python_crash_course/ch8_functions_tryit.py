#Brian Saville
#June 1, 2026
#Working on the try it exercises for Ch8: Functions of Python Crash Course

#8-1: Message
def message():
    """Displays a message about what I'm making."""
    print("In this chapter, I'm learning about functions!")

message()


#8-2: Favorite Book
def favorite_book(title):
    """Prints a statement about an inputted book title."""
    print("I've had " + title + " sitting on my shelf forever!")

favorite_book("Demon Copperhead")


#8-3: T-shirt
def tshirt(size = "L", color = "blue", message = "Life is Good"):
    """Prints a statement about a shirt of a chosen size and message."""
    print("I'm looking for a " + color + ", size " + size + " t-shirt.")
    print('Printed on the shirt is the message: "' + message + '".')

tshirt("small", "red", "bogos binted?")
tshirt(color = "green", size = "XXL", message = "Virginia is for lovers")


#8-4: Large shirts
def tshirt(size = "large", color = "blue", message = "I love Python!"):
    """Prints a statement about a shirt of a chosen size and message."""
    print("I'm looking for a " + color + ", size " + size + " t-shirt.")
    print('Printed on the shirt is the message: "' + message + '".')

tshirt(color = "pink")
tshirt("medium", "yellow")
tshirt("extra small", message = "Tangela Fan Club")


#8-5: Cities
def describe_city(city = "Reykjavik", country = "Iceland"):
    """"Prints a statement about a given city and its home country."""
    print("I am going on a voyage to " + city + ", " + country + "!!!")

describe_city("New York", "USA")
describe_city(city = "Melbourne", country = "Australia")
describe_city("Tokyo", country = "Japan")