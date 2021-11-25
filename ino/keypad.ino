#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;

char KEYS[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte COL_PINS[ROWS] = {5, 4, 3, 2};
byte ROW_PINS[COLS] = {9, 8, 7, 6};

Keypad customKeypad = Keypad(makeKeymap(KEYS), ROW_PINS, COL_PINS, ROWS, COLS);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char button = customKeypad.getKey();
  if (button) {
    Serial.println(button);
  }
}
