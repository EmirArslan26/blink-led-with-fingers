# ✋ Blink LED with Fingers

## 🔹 Description
This project uses **Python (OpenCV & MediaPipe)** to detect the number of fingers shown in front of a webcam. The detected number is sent via serial communication to an **Arduino**, which blinks LEDs based on the number of fingers.

## 🎥 Demo Video
[▶️ Watch on YouTube](https://youtu.be/ioeAbMgI5Z4?si=g6BzvEMV0ycUenil)

## 🛠️ Technologies Used
- Python
  - OpenCV
  - MediaPipe
  - PySerial
- Arduino
- Webcam (`cv2.VideoCapture(0)`)

## ⚙️ How It Works
1. Webcam captures hand movements in real-time.
2. Python detects the number of open fingers.
3. Sends that number to Arduino via serial.
4. Arduino blinks the LEDs accordingly.

## 🚀 How to Run
```bash
pip install opencv-python mediapipe pyserial
python main.py
```
Upload the Arduino sketch, connect via USB, and show your fingers to the camera.

## 📬 Contact
- Email: emirarslan0026@gmail.com

---

# 🇹🇷 Parmaklarla LED Yakma Projesi

## 🔹 Açıklama
Bu projede, **Python (OpenCV & MediaPipe)** ile kameradan parmak sayısı algılanır. Algılanan sayı, serial port üzerinden **Arduino**'ya gönderilir ve Arduino bu sayıya göre LED'leri yakar.

## 🎥 Demo Videosu
[▶️ YouTube'da İzle](https://youtu.be/ioeAbMgI5Z4?si=g6BzvEMV0ycUenil)

## 🛠️ Kullanılan Teknolojiler
- Python
  - OpenCV
  - MediaPipe
  - PySerial
- Arduino
- Webcam (`cv2.VideoCapture(0)`)

## ⚙️ Nasıl Çalışır
1. Kamera, el hareketlerini gerçek zamanlı algılar.
2. Python açık parmak sayısını tespit eder.
3. Sayıyı serial port ile Arduino'ya gönderir.
4. Arduino, gelen sayıya göre LED’leri yakar.

## 🚀 Çalıştırma Adımları
```bash
pip install opencv-python mediapipe pyserial
python main.py
```
Arduino kodunu yükle, USB ile bağla ve elini kameraya göster 😊

## 📬 İletişim
- E-posta: emirarslan0026@gmail.com
