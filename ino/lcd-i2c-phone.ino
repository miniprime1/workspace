// Required Library: "LiquidCrystal I2C(Frank de Brabander)"
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
}

void loop() {
  lcd.setCursor(0, 0);
  lcd.print("Kyumin's Phone:");
  lcd.setCursor(0, 1);
  lcd.print("010-8809-4066");
}
