"""
def sıralama(dizi):  ### sıralama adında bir fonksiyon olusturduk
    n = len(dizi)  ### ikili sıralama yapılacagı icin listenin uzunlugunu aldık
    
    for i in range(n):   ###i'nin 0'dan n-1'e kadar değerler almasını saglıyoruz
        for j in range(0, n-i-1):
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
    return dizi

kullanıcı_sayısı = input("Sıralamak için sayıları aralarına boşluk koyarak girin: ")
dizi = list(map(int, kullanıcı_sayısı.split())) ###user_input.split() ifadesi, kullanıcı girişini boşluklardan ayırarak bir liste oluşturur.
                                                ###map(int, user_input.split()) ifadesi, bu liste elemanlarını int (tam sayı) tipine dönüştürür.
                                                ###list(...) ifadesi, bu tam sayıları içeren bir liste oluşturur.

sıralanmıs_kelimeler = sıralama(dizi)   
print(f"sıralanmıs sayılar : \n\n {sıralanmıs_kelimeler}")

"""

def sıralama(dizi):
    
    uzunluk=len(dizi)
    
    for i in range(uzunluk):
        for j in range(0,uzunluk-i-1):
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
    return dizi  

dizi1=input("birinci diziyi girin (virgulle ayırarak) : ")
dizi2=input("ikinci diziyi girin (virgulle ayırarak) : ")

liste1 = [int(x) for x in dizi1.split(',')] ### '2' , '3' , '5'  ==== x degiskenine ata integer degerine donustur
liste2 = [int(x) for x in dizi2.split(',')]

 
toplu_liste=liste1+liste2 ##listeyi birlestirilmesi 

sıralanmıs_liste = sıralama(toplu_liste)  ##sıralanmıs listeyi sıralama fonskiyonuna toplu listeyi parametre vererek hesaplandı
print("\n")
print(f"sıralanmıs liste \n\n {sıralanmıs_liste} \n")  ##ekrana yazdırma

