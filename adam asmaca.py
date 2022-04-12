yanıt="e"
while yanıt=="e":
    import random
    hak=6
    denenen_harfler=[]
    with open("C:/Users/Fevzi Furkan/Desktop/meslekler.txt","r",encoding="utf-8") as meslekler:
        meslek=[]
        for i in meslekler:
            meslek.append(i)
    kelime=meslek[random.randint(0,len(meslekler))]
    a=(len(kelime)-1)*"_"
    kelime = kelime.strip()
    aranan=kelime
    if kelime.find(" ")!=-1:
        k1=kelime.find(" ")
        k2=len(kelime)-k1-1
        a=k1*"_"+" "+k2*"_"
    kelime=kelime.lower()
    a=list(a)
    while hak>=0:
        print(*a)
        print("yanlış harfler:", str(denenen_harfler))
        if  not("_" in a) :
            print("\n\ntebrikler kazandınız")
            break
        deneme = input("bir harf giriniz: ")

        if (kelime.find(deneme)!=-1):
            while kelime.find(deneme)!=-1:
                a[kelime.find(deneme)]=deneme
                kelime = kelime.replace(deneme," ",1)
        else:
            hak-=1
            denenen_harfler.append(deneme)
            if hak == 5:
                print("""
             ________
            |        |
            |        |
            |        O
            |       
            |        
            |
            |
            |
            """)
            elif hak == 4:
                print("""
             ________
            |        |
            |        |
            |        O
            |        |
            |        
            |
            |
            |
            """)
            elif hak == 3:
                print("""
                     ________
                    |        |
                    |        |
                    |        O
                    |        |\ \
    
                    |        
                    |
                    |
                    |
                    """)
            elif hak == 2:
                print("""
                     ________
                    |        |
                    |        |
                    |        O
                    |       /|\ \
    
                    |        
                    |
                    |
                    |
                    """)
            elif hak == 1:
                print("""
                     ________
                    |        |
                    |        |
                    |        O
                    |       /|\ \
    
                    |       / 
                    |
                    |
                    |
                    """)
            elif hak==0:
                print("""
                     ________
                    |        |
                    |        |
                    |        O
                    |       /|\ \
                     
                    |       / \ \
                
                    |
                    |
                    |
                        """)
                print("kaybettiniz\n(T_T)\t(T_T)\naranan kelime:",aranan)
                break
    yanıt = input("tekrar oynamak ister misiniz (e/h): ")