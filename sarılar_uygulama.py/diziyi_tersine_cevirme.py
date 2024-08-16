def dizi_ters_cevir(dizi):
    ters_dizi = dizi[::-1]
    return ters_dizi

# Kullanıcıdan diziyi al
dizi = input("Lütfen bir dizi veya kelime girin: ")

# Diziyi ters çevir
ters_dizi = dizi_ters_cevir(dizi)

# Sonucu ekrana yazdır
print("Girdiğiniz dizi/kelimenin ters çevrilmiş hali:", ters_dizi)
