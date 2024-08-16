""" OKUL NO 
okul_no=827
print(okul_no)

"""

""" DİKDÖRTGEN ALAN H
kkenar=3
ukenar=5
alan=kkenar*ukenar
print(alan)
"""

""" ÜSLÜ TOPLAMA İŞLEMİ
sonuc=(4+3)**2
print(sonuc)

"""

""" ÇIKTI SORUSU
a=10
b=11
c=12
print(a is c)
print(a is not b)
a+=1
print (a is b)
a+=1
print(a is c)
"""

""" MEB YAZDIRMA
m="milli"
e="eğitim"
b="bakanlığı"

print(m,e,b)
"""

""" MERHABA YAZDIRMA
print("merhaba" *3)

"""

""" PARA BİRİMİ
para_birimi="türk lirası"

print(para_birimi)
type(para_birimi)
"""

""" ORTALAMA HESAPLAMA
not1=int(input("1.notunuzu giriniz"))
not2=int(input("2.notunuzu giriniz"))
not3=int(input("3.notunuzu giriniz"))

ort=(not1+not2+not3)/3
input(ort)

"""

""" KARE HESAPLAMA
sayi=int(input("lütfen karesini hesaplamak istediğiniz sayıyı giriniz"))

kare=sayi*sayi

print(kare)

"""

""" YAS HESAPLAMA
yıl=2023
ad=input("lütfen adınızı giriniz")
dt=int(input("lütfen doğum tarihinizi giriniz"))

yas=(yıl-dt)
print("adınız",ad)
print("yasınız",yas)
"""

""" KİTAP OKUMA
ad=input("lütfen adınızı giriniz")
ksayısı=int(input("okuduğunuz kitap sayısı"))

list=["ad","ksayısı"]
print(list[0], list[1])

"""

""" LİST HAFTANIN GÜNLERİ
list=['pazartesi','salı', 'çarşamba','perşembe','cuma','cumartesi','pazar']
print(list)
"""

""" LİST MEYVE
list=['muz','şeftali','kayısı']
print(list[0],list[1],list[2])

"""

""" LİST İNDEKS ÇIKARMA
list=['pazartesi','salı', 'çarşamba','perşembe','cuma']
print(list[4])

"""

""" ASAL SAYILAR ÇIKTI
asal_sayilar=[2,3,5,7,11,13,17,19,23]
print(asal_sayilar[::2])

"""

""" INSERT EKLEME
list=["sanat","sanat","içindir"]
list.insert=([1],"toplum")

print(list)
"""


hafta_ici=["pazartesi", "salı", "çarşamba","perşembe","cuma"]
print("cumartesi" in hafta_ici)