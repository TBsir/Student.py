 #Table = [] inside the first loop.
#A fresh list is created for every row.
#Incorrect
#Table = [] outside the first loop.
#One list keeps collecting everything.
def G():
    Grid=int(input(f"how many grids do you want"))
    for i in range (1,Grid+1):#First round: i = 1  Second round: i = 2  Third round: i = 3
        Table=[]
        for H in range(1,Grid+1):#The reason we put a [1] instead of [i] its so that every i value goes through every H Value.
          #WHich can confuse python and give you random numebers
            FR=i*H
            Table.append(FR)
        print(*Table) #The star removes any commas and brackets printed
G()

#IF TEH CODE WAS RUN IT WOUKLD BE 
If i = 2, the second loop makes H go through 1, 2 and 3.
So we calculate:
- 2 × 1 = 2
- 2 × 2 = 4
- 2 × 3 = 6
Output: 2 4 6
#Remember: i stays as the row number, while H changes to create the columns.
#EAMPLE OF THIS RULE BELOW 
#First loop (i) controls the rows.
#Second loop (H) controls the columns.
#EXAMPLE 2 CLEARER
Input I: "3" GRID
1 2 3
2 4 6
3 6 9 










