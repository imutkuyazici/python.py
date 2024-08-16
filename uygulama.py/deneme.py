import cv2

# Yüz tanıma modelini yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Video akışını başlat
video_capture = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = video_capture.read()

    # Gri tonlamaya dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Her bir yüz için dikdörtgen çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Sonuçları göster
    cv2.imshow('Video', frame)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# İşlemi serbest bırak ve pencereleri kapat
video_capture.release()
cv2.destroyAllWindows()
