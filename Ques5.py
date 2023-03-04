#5. Write a python script to handle multiple Exception in one try?
def Multi_exception(a):
    try:
        b=int(input("Enter a Number :"))
        Division=a/b
    except ValueError:
        print("Please Assign a Number :")
    except ZeroDivisionError:
        print("You can not divide by Zero!")
    except Exception:
        print("Something Wrong")
    else:
        print(Division)
Multi_exception(16)