def G():
    Num1=int(input("What is your interger").strip())
    Num2=int(input("How many multiples of Num1 do you want").strip())
    for i in range(1,Num2+1):#it meanse start from 1 to watever num2 is 
        Num3=Num1*i # I is going to go theough each of the values up until num2 so it then multiples each of those values by num1 which is the number we want to get multiples of eg multiples of 3
        print(Num3)
G()
