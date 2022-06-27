from random import randint
from meslekler_listesi import meslekler

kelime=meslekler[randint(0,len(meslekler)-1)]
kelime=kelime.lower()
soru=[]
yanlış_tahmin=set()

for i in kelime:
    if (i!= " "):
        soru.append("_")
    else:
        soru.append(" ")
oyun=True
can=6
while oyun:
    print(*soru)
    print("yanlış tahminler:", *yanlış_tahmin)
    tahmin=input("tahmin: ")
    if (tahmin==kelime):
        print("tebrikler kazandınız")
        oyun=False
    elif (tahmin in kelime):
        for i in range(0,len(kelime)):
            if tahmin==kelime[i]:
                soru[i]=kelime[i]
    else:
        yanlış_tahmin.add(tahmin)
        can-=1
    print("yanlış tahminler:",*yanlış_tahmin)
    if can==5:
        print(""" 
    _____________
    |            |
    |            O
    |         
    |           
    |
  __|__
    """)
    elif can == 4:
        print(""" 
            _____________
            |            |
            |            O
            |            |
            |           
            |
          __|__
            """)
    elif can == 3:
        print(""" 
            _____________
            |            |
            |            O
            |           /| 
            |           
            |
          __|__
            """)
    elif can == 2:
        print(""" 
            _____________
            |            |
            |            O
            |           /|\ 
            |            
            |
          __|__
            """)
    elif can == 1:
        print(""" 
            _____________
            |            |
            |            O
            |           /|\ 
            |           /  
            |
          __|__
            """)
    elif can == 0:
        print(""" 
            _____________
            |            |
            |            O
            |           /|\ 
            |           / \ 
            |
          __|__
            """)
        print("kaybettiniz\n"
              f"kelime {kelime}")
        oyun=False