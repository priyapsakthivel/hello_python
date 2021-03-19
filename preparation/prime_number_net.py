number= int(input("please enter a number"))
if number >1:
    for i in range(2,number):
        if (number%i)==0:
            print("its a prime number")
        else:
            print("its a composite number")