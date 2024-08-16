import os

takimlar = []
kaydet = True

def sorgula(takim):
    if takim in takimlar:
        return False
    else:
        return True
    
def takim_kaydet():
    global kaydet
    os.system('cls')
    if kaydet:
        sayac = 1
        while sayac < 17:
            takim = input(f"{sayac}. Takım : ")
            if sorgula(takim):
                print(f"{takim} takımı kayıtlı.")
                continue            
            else:
                takimlar.append(takim)
                sayac += 1
        print(takimlar)
        kaydet = False
        input(f"\nTakımlar kaydedildi.\nAna ekrana dönmek için enter tuşuna basınız..")
        
    else:
        input(f"Takımlar kayıtlı.\nAna ekrana dönmek için enter tuşuna basınız..")   

def mac_sonucunu_belirle(takim1, takim2):
    while True:
        try:
            gol1 = int(input(f"{takim1} için gol sayısını girin: "))
            gol2 = int(input(f"{takim2} için gol sayısını girin: "))
            if gol1 == gol2:
                print("Beraberlik. Lütfen tekrar girin.")
            else:
                return (takim1 if gol1 > gol2 else takim2)
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal değer girin.")

def ust_tura_gecenler(takimlar):
    ust_tur = []
    while len(takimlar) != 0:
        takim1 = takimlar.pop(0)
        takim2 = takimlar.pop(0)
        kazanan = mac_sonucunu_belirle(takim1, takim2)
        ust_tur.append(kazanan)
        print(f"{takim1} ve {takim2} arasındaki maçı {kazanan} kazandı.\n")
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
        cf = ust_tura_gecenler(takimlar)        
        input(f"\nÇeyrek finale kalan takımlar\n{cf}\n\nÇeyrek final maçları için enter tuşuna basınız..")
        yf = ust_tura_gecenler(cf)        
        input(f"\nYarı finale kalan takımlar\n{yf}\n\nYarı final maçları için enter tuşuna basınız..")
        final = ust_tura_gecenler(yf)        
        input(f"\nFinale kalan takımlar\n{final}\n\nFinal maçı için enter tuşuna basınız..")
        s = ust_tura_gecenler(final)
        input(f"\nŞampiyon olan takım\n{s}\n\nAna ekrana dönmek için enter tuşuna basınız..")
        kaydet = True

while True:
    os.system('cls')
    secim = input("****Şampiyonlar Ligi****\n1-Takımları Kaydet\n2-Takımları Listele\n3-Elemeleri Başlat\n4-Çıkış\nSeçiminiz : ")
    if secim == "1":
        takim_kaydet()
    elif secim == "2":
        takim_listele()
    elif secim == "3":
        eslesme_baslat()
    elif secim == "4":
        break
    else:
        input("Lütfen geçerli bir seçenek seçiniz...")
