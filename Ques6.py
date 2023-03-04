#6. Write a python script to create a calculator with 4 basic operations, and handle a maximum number of exceptions.?
def Calculater():
    try:
        num1=int(input("Enter a First Number :"))
        num2=int(input("Enter Second Number :"))
        symbol=input("Enter Symbol for:- \nAddition(+)\n Subtraction(-)\n Multiply(*)\n Divide(/)")

        if symbol=='+':
            return num1+num2
        elif symbol=='-':
            return num1-num2
        elif symbol=='*':
            return num1*num2
        elif symbol=='/':
            return num1/num2
    except ValueError:
        print("Please Enter integer type Value")
    except ZeroDivisionError:
        print("You can't divide by Zero!")
    except Exception:
        print("Something is wrong!")

print(Calculater())

