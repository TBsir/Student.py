def G():
    Num1=int(input(f"Give a number").strip())
    Total=0 #This is our accumulator.An accumulator stores a running total.We start at zero become we have no values yet 
    for i in range(1,Num1+1):
        Num2=i*i
        Total=Total+Num2 #Each time that i moves on to the next value The Accumulator gets updated and sets the total as the previous total i value and adds it to the new total of the next i value
      #Example below
      #Step	i (current number)	Square (i × i)	Previous total + square	New total
                    # 1	           1 x 1	          0          +         1	    = 1                   
                    # 2	          2	x  4	          1          +         4      = 5
                    #3	            3  x 9	          5          +         9	    = 14
                    #4	            4	 x 16	          14         +        16      = 30    
print(Total)
G()
