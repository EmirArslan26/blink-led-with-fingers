import cv2  # OpenCV kütüphanesi, görüntü işleme için kullanılır.
import mediapipe as mp  # Mediapipe kütüphanesi, el tespiti ve landmark (nokta) çıkarma için kullanılır.
import serial  # Seri haberleşme için kullanılır (örneğin, Arduino ile iletişim).
import time  # Zamanla ilgili işlemler için kullanılır.

# Mediapipe'in el tespiti ve çizim araçlarını yükle.
mp_el = mp.solutions.hands
mp_cizim = mp.solutions.drawing_utils

# Kamera bağlantısını başlat. 0, varsayılan kamera anlamına gelir.
kamera = cv2.VideoCapture(0)

# Seri haberleşme başlatılır. "COM3" portu ve 9600 baud rate ile.
with serial.Serial("COM3", 9600) as ser:
    time.sleep(2)  # Seri haberleşmenin başlaması için 2 saniye beklenir.

    # Mediapipe el tespiti modelini başlat. 
    # min_tracking_confidence ve min_detection_confidence, tespit ve takip hassasiyetini belirler.
    # max_num_hands = 1, sadece bir elin tespit edilmesini sağlar.
    with mp_el.Hands(min_tracking_confidence=0.6, min_detection_confidence=0.6, max_num_hands=1) as el:
        while kamera.isOpened():  # Kamera açık olduğu sürece döngü devam eder.
            basari, resim = kamera.read()  # Kameradan bir kare okunur.
            if not basari:  # Eğer kameraya bağlanılamazsa döngüden çıkılır.
                print("kameraya bağlanılamıyor")
                break

            # Görüntüyü BGR formatından RGB formatına çevir (Mediapipe RGB formatını kullanır).
            resim_RGB = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

            # El landmark'larını tespit et.
            sonuc = el.process(resim_RGB)

            # Görüntünün boyutlarını al.
            yukseklik, genişlik, kanal = resim.shape

            # Landmark'ların X ve Y koordinatlarını saklamak için boş listeler oluştur.
            landmarks_Y = []
            landmarks_X = []

            # Eğer el tespit edilirse:
            if sonuc.multi_hand_landmarks:
                # İlk tespit edilen elin landmark'larını al.
                landmarks = sonuc.multi_hand_landmarks[0]

                # Landmark'ları ve bağlantıları görüntü üzerine çiz (isteğe bağlı, şu anda yorum satırında).
                # mp_cizim.draw_landmarks(resim, landmarks, mp_el.HAND_CONNECTIONS)

                # Her bir landmark için X ve Y koordinatlarını hesapla ve listelere ekle.
                for LM in landmarks.landmark:
                    x = LM.x * genişlik  # X koordinatını piksel cinsine çevir.
                    y = LM.y * yukseklik  # Y koordinatını piksel cinsine çevir.

                    landmarks_X.append(x)
                    landmarks_Y.append(y)

                # Elin sınırlarını belirlemek için minimum ve maksimum X ve Y değerlerini bul.
                min_Y = int(min(landmarks_Y))
                max_Y = int(max(landmarks_Y))
                max_X = int(max(landmarks_X))
                min_X = int(min(landmarks_X))

                # Elin etrafına bir dikdörtgen çiz.
                cv2.rectangle(resim, (min_X-15, min_Y-15), (max_X+15, max_Y+15), (0, 250, 100), 2)

                # Parmakların açık olup olmadığını kontrol etmek için boolean değişkenler oluştur.
                parmak_1 = False  # Başparmak
                parmak_2 = False  # İşaret parmağı
                parmak_3 = False  # Orta parmak
                parmak_4 = False  # Yüzük parmağı
                parmak_5 = False  # Serçe parmak

                # Parmakların açık olup olmadığını belirlemek için landmark'ların konumlarını karşılaştır.
                if landmarks_X[4] < landmarks_X[2]:  # Başparmak
                    parmak_1 = True
                if landmarks_Y[8] < landmarks_Y[6]:  # İşaret parmağı
                    parmak_2 = True
                if landmarks_Y[12] < landmarks_Y[10]:  # Orta parmak
                    parmak_3 = True
                if landmarks_Y[16] < landmarks_Y[14]:  # Yüzük parmağı
                    parmak_4 = True
                if landmarks_Y[20] < landmarks_Y[18]:  # Serçe parmak
                    parmak_5 = True

                # Eğer el ters çevrilmişse (başparmak diğer tarafa bakıyorsa), başparmak durumunu tersine çevir.
                if landmarks_X[20] < landmarks_X[4]:
                    parmak_1 = not parmak_1

                # Parmakların durumunu bir listeye ekle.
                parmaklar = [parmak_1, parmak_2, parmak_3, parmak_4, parmak_5]

                # Açık parmak sayısını say.
                acik_parmak_sayisi = 0
                if landmarks_Y[12] < landmarks_Y[0]:  # Eğer el yukarıda ise:
                    for parmak in parmaklar:
                        if parmak:  # Eğer parmak açıksa:
                            acik_parmak_sayisi += 1

                    # Açık parmak sayısını ekrana yazdır.
                    cv2.putText(resim, str(acik_parmak_sayisi), (50, 50), cv2.FONT_HERSHEY_PLAIN, 5, (250, 75, 0), 2)

                    # Açık parmak sayısını seri port üzerinden gönder.
                    ser.write(str(acik_parmak_sayisi).encode())

            # Görüntüyü ekranda göster.
            cv2.imshow("el algılama", resim)

            # 'q' tuşuna basılırsa döngüden çık ve programı sonlandır.
            if cv2.waitKey(5) & 0xFF == ord("q"):
                break