#4. Write a python script to handle a ValueError?
def valueError():
    try:
        x=int("Hello World")
        print(x)
    except ValueError:
        print("Please Assign same type Value in x")
valueError()