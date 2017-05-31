def hello(name="Jose"):

    def greet():
        return "\t This is inside the greet() function"

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

    if name == "Jose":
        return greet
    else:
        return welcome


x = hello()
print(x)