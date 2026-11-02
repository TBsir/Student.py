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
