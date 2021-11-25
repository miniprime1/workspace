int flameSensor = A0;
int sensorValue = 0;

void setup() {
  Serial.begin(9600);
  pinMode(flameSensor, INPUT);
}

void loop() {
  sensorValue = analogRead(flameSensor);

  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  Serial.print("Fire Detection: ");
  if (sensorValue) Serial.println("True(Detected)");
  else Serial.println("False(Not-Detected)");

  Serial.println("");
  delay(500);
}
