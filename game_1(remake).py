#start
while True:
    print("do u wanna start game??")
    start = input()
    if start == 'yes':
#game yes
        print("""******
you hear something strange in your backyard..
what do u want to do b it?
******""")
        while True:
            print("check noise(1), stay home(2)")
            choice1 = input()
            if choice1 == '1':
                print("""******
u noticed someone and hes trying to rob your garage!!
quick, you need to do something!!
******""")   
#choices after checking up
                while True:
                    print("call cops(1), beat him up(2), hide(3)")
                    choice2 = input()
#cops
                    if choice2 == '1':
                        print("""******
cops arrived and he got arrested!! yayyy!! *GOOD ENDING*
******""")
                        break
#beat his a$$ off
                    elif choice2 == '2':
                        print("""******
he wanna fight u back!!
what u want to do??
punch him in the stomach(1), kick his leg(2), twist his arm(3)
""")
#fight!!!!!
                        while True:
                            choice3 = input()
                            if choice3 == "1":
                                print("yaay! he dropped his knife, got scared of your strenght and escaped!! *GOOD ENDING*")
                            elif choice3 == "2":
                                print("he tripped, fell off and dropped his knife but after he stood up he escaped!! yaay!! *GOOD ENDING*")
                            elif choice3 == "3":
                                print("he had a knife and stabbed you, now you're bleeding and hes robbing your garage AND HOUSE, great........... *BAD ENDING*")
                        else:
                                print("wrong ans")
                        break
#hide
                    elif choice2 == '3':
                        print("""******
"he found and attacked you!! you passed out and got robbed. *BAD ENDING*"
""")
                        break
                    else:
                        print("wrong ans")
                break
#do nothing                
            elif choice1 == '2':
                print("someone broke into your house and attacked you, now you're laying on the floor slowly passing out and watching him robbing all your things....... *BAD ENDING*")
                break
            else:
                print("wrong ans")
            break
        break
#game no
    elif start == 'no':
        print("quiting game")
        break 
    else:
        print("wrong ans")