def G():
    Pie=input(f"Type in any string").strip()
    Pie2=input(f"Type in another string").strip()
    if len(Pie)>len(Pie2):#Len operator is used to count how many letters there are in a particular string 
        print(f"Longer")
    if len(Pie)<len(Pie2):
        print(f"Shorter")
    if len(Pie)==len(Pie2):
        print(f"Equal")
G()
 

#INCORRECT
pie=input(len(f"Type in any string").strip()
#The problem is that len() is being applied to the instruction rather than the string entered by the user.
#THE INSTRUCTION IN THIS CASE IS "TYPE I ANY STRING SO TEH LEN() IS JUST GOING TO COUNT HOW MANY LETTERS AND SPACES ARE IN"TYPE IN ANY STRING " IN THIS CASE ITS 18
