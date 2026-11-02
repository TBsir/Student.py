def G():
    Prone="a","e","i","o","u"
    Vowels=input(f"Type a letter").lower() #This operator turns the string into a lower case remember
    if Vowels in Prone: #The in operator is used to check if a value exists  in two variables but only used for a singular value Can also be usd in intergers
        print(f"Vowel")
    else:
        print(f"Consonant")
        
G()
