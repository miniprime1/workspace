int soundSensor = A0;
int sensorValue = 0;
int counter = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(soundSensor);
  if (sensorValue >= 28) {
    counter += 1;
    Serial.print("Counter: ");
    Serial.println(counter);
    Serial.print("Sensor Value: ");
    Serial.println(sensorValue);
    Serial.print("Loudness: ");
    if (sensorValue <= 29) Serial.println("Low");
    else if (sensorValue <= 32) Serial.println("Medium");
    else Serial.println("High");
    Serial.println("");
    delay(200);
  }
}