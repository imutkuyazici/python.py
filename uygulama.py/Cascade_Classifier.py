import cv2

# Yüz algılama için CascadeClassifier nesnesini oluştur
yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cascade Classifier yüklendi mi kontrol et
if yuz_cascade.empty():
    print("Hata: Cascade Classifier yüklenemedi!")
else:
    print("Cascade Classifier başarıyla yüklendi.")

