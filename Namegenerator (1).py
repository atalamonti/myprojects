#Name Generator Project
#Angelo Talamonti
#10/17
#Init
#Functions
#Main
print("This will help you decide which restauraunt you should go to!")
print("Answer these questions to find our which restauraunt you should eat at")
ans = input("Fast food (a) or sit in (b)?")
if ans == "a":
    ans = input("Everywhere (c) or Have to look a bit (d)")
    if ans == "c":
        ans = input("Burgers (ham) or Sandwiches (sand)")
        if ans == "ham":
            print("You should go to McDonalds")
        else:
            print("You should go to Subway")
    if ans == "d":
        ans = input("Good fries (fry) or Good fortune (fort)")
        if ans == "fry":
            print("You should go to Chick-Fil-A")
        else:
            print("You should go to Panda Express")
if ans == "b":
    ans = input("Little bit of everything (l) or Something specific (s)")
    if ans == "l":
        ans = input("Apples (app) or Peppers (pep)")
        if ans == "app":
            print("You should go to Applebee's")
        else:
            print("You should go to Chili's")
    if ans == "s":
        ans = input("Closed for the night (closed) or Open no matter what (open)")
        if ans == "closed":
            print("You should go to Olive Garden")
        if ans == "open":
            print("Have fun at Waffle House!")
