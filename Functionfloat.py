def Carnage():
    Num1=float(input(f"What number do you want to input").strip())
    Num2=float(input(f"What second number do you want to input").strip())
    Num3=(Num1*Num2)
    return Num3
result=Carnage()
Num1=input(f"Do you want to multiply your value by 2")
#if Num1.lower()=="yes": This Num1.lower() allows the user to be able to enter upper case "Yes" or lower case"yes" same thing with.upper()
    Num4=(result*2)
    print(Num4)
else:
    print(f"Then you must be happy with your result")
  #Writing Carnage like thsi is just the function name 
#like thsi Carnage() calls the function to give you the value each time you write taht it tells the function to run and give the value
#That's because every time you call Carnage(), Python executes the instructions inside that function again.
#Rememmber it does not save the value as the varaiable it only brings out the result what you need now if you want to use it again ist to put 
#that carnage in a variable eg Result=Carnage() that way you can use it again and again without having to run the instruction  again and it asking
#Each time for new data
#Example below
result = Carnage() #lets say the result was 15 so you just do taht from line22 to 24

print(result * 2)
print(result * 3)
print(result + 10)
