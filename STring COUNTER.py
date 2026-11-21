def G():
    Ren=input(f"Give me a sentence".strip()) #EXAMPLE IN THE WORD "HELLO
    Letters={} # A dictionary stores information using KEY-VALUE pairs.
    for i in range(len(Ren)):
        Character=Ren[i] #Ren = the whole list. 0 = the position. Ren[0] = the item at position 0.,ITS LIKE MAR AND MDR MAR IS THE 0
      #WHILE MDR IS THE DATA INSIDE POSITION ZERO WHICH IS WHATS INSIDE REN[I]
        if Character in Letters:#This asks Python:"Have I already recorded this letter in my dictionary?" 
        Letters[Character]+=1 #if it has and there is a second letter the same as that one it adds it to the counter
      #e.g in Hello there is two l once it encounters the second l it adds it to Letters[Charcater]+=1 as this stores an updated value
      #To the same existing variable. its short hand for Letters[Character]=Letters[Character +1]
        else:
            Letters[Character]=1 #If the letter does NOT already exist in the dictionary, do something else."
#For example, imagine Python encounters the letter H for the first time.
#It isn't in the dictionary yet, so Python moves to else.
#Line 12: Letters[Character] = 1 IT sees that the character H is not in the dictionarry letters yet so it adds it and gives it the value of one
#since there is no other H there 
    print(Letters)
G()

#ALSO THE SQUARE BRACKETS IN REN=[I] TELLS PYTHON Go inside Ren and retrieve the item at position i." ThATS WHAT THE SQUARE BRACKETS ARE FOR 
#ITS THE SAME WITH TEH OTHER VARIABLES AND OPERATORS WITH THE SQUARE BRACKETS 
