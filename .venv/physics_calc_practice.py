print("What formula use u want to use")
def loop():
    formula = input("select a letter(a-e)")
    a = "speed = distance/time"
    b = "period = 1/frequency"
    c = "potential energy = mass*gravity*height"
    d = "weight = mass*gravity"
    e = "momentum = mass*velocity"
    if formula == "a":
        print(a)
        wish = input("do you wish to continue(Y/N)")
        if wish == "Y":
            loop()
        if wish == "N":
            print("goodbye")
    if formula == "b":
        print(b)
        wish = input("do you wish to continue(Y/N)")
        if wish == "Y":
            loop()
        if wish == "N":
            print("goodbye")
    if formula == "c":
        print(c)
        wish = input("do you wish to continue(Y/N)")
        if wish == "Y":
            loop()
        if wish == "N":
            print("goodbye")
    if formula == "d":
        print(d)
        wish = input("do you wish to continue(Y/N)")
        if wish == "Y":
            loop()
        if wish == "N":
            print("goodbye")
    if formula == "e":
        print(e)
        wish = input("do you wish to continue(Y/N)")
        if wish == "Y":
            loop()
        if wish == "N":
            print("goodbye")
loop()