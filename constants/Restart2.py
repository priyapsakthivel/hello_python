#create a calci program which gets 4 input from user and perform all the 4 operations using method

num1=input("please enter a number1")
num2=input("please enter a number2")
num3=input("please enter a number3")
num4=input("please enter a number4")

def addition(num1,num2):
    add= int(num1)+int(num2)
    print(add)
addition(num1,num2)
def subtraction(num3,num2):
    sub= int(num3)-int(num2)
    print(sub)
subtraction(num3,num2)
def multiply(num4,num2):
    multi= int(num4)*int(num2)
    print(multi)
multiply(num4,num2)
def division(num4,num1):
    div= int(num4)/int(num1)
    print(division)
division(num4,num1)
