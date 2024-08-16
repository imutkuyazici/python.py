def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    else:
        return x / y

print("Lütfen işlem yapmak istediğiniz iki sayıyı girin:")

sayi1 = float(input("Birinci sayı: "))
sayi2 = float(input("İkinci sayı: "))


print("İşlem Seçenekleri:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")

if secim == '1':
    print("Toplama sonucu:", toplama(sayi1, sayi2))
elif secim == '2':
    print("Çıkarma sonucu:", cikarma(sayi1, sayi2))
elif secim == '3':
    print("Çarpma sonucu:", carpma(sayi1, sayi2))
elif secim == '4':
    print("Bölme sonucu:", bolme(sayi1, sayi2))
else:
    print("Geçersiz giriş!")
