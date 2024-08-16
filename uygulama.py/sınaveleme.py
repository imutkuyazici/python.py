import os
import random
takimlar=[]
ceyrek_final=[]
yari_final=[]
final=[]
sampiyon=' '
kaydet=True

def sorgula(takim):
    if takim in takimlar:
        return True
    else:
        return False

def takim_kaydet():
    global kaydet
    os.system('cls')
    if kaydet:        
        sayac=1
        while(sayac<17):        
            takim=input(f"{sayac}. Takım : ")
            if sorgula(takim):
                print(f"{takim} takımı kayıtlı.")
                continue            
            else:
                takimlar.append(takim)
                sayac+=1
        print(takimlar)
        kaydet=False
        input(f"\nTakımlar kaydedildi.\nAna ekrana dönmek için enter tuşuna basınız..")
        
    else:
        input(f"Takımlar kayıtlı.\nAna ekrana dönmek için enter tuşuna basınız..")   

def ust_tura_gecenler(takimlar):
    ust_tur=[]
    while (len(takimlar)!=0):
            takim1=random.choice(takimlar)
            takimlar.remove(takim1)
            takim2=random.choice(takimlar)
            takimlar.remove(takim2)
            gol1=random.randint(0,5)
            gol2=random.randint(0,5)
            while gol1==gol2:
                gol1=random.randint(0,5)
                gol2=random.randint(0,5)
            if gol1>gol2:
                ust_tur.append(takim1)
            else:
                ust_tur.append(takim2)
            print(f"{takim1} : {gol1}\n{takim2} : {gol2}\n")
    return ust_tur

def takim_listele():   
    os.system('cls')    
    if kaydet:
        input("Kayıtlı takım bulunamadı.\nAna ekrana dönmek için enter tuşuna basınız..")
    else:
        print(takimlar)
        input(f"\nTakımlar listelendi.\nAna ekrana dönmek için enter tuşuna basınız..")

def eslesme_baslat():
    global kaydet   
    os.system('cls')    
    if kaydet:
        input("Kayıtlı takım bulunamadı.\nAna ekrana dönmek için enter tuşuna basınız..")
    else:        
        cf=ust_tura_gecenler(takimlar)        
        input(f"\nÇeyrek finale kalan takımlar\n{cf}\n\nÇeyrek final maçları için enter tuşuna basınız..")
        yf=ust_tura_gecenler(cf)        
        input(f"\nYarı finale kalan takımlar\n{yf}\n\nYarı final maçları için enter tuşuna basınız..")
        final=ust_tura_gecenler(yf)        
        input(f"\nFinale kalan takımlar\n{final}\n\nFinal maçı için enter tuşuna basınız..")
        s=ust_tura_gecenler(final)
        input(f"\nŞampiyon olan takım\n{s}\n\nAna ekrana dönmek için enter tuşuna basınız..")
        kaydet=True

while True:
    os.system('cls')
    secim=input("****Şampiyonlar Ligi****\n1-Takımları Kaydet\n2-Takımları Listele\n3-Elemeleri Başlat\n4-Çıkış\nSeçiminiz : ")
    if secim=="1":
        takim_kaydet()
    elif secim=="2":
        takim_listele()
    elif secim=="3":
        eslesme_baslat()
    elif secim=="4":
        break
    else:
        input("Lütfen geçerli bir seçenek seçiniz...")
    