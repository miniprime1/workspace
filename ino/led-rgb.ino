int LED_R = 4; // 0x100
int LED_G = 3; // 0x011
int LED_B = 2; // 0x010

int COUNT = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);
}

void on(int R, int G, int B, int T) {
  analogWrite(LED_R, R);
  analogWrite(LED_G, G);
  analogWrite(LED_B, B);
  delay(T);
  off();
}

void off() {
  analogWrite(LED_R, 0);
  analogWrite(LED_G, 0);
  analogWrite(LED_B, 0);
}

void loop() {
  COUNT++;
  Serial.println("Red!");
  on(255, 0, 0, 1500); // Red, 1sec
  Serial.println("Green!");
  on(0, 255, 0, 1500); // Green, 1sec
  Serial.println("Blue!");
  on(0, 0, 255, 1500); // Blue, 1sec
  if (COUNT==10) {exit(0);}
}
