def sıralama(dizi): ### def degiskeniyle sıralama adında bir fonksiyon olusturup diziyi parametre olarak verdim
    uzunluk = len(dizi) ### yazdırdıgımız listenin uzunlugunu alıyoruz 

    for i in range(uzunluk):  ###burada (0,u-1) yapmamızın sebebi i nin listenin 0.indeksinden itibaren karsılastırmaya baslayıp, listenin uzunlugundan bir eksigine kadar karsılastırması bunu yapmamızın sebebi buble sort un ikili karsılastırması son elemana geldignde karsılastırcak baska eleman olmadıgı icin -1 vermemiz.
        
        for j in range(0, uzunluk-i-1): ###burada yeni bir dongu olusturuyoruz, j degerine i+1 degerini veriyoruz cunku i degeri bir indeksi tutarken, j ise diger indekslerle karsılastırma yapıyor.
            
            if dizi[j]>dizi[i+1]:###buble sort yaptıgımız icin ikili karsılastırma yapıyoruz ve min degerini ekledigimiz i yi j ile karsılastırıyoruz j i den kucukse kodumuz devam ediyor.
                dizi[j], dizi[j+1] = dizi[j+1], dizi[j]
    return dizi
                
k_sayısı = input("sıralamak istediginiz sayıları aralarına bosluk koyarak giriniz : ")
dizi = list(map(int,k_sayısı.split()))

sıralanmıs_kelimeler = sıralama(dizi)

print(f"sıralanmış sayılar \n {sıralanmıs_kelimeler}")
