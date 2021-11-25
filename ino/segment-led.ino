// Title: 7 Segment LED
// Description: Display 0~9 on 7 Segment LED

int segmentLEDs[] = {2, 3, 4, 5, 6, 7, 8, 9};
int segmentLEDsNum = 8;

int digit[10][8] = {
  {0, 0, 0, 0, 0, 0, 1, 1}, // 0
  {1, 0, 0, 1, 1, 1, 1, 1}, // 1
  {0, 0, 1, 0, 0, 1, 0, 1}, // 2
  {0, 0, 0, 0, 1, 1, 0, 1}, // 3
  {1, 0, 0, 1, 1, 0, 0, 1}, // 4
  {0, 1, 0, 0, 1, 0, 0, 1}, // 5
  {0, 1, 0, 0, 0, 0, 0, 1}, // 6
  {0, 0, 0, 1, 1, 1, 1, 1}, // 7
  {0, 0, 0, 0, 0, 0, 0, 1}, // 8
  {0, 0, 0, 0, 1, 0, 0, 1}  // 9
};

void setup() {
  for (int i=0; i<segmentLEDsNum; i++) {
    pinMode(segmentLEDs[i], OUTPUT);
  }
}

void loop() {
  for (int i=0; i<10; i++) {
    for (int j=0; j<segmentLEDsNum; j++) {
      digitalWrite(segmentLEDs[j], digit[i][j]);
    }
  delay(1000);
  }
}
