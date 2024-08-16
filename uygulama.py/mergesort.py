# Merge Sort 


def merge_sort(arr):
    # Dizi bir veya daha az elemana sahipse, zaten sıralıdır, bu yüzden diziyi doğrudan döndür.
    if len(arr) <= 1:
        return arr
    
    # Diziyi ikiye bölmek için orta noktayı bul.
    mid = len(arr) // 2
    
    # Diziyi ikiye bölerken sol ve sağ alt dizileri oluştur.
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Sol ve sağ alt dizileri için merge_sort fonksiyonunu tekrar çağırarak her alt diziyi sırala.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Sıralanmış alt dizileri birleştir ve döndür.
    return merge(left_half, right_half)

def merge(left, right):
    # Birleştirilmiş sonucu depolamak için bir liste oluştur.
    result = []
    # Sol ve sağ diziler için indeksler oluştur.
    left_idx, right_idx = 0, 0
    
    # Her iki alt dizi de eleman içerdiği sürece döngüyü çalıştır.
    while left_idx < len(left) and right_idx < len(right):
        # Sol dizinin mevcut elemanı sağ dizinin mevcut elemanından küçükse, sol elemanı sonuca ekle ve sol indeksi artır.
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        # Aksi halde sağ dizinin mevcut elemanını sonuca ekle ve sağ indeksi artır.
        else:
            result.append(right[right_idx])
            right_idx += 1
                
    # Bir dizinin elemanları tükenene kadar devam eden birleştirme işleminden sonra, kalan elemanları sonuca ekle.
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    # Birleştirilmiş sonucu döndür.
    return result

# Örnek kullanım:
arr = [3, 7, 2, 8, 1, 5, 4, 6]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
