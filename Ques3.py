#3. Write a python script to handle the ArithmeticError?
def ArithematicError(a,b):
    try:
        Division=a/b
        print(Division)
    except:
        print("Can not Divide by Zero")

ArithematicError(9,0)