sayi=int(input("Lütfen bir sayı giriniz : "))

def fibonacci(sayi):
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(2,sayi):
        c = a + b
        a = b
        b = c
        print(c)

fibonacci(sayi)

