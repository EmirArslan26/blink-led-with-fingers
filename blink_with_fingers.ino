int led_pins[] = {2, 3, 4, 5, 6}; // LED'lerin bağlı olduğu pinler
int led_number = 5;               // Toplam LED sayısı
char gelenveri = 0;                // Seri porttan gelen veri

void setup() {
  Serial.begin(9600);             // Seri iletişimi başlat
  for (int i = 0; i < led_number; i++) {
    pinMode(led_pins[i], OUTPUT); // LED pinlerini çıkış olarak ayarla
    digitalWrite(led_pins[i], LOW); // Başlangıçta tüm LED'leri söndür
  }
}

void loop() {
  if (Serial.available() > 0) {
    gelenveri = Serial.read(); // Seri porttan gelen sayıyı oku
    Serial.print("Gelen Veri: ");  // Gelen veriyi seri monitöre yazdır
    Serial.println(gelenveri);

    if (gelenveri == '1'){
      digitalWrite(led_pins[0],1);
      digitalWrite(led_pins[1],0);
      digitalWrite(led_pins[2],0);
      digitalWrite(led_pins[3],0);
      digitalWrite(led_pins[4],0);
    }
    if (gelenveri == '2'){
      digitalWrite(led_pins[0],1);
      digitalWrite(led_pins[1],1);
      digitalWrite(led_pins[2],0);
      digitalWrite(led_pins[3],0);
      digitalWrite(led_pins[4],0);
    }
    if (gelenveri == '3'){
      digitalWrite(led_pins[0],1);
      digitalWrite(led_pins[1],1);
      digitalWrite(led_pins[2],1);
      digitalWrite(led_pins[3],0);
      digitalWrite(led_pins[4],0);
    }
    if (gelenveri == '4'){
      digitalWrite(led_pins[0],1);
      digitalWrite(led_pins[1],1);
      digitalWrite(led_pins[2],1);
      digitalWrite(led_pins[3],1);
      digitalWrite(led_pins[4],0);
    }
    if (gelenveri == '5'){
      digitalWrite(led_pins[0],1);
      digitalWrite(led_pins[1],1);
      digitalWrite(led_pins[2],1);
      digitalWrite(led_pins[3],1);
      digitalWrite(led_pins[4],1);
    }
    if (gelenveri == '0'){
      digitalWrite(led_pins[0],0);
      digitalWrite(led_pins[1],0);
      digitalWrite(led_pins[2],0);
      digitalWrite(led_pins[3],0);
      digitalWrite(led_pins[4],0);
    }
  }
}