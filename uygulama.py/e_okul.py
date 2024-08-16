import os

ogrenci=[]

while(True):
    os.system("cls")
    secim=input("*****E OKUL*****\n1- ogrenci kaydet\n2- ogrenci sil\n3- ogrenci güncelle\n4- ogrenci listele\n\nseçim yapınız : ")
    
    if secim == "1" :
        os.system("cls")
        no =input("ogrenci no giriniz : ")
        sınıf =input("ogrenci sınıf giriniz : ")
        ad =input("ogrenci ad giriniz : ")
        soyad =input("ogrenci soyad giriniz : ")
        ogrenci ==[]
        ogrenci.append([no,sınıf,ad,soyad])
        input("ogrenci başarıyla kaydedilmiştir. devam etmek için enter tuşuna bas")
    else :    
        for i in ogrenci :
            if no in i [0] :
                input("okul numarası kayıtlı. enter tuşuna basınız")
                break
            else: 
                ogrenci.append([no,sınıf,ad,soyad])
                print(ogrenci)
                input("ogrenci başarıyla kaydedilmiştir. devam etmek için enter tuşuna bas")