def hello_world():
    for i in range(4):
        value = hello_alien(i)
        if (value):
            break
        else:
            continue

def hello_alien(n):
    if n == 6:
        print("im in True")
        return True
    else:
        print("im in false")
        return False

hello_world()