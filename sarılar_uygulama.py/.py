def ebob(sayi1, sayi2):
    # En büyük ortak böleni bulan fonksiyon
    ebob = 1
    # 1'den başlayarak her sayıyı kontrol et
    for i in range(1, min(sayi1, sayi2) + 1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob = i  # Eğer bölen her iki sayıya da bölüyorsa, ebob'u güncelle
    return ebob

# Kullanıcıdan iki sayıyı giriş olarak al
sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# EBOB'u hesapla
sonuc = ebob(sayi1, sayi2)

# Sonucu ekrana yazdır
print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {sonuc}")
