#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#define POTE01 36

BluetoothSerial SerialBT;

void setup() {
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
}

void loop() {
  readPote();
  delay(20);
}

void readPote() {
  int x = map(analogRead(POTE01), 0, 4095, 0, 100);
  SerialBT.println(String(x));
}
