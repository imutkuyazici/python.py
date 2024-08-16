#asal sayı

sayi=int(input("bir sayı giriniz : "))

if sayi > 1 :
        for i in range(2,sayi) :
            if (sayi % i) == 0 :
                print(sayi,"asal sayı değildir !")
                break
        else :
            print(sayi,"asal sayıdır")   
else :
    print(sayi,"asal sayı değildir")

