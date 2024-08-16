# Yıldızların bulunduğu koordinatları belirleyelim
yıldız_konum = [
    (0, i) for i in range(10)
] + [
    (i, 0) for i in range(1, 7)
] + [
    (6, i) for i in range(1, 10)
] + [
    (i, 9) for i in range(1, 4)
] + [
    (3, i) for i in range(4, 10)
] + [
    (i, 4) for i in range(4, 7)
]

# Şeklin boyutlarını belirleyelim
satirlar = 7
sutunlar = 10

# Şekli çizmek için çift döngü kullanarak karakterleri yerleştirelim
for satir in range(satirlar):
    for col in range(sutunlar):
        if (satir, sutunlar) in yıldız_konum:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
