#define POT_PIN A3
#define SDA_PIN A4
#define SDA_PIN A5
#define ADDR 0x8

#include <Wire.h>

void envia(){
  int potVal = analogRead(POT_PIN);
  Serial.flush();
  Serial.print("Enviando: ");
  Serial.println(potVal);
  //  Wire.write(0x01);
  Wire.write(highByte(potVal));
  Wire.write(lowByte(potVal));
  
}

void setup() {
  Serial.begin(9600);
  Wire.begin(ADDR);
  Wire.onRequest(envia);
}

void loop() {
  delay(100);
}

// void receive(int a){
//   if(Wire.available()){
//     char c = Wire.read();
//     Serial.print(c, BIN);
//     Serial.print(" ");
//     Serial.println(c, HEX);
//   }
// }

// void setup(){
//   Serial.begin(9600);
//   Wire.begin(ADDR);
//   Wire.onReceive(receive);
// }

// void loop(){
//   delay(100);
// }