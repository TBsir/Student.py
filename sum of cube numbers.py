def G():
    num1=int(input(f"Give me a numbeer").strip())
    Total=0 #DONT BOTHER USING A SECOND LOOP ITS UNNECASSARY BECAUSE [I] ALRAEDY GOES THROUGH EACH NUMBER
  #WHICH IS WHY YOU USE A RUNNING TOTAL INSTEAD 
    for i in range(1,num1+1):
        Result=i*i*i
        Total=Total+Result #THE TOTAL UPDATES EACH TIME YOU GO THROUGH THE LOOP
    print(Total)
G()
