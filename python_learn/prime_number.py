for i in range(2,11):
    for j in range(1,10):
        condition=int (j)<int(i)&int(i)<int(j)
    if(int(i)%int(i)==0) & int(i%1)==0 & int(i)%int(condition)==0:
        print(i,"its a prime number")
        if(i%2==1):
            print(i,"its an even number")
        else:
            print("its odd number")
    else:
        print(i,"its a composite number")
        if (i % 2 == 1):
            print(i, "its an even number")
        else:
            print("its odd number")