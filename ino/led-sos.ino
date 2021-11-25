void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  dot(); dot(); dot();
  dash(); dash(); dash();
  dot(); dot(); dot();
  Serial.println("SOS!");
  delay(1000);
}

void dot()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(250); 
  digitalWrite(LED_BUILTIN, LOW);
  delay(250); 
}

void dash()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000); 
  digitalWrite(LED_BUILTIN, LOW);
  delay(250); 
}
