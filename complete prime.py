def G():
    Num1 = int(input("Give any number: ").strip())

    if Num1 < 2: # also you cant put this line of code ahead of line 2 because teh user has to input something first 
        print("Not prime")

    elif Num1 == 2 or Num1 == 3 or Num1==5:
        print("Prime")

    elif Num1 % 2 == 0:
        print("Not Prime")

    elif Num1 % 3 == 0:
        print("Not Prime")

    elif Num1 % 5 == 0:
        print("Not Prime")

    elif Num1 % 7 == 0:
        print("Not Prime")

    else:
        print("Prime")

G()
#Note;Python reads code from top to bottom so lets say the user input 9 
# 9<2 no
#is 9 the same as 2,3,5 No
#9 divided by 2 no
#9 divided by 3 yes so it stops there 
# SAME THING WITH 2 
#2<2 No
#is 2 thw same thing as 2 or 3 or 5 yes same thing as two so it stops there. SO ONCE ONE SATISYING CONDITION IS MET THE CODE STOPS 
