light = input("what color is the traffic light? (red, green, yellow)")
if light == "red":
    print("wait!!!")
elif light == "yellow":
    print("get ready!!!")
elif light == "green":
    print("gooo!!!!!!!!!!!")
else:
    print("wrong answer")
print(".....................")
print("after some time you passed the traffic lights, hallway and youre heading home")
print("you arrived home and hear something strange in backyard")
print(".....................")
print("what do you want to do??")
choice = input("(check noise, stay in home)")
if choice == "check noise":
    print("u noticed someone and hes trying to rob your garage!!")
    print("quick, you need to do something!!")
    choice1 = input("(call cops, beat him up, hide)")
    if choice1 == "call cops":
        print("cops arrived and he got arrested!! yayyy!! *GOOD ENDING*")
    elif choice1 == "beat him up":
        print("he wanna fight u back!!")
        chc1 = input("(punch him in the stomach, kick his leg, twist his arm)")
        if chc1 == "punch him in the stomach":
            print("yaay! he dropped his knife, got scared of your strenght and escaped!! *GOOD ENDING*")
        elif chc1 == "kick his leg":
            print("he tripped, fell off and dropped his knife but after he stood up he escaped!! yaay!! *GOOD ENDING*")
        elif chc1 == "twist his arm":
            print("he had a knife and stabbed you, now you're bleeding and hes robbing your garage AND HOUSE, great........... *BAD ENDING*")
        else:
            print("he'll beat you up if you're not gonna choose anything!!!!!")
    elif choice1 == "hide":
        print("he found and attacked you!! you passed out and got robbed. *BAD ENDING*")
    else:
        print("AAAAAAAAAAAAAAAAAAAAAAA IM STRESSED DO SOMETHING!!!")
elif choice == "stay in home":
    print("you still hear strange noises and they're even louder.....")
    print("i think you should check this out......")
    chc2 = input("(check noise, do nothing)")
    if chc2 == "check noise":
        print("u noticed someone and hes trying to rob your garage!!")
        print("quick, you need to do something!!")
        choice3 = input("(call cops, beat him up, hide)")
        if choice3 == "call cops":
            print("cops arrived and he got arrested!! yayyy!! *GOOD ENDING*")
        elif choice3 == "beat him up":
            print("he wanna fight u back!!")
            chc4 = input("(punch him in the stomach, kick his leg, twist his arm)")
            if chc4 == "punch him in the stomach":
                print("yaay! he dropped his knife, got scared of your strenght and escaped!! *GOOD ENDING*")
            elif chc4 == "kick his leg":
                print("he tripped, fell off and dropped his knife but after he stood up he escaped!! yaay!! *GOOD ENDING*")
            elif chc4 == "twist his arm":
                print("he had a knife and stabbed you, now you're bleeding and hes robbing your garage AND HOUSE, great........... *BAD ENDING*")
            else:
                print("he'll beat you up if you're not gonna choose anything!!!!!")
        elif choice3 == "hide":
            print("he found and attacked you!! you passed out and got robbed. *BAD ENDING*")
        else:
            print("AAAAAAAAAAAAAAAAAAAAAAA IM STRESSED DO SOMETHING!!!")
    elif chc2 == "do nothing":
        print("someone broke into your house and attacked you, now you're laying on the floor slowly passing out and watching him robbing all your things....... *BAD ENDING*")
else:
    print("u need to choose something!!")