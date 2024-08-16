import random
import string

def rastgele_kelime_uret(uzunluk):
    harfler = string.ascii_lowercase + "ç,ğ,ı,ö,ş,ü"  # Türkçe karakterler de eklendi
    kelime = ''.join(random.choice(harfler) for _ in range(uzunluk))
    return kelime

# Rastgele kelime uzunluğu belirliyoruz (örneğin, 5 ile 10 harf arasında)
kelime_uzunlugu = random.randint(5, 10)
secili_kelime = rastgele_kelime_uret(kelime_uzunlugu)

tahmin_sayisi = 5
harfler = []  # Kullanıcının girdiği harfleri saklayacağımız liste
x = len(secili_kelime)
z = list('_' * x)
print(' '.join(z), end='\n')

while tahmin_sayisi > 0:
    harf = input("Bir harf giriniz: ").lower()

    if harf in harfler:
        print("Lütfen daha önce tahmin ettiğiniz harfleri tekrar girmeyiniz...")
        continue
    elif len(harf) > 1:
        print("Sadece bir harf girilebilir.")
        continue
    elif harf not in secili_kelime:  # Girilen harf kelime içinde yoksa
        tahmin_sayisi -= 1
        print(f"Harf kelimede yok! {tahmin_sayisi} tane tahmin hakkınız kaldı.")
    else:
        for i in range(len(secili_kelime)):
            if harf == secili_kelime[i]:
                z[i] = harf
        harfler.append(harf)
        print(' '.join(z), end='\n')

    if '_' not in z:  # Eğer kelimenin tüm harfleri bulunmuşsa
        print("Tebrikler! Kelimeyi doğru tahmin ettiniz!")
        break

    cevap = input("Kelimenin tamamını tahmin etmek istiyor musunuz? ['e' veya 'h']: ").lower()

    if cevap == "e":
        tahmin = input("Kelimenin tamamını tahmin edebilirsiniz: ").lower()
        if tahmin == secili_kelime:
            print("Tebrikler bildiniz!")
            break
        else:
            tahmin_sayisi -= 1
            print(f"Yanlış tahmin ettiniz. {tahmin_sayisi} tane tahmin hakkınız kaldı.")

if tahmin_sayisi == 0:
    print(f"Tahmin hakkınız kalmadı. Kaybettiniz! Adam asıldı. Kelime: {secili_kelime}")
