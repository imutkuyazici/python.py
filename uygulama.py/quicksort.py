# quick sort

def quick_sort(arr):
    # Dizi boş veya tek elemanlı ise, diziyi doğrudan döndürüyoruz.
    if len(arr) <= 1:
        return arr
    
    # Pivot elemanı seçiyoruz. Bu örnekte, dizinin ortasındaki elemanı seçiyoruz.
    pivot = arr[len(arr) // 2]
    
    # Pivot elemanından küçük, pivot elemanına eşit ve pivot elemanından büyük olan alt dizileri oluşturuyoruz.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Sol, orta ve sağ alt dizileri quick_sort fonksiyonunu tekrar çağırarak sıralı hale getiriyoruz.
    return quick_sort(left) + middle + quick_sort(right)

# Örnek kullanım:
my_array = int(input("bir dizi giriniz (virgulle ayırarak) : "))
# quick_sort fonksiyonunu kullanarak diziyi sıralıyoruz.
sorted_array = quick_sort(my_array)
print("Sıralanmış dizi:", sorted_array)
