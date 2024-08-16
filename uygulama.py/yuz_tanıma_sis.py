import cv2

# Kameradan görüntü almak için VideoCapture nesnesini oluştur
vid = cv2.VideoCapture(0)

# Yüz algılama için CascadeClassifier nesnesini oluştur
yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = vid.read()
    
    if not ret:
        break

    # Görüntüyü gri tona dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    yuzler = yuz_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Algılanan yüzlerin sayısını yazdır
    print('Algılanan yüzler : ', len(yuzler))

    for (x, y, w, h) in yuzler:
        # Algılanan yüzün etrafına dikdörtgen çiz
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Sonuçları göster
    cv2.imshow('Yuz Tanima Sistemi', frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak ve pencereleri kapat
vid.release()
cv2.destroyAllWindows()


