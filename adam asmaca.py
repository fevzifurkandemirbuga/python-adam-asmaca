yanıt = "e"
while yanıt == "e":
    import random

    hak = 6
    denenen_harfler = []
    with open("C:/Users/Fevzi Furkan/Desktop/meslekler.txt", "r", encoding="utf-8") as meslekler:
        meslek = []
        for i in meslekler:
            meslek.append(i)
    kelime = meslek[random.randint(0, len(meslek))]
    kelime = kelime.strip()
    aranan = kelime
    sorulan=[]
    for i in kelime:
        if i==" ":
            sorulan.append(" ")
        else:
            sorulan.append("_")
    kelime = kelime.lower()
    while hak >= 0:
        print(*sorulan)
        print("yanlış harfler:", str(denenen_harfler))
        if not ("_" in sorulan):
            print("\n\ntebrikler kazandınız")
            break
        deneme = input("bir harf giriniz: ")

        if (kelime.find(deneme) != -1):
            while kelime.find(deneme) != -1:
                sorulan[kelime.find(deneme)] = deneme
                kelime = kelime.replace(deneme, " ", 1)
        else:
            hak -= 1
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
            elif hak == 0:
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
                print("kaybettiniz\n(T_T)\t(T_T)\naranan kelime:", aranan)
                break
    yanıt = input("tekrar oynamak ister misiniz (e/h): ")