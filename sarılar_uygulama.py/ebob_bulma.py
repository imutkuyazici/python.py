
def ebob(sayi1,sayi2):
    ebob = 1

    for i in range(1, min(sayi1,sayi2) +1 ) : #------>>>> 1 den baslayarak sayı1 veya sayı2 den hangisinin daha kucuk oldugunu 1er artırarak bulmaya yarayan kod
        if sayi1 % i == 0 and sayi2 % i == 0 :
            ebob = i
    return ebob


sayi1 = int(input("birinci sayıyı giriniz : "))
sayi2 = int(input("birinci sayıyı giriniz : "))

sonuc = ebob(sayi1,sayi2)
print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {sonuc}")

