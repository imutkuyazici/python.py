"""
def yıldız_olustur():
    satir=int(input("lutfen bir satır sayısı giriniz : "))
    if satir<=10:
        for satir in range(1,10):
            print("yıldız ücgen olusturuluyor...")
            input("devam etmek icin 'enter' tusuna basınız") 
            print(satir[::-1])
    else:
        print("lütfen 1-10 arası bir sayı giriniz... ")
    
yıldız_olustur()

"""



kullanıcı_secimi=int(input("lütfen bir sayı giriniz : "))
print("Girdiğiniz sayinin iki katı: {sayi}".format(sayi=kullanıcı_secimi*2))

satirSayisi=int(input("lütfen satır sayısı giriniz : "))
for satirSayisi in range(1,satirSayisi,+1):
    print ("*" * satirSayisi)

kullanıcı_secimi=int(input("lütfen bir sayı giriniz : "))
print("Girdiğiniz sayinin iki katı: {sayi}".format(sayi=kullanıcı_secimi*2))

"""satirSayisi=int(input("lütfen satır sayısı giriniz : "))
for satirSayisi in range(1,satirSayisi,+1):
    print ("*" * satirSayisi)

for kullanıcı_secimi in range(1,satirSayisi-81):
       print(" "* (kullanıcı_secimi-satirSayisi) + "*"*satirSayisi)"""