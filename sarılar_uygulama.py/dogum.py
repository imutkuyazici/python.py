from datetime import datetime

dogum = input("Dogum tarihinizi giriniz (GG/AA/YYYY) : ")

dogum2 = datetime.strptime(dogum, "%d/%m/%Y")

bugun = datetime.now()

yas = bugun - dogum2

print("Yaşadığınız saniye:", yas.total_seconds())
