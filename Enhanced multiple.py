def G():
    Num1=int(input("What is your interger").strip())
    Num2=int(input("How many multiples of N do you want").strip())
    Num4=int(input("What number do you want to add to it").strip())
    Result=[] #This is used to create a list and it has to be before the for loop so that it can add it
    for i in range(1,Num2+1):
        Num3=Num1*i
        Result.append(Num3)# .append adds items to that list called Result 
    for item in Result: #item is the same as i as it is a variable 
        print(str(item)+str(Num4)) # it takes every interger in your result list and turns it into a string then takes every item and adds it as a string to the Num4 which is also a string 
G()
