x = "awesome"


def myFunc():
    global x
    # print(x = awesome)
    print("Python is " + x)
    x = "fantastic"
    # print(x = fantastic)


myFunc()
print("Python is " + x)