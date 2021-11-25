int LED_R = 4;
int LED_G = 3;
int LED_B = 2;

void setup() {
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);
}

void loop() {
  digitalWrite(LED_R, HIGH);
  delay(500);
  digitalWrite(LED_R, LOW);
  digitalWrite(LED_G, HIGH);
  delay(500);
  digitalWrite(LED_G, LOW);
  digitalWrite(LED_B, HIGH);
  delay(500);
  digitalWrite(LED_B, LOW);
}
