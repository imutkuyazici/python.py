#selection sort
"""
#ilk önce bir tane liste tanımlıyoruz, listeye bir isim veriyoruz.
slar=[23,65,24,12,0,958,-158]
#listeyi tanımladıktan sonra, burada len fonksiyonuyla listenin uzunlugunu ölcüyoruz.
u=len(slar)


for i in range (0,u-1):#burada i degeri listenin 0.indeksinden baslayarak butun indekslere deger verir.
    min=i #listenin min. degerini i olarak belirtiyoruz.
    for j in range(i+1,u) :#burada yeni bir dongu olusturuyoruz, j degerine i+1 degerini veriyoruz cunku i degeri bir indeksi tutarken, j ise diger indekslerle karsılastırma yapıyor.
        if slar[min]>slar[j]:#slar adını verdigimiz listenin minimum degeri ile j yi karsılastırıyoruz.
            min=j#egerki j min degerden kucuk ise j yi min e atıyoruz
    y=slar[i]#listenin ilk indeksindeki sayıyı yedek degiskenine atıyoruz
    slar[i]=slar[min]#listenin ilk indeksine min degerini veriyoruz
    slar[min]=y#daha sonra min degerini yedek degiskenine atıyoruz
    print(slar)#son olarak listeyi yazdırıyoruz

print("sıralanmıs liste : ",slar)#buda bizim sıralanmıs listemiz
"""
#buble sort



liste=[6,4,5,1,3,2]#ilk önce bir tane liste tanımlıyoruz, listeye bir isim veriyoruz.

def buble_sort(liste) :#burada def komutuyla bir buble_sort adında bir fonksiyon olusturuyoruz
    for i in range (0,u-1):#burada (0,u-1) yapmamızın sebebi i nin listenin 0.indeksinden itibaren karsılastırmaya baslayıp, listenin uzunlugundan bir eksigine kadar karsılastırması bunu yapmamızın sebebi buble sort un ikili karsılastırması son elemana geldignde karsılastırcak baska eleman olmadıgı icin -1 vermemiz.
        min=i#burada i yi min degerine atıyoruz
        for j in range(i+1,u) :#burada yeni bir dongu olusturuyoruz, j degerine i+1 degerini veriyoruz cunku i degeri bir indeksi tutarken, j ise diger indekslerle karsılastırma yapıyor.
            u=len(liste)#listeyi tanımladıktan sonra, burada len fonksiyonuyla listenin uzunlugunu ölcüyoruz.
            if liste[j]<liste[i]:#buble sort yaptıgımız icin ikili karsılastırma yapıyoruz ve min degerini ekledigimiz i yi j ile karsılastırıyoruz j i den kucukse kodumuz devam ediyor.
                yedek=liste[i]#buldugumuz min i degerini yedek fonksiyonuna atıyoruz
                liste[i]=liste[j]#listenin j. degerini , listenin i. degerine atıyoruz
                liste[j]=yedek#j degerini i degerine atadıktan sonra j degerini yedek fonksiyonuna ekliyoruz
                print("sıralanmıs liste : ",liste)# son olarak listenin son halini yazdırıyoruz.

#insertion sort
"""
def insertion_sort(arr):
    # Dizinin her elemanını dolaşacak bir döngü oluşturuyoruz.
    for i in range(1, len(arr)):
        # Dizinin i. elemanını key olarak belirliyoruz.
        k = arr[i]
        # Bu anahtarın, dizideki doğru konumunu bulmak için j değişkenini kullanıyoruz.
        j = i - 1
        # Dizinin doğru konumunu bulmak için geriye doğru bir döngü başlatıyoruz.
        # Anahtarın konumunu bulmak için diziyi sıralı bir şekilde ilerliyoruz.
        while j >= 0 and k < arr[j]:
            # Eğer bir önceki eleman, anahtardan daha büyükse,
            # bu elemanı bir sağa kaydırıyoruz.
            arr[j + 1] = arr[j]
            # Daha önceki elemanlarla karşılaştırmak için j'yi bir azaltıyoruz.
            j -= 1
        # Anahtarı doğru konumuna yerleştiriyoruz.
        arr[j + 1] = k

# Örnek kullanım:
sıralanmıs = [5, 2, 4, 6, 1, 3]
# insertion_sort fonksiyonunu kullanarak diziyi sıralıyoruz.
insertion_sort(sıralanmıs)
# Sıralanmış diziyi ekrana yazdırıyoruz.
print("Sıralanmış dizi:", sıralanmıs)
"""































































