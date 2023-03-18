#define POTE01 A0

void setup() {
  Serial.begin(9600);
}

void loop() {
  readPote();
}

void readPote() {
  int x = map(analogRead(POTE01), 0, 1023, 0, 100);
  Serial.println(String(x));
}
