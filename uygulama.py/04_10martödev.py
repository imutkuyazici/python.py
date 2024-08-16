#basamak degeri bulma
"""
# Kullanıcıdan sayıyı al
sayi = int(input("Bir sayı girin: "))

# Sayının basamak değerlerini bul
basamaklar = []
while sayi > 0:
    basamaklar.append(sayi % 10)
    sayi //= 10

# Basamak değerlerini ekrana yazdır
print("Girdiğiniz sayının basamakları:")
for basamak in reversed(basamaklar):
    print(basamak)
"""

#buble sort sıralama
"""
def bubble_sort(liste):
    n = len(liste)
    while True:
        siralandi = True
        for i in range(n-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                siralandi = False
        if siralandi:
            break
        n -= 1 


sayilar = []
while True:
    sayi = input("Bir sayı girin (bitirmek için 'q' tuşuna basın): ")
    if sayi.lower() == 'q':
        break
    try:
        sayilar.append(int(sayi))
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")

bubble_sort(sayilar)

print("Sıralanmış liste:", sayilar)

"""

#selection sort 
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min_index = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)

numbers = input("Sıralanacak sayıları girin (virgülle ayırarak): ").split(',')
numbers = [int(num) for num in numbers]

selection_sort(numbers)

print("Sıralanmış sayılar:", numbers)

"""