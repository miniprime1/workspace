// Required Library: "DHT sensor library (Adafruit)", "Adafruit Unified Sensor (Adafruit)"
#include <DHT.h>

DHT dhtSensor(A5, DHT11);

void setup() {
  Serial.begin(9600);
  dhtSensor.begin();
}

void loop() {
  int temp = dhtSensor.readTemperature();
  int humi = dhtSensor.readHumidity();

  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println("C (Error: +/-2)");

  Serial.print("Humidity: ");
  Serial.print(humi);
  Serial.println("RH (Error: +/-5)");

  Serial.println("");
  delay(5000);
}
