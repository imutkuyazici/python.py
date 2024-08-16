import random
import os

def sayı_tahmin_oyunu():
    os.system("cls")

    hedef_tahmin = random.randint(1,20)
    tahmin_hakkı = 5

    print("*****SAYI TAHMİN OYUNUNA HOSGELDİNİZ*****\n")
    print("1-20 arasında bir sayı tahmin edin")
    
    while tahmin_hakkı > 0 :
        try:
            kullanıcı_girisi=int(input("tahmininiz : "))
            if kullanıcı_girisi<1 or kullanıcı_girisi>20:
                print("hatalı giris. 1 - 20 arasında bir sayı tutunuz..")
                continue
            if kullanıcı_girisi < hedef_tahmin :
                print("daha yuksek bir sayı tutunuz.")
            elif kullanıcı_girisi > hedef_tahmin :
                print("daha dusuk bir sayı tutun.")
            else:
                print("DOGRU TAHMİN !!!!!")
                return
        
            tahmin_hakkı -= 1
            print(f"kalan tahmin hakkınız {tahmin_hakkı}")
            input(" ")
            os.system("cls")

        except ValueError :
            print("hatalı giris. Lütfen bir sayı giriniz.")
    
    print(f"tahmin hakkınız kalmadı.\nDogru cevap : \n\n {hedef_tahmin}")

sayı_tahmin_oyunu()


