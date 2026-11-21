def G():
    Celcius=int(input(f"Give me any temperature"))
    Table=[] #NOTE FOR A  LIST YOU MUST ALWAYS,ALWAYS PUT .APPEND TO ADD THINGS TO THAT LIST 
    for i in range(0,Celcius+1):
        FR=(i)*1.8+32
        Table.append(round(FR,0)) #TO ROUND THING JUST PUT (ROUND(VARIABLE,DP))
    print(Table)
G()
