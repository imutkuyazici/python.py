x=input("bir cümle giriniz : ")
x=x.lower()


#türkçe karakter yazdırmama
"""for i in x :
    if i=="ç" or i=="ğ" or i=="ı" or i=="ö" or i=="ş" or i=="ü" or i== "İ" :
        continue
    print(i)
"""


#sesli harf yazdırma
"""for i in x :
    if i=="a" or i=="e" or i=="o" or i=="ö" or i=="u" or i=="ü" or i=="ı" or i=="i" :
        continue
    print(i)
"""


#sessiz harf yazdırma
"""for i in x :
    if i=="b" or i=="c" or i=="ç" or i=="d" or i=="f" or i=="g" or i=="ğ" or i=="h" or i=="j" or i=="k" or i=="l" or i=="m" or i=="n" or i=="p" or i=="r" or i=="t" or i=="v" or i=="y" or i=="z" :
        continue
    print(i)
"""


#harf hesaplama
"""sesliharf=["a","e","o","ö","u","ü","ı","i" ]
sessizharf=["b","c","ç","d","f","g","ğ","h","j","k","l","m","n","p","r","t","v","y","z" ]

bosluk=0
sesizh=0 
seslih=0

for i in x :
    if i in sesliharf : 
        seslih+=1
    elif i==" ":
        bosluk+=1
    elif i in sessizharf :
        sesizh+=1
print(f"sesli harf sayısı = {seslih}")
print(f"sessizharf sayısı = {sesizh}")
print(f"bosluk sayısı = {bosluk}")

"""


#ingilizce çeevirme
"""
yenicümle = True

for i in x: 
    if i=="ö":
        yenicümle+="o"
    elif i=="ü":
        yenicümle+="u"
    elif i=="ç":
        yenicümle+="c"
    elif i=="ş":
        yenicümle+="s"
    elif i=="ı":
        yenicümle+="i"
    elif i=="ğ":
        yenicümle+="g"
    else :
        yenicümle+=i
print(yenicümle)
         """

#rastgele bir sayı üretme
"""
import random
import os 
puan=0
secim=0
sayi=1
tur=1
while sayi!=secim:
    sayi=random.randint(1,5)
    secim=(input("1-5 arası bir sayı giriniz : "))
    os.system("cls")
    if secim!=sayi:
        puan+=10
        print(f"10 puan kazandın puanın {puan} bilgisayarın seçtiği sayı:{sayi}")
        input("")
        tur+1
        print(tur)
        os.system("cls")
    else:
        print(f"kaybetiniz puanınız {puan}")
        input("")
        
"""




