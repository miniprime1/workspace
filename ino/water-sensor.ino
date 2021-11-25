int waterPin = A5;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(waterPin);
  Serial.print("Sensor Value: ");
  Serial.println(value);

  Serial.print("Water Level: ");
  if (value <= 450) {
    Serial.println("Low");
  }
  else if (value <= 600) {
    Serial.println("Middle");
  }
  else {
    Serial.println("High");
  }

  Serial.println("");
  delay(1000);
}
