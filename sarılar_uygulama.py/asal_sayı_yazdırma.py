# asal sayı yazdırma 

sayi=int(input("bir sayı giriniz : "))

if sayi > 1 :
    for i in range (2,sayi) :

        for j in range (2,i):
            if i%j==0 :
                print(f"{i} asal sayı değildir")
                break
        else:
            print(i,"asal sayıdır")

else :
    print(sayi," asal sayı değildir")