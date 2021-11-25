byte bits = 16;
long maximum = pow(2, bits);
long number = 0;

void setup() {
  Serial.begin(9600);
  number = random(maximum);
  Serial.println(number);
}

void loop() {
  
}