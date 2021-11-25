int VRx = A0;
int VRy = A1;
int SW = A2;

int x = 0;
int y = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  x = map(analogRead(VRx), 0, 1023, -100, 100);
  y = map(analogRead(VRy), 0, 1023, -100, 100);

  Serial.print("Joystick X: ");
  Serial.println(x);
  Serial.print("Joystick Y: ");
  Serial.println(y);

  Serial.println("");
  delay(500);
}