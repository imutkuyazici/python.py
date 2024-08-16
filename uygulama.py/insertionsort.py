def sıralama(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_arrey = list(map(int, input("Sıralamak istediğiniz sayıları aralarına boşluk koyarak giriniz: ").split()))

sıralama(my_arrey)

print("Sıralanmış dizi:", my_arrey)
