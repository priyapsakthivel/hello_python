def hello_world():
    for i in range(3):
        value = hello_alien(i)
        if (value):
            break
        else:
            continue

def hello_alien(n):
    if n == 5:
        print("im in True")
        return True
    else:
        print("im in false")
        return False

hello_world()