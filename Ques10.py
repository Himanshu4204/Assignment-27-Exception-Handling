#10. Write a python script to implemented a nested Try Except block?

def nested():
    try:
        num1=int(input("Enter First Number:"))
        num2=int(input("Enter Second Number:"))

        try:
            division=num1/num2
            print("Division is :",division)

        except ZeroDivisionError:
            print("You cant not divide by Zero!")

    except ValueError:
        print("Please Enter a Integer type value")
nested()

