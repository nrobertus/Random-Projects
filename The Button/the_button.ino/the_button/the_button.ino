#define BTN_PRESSED 1000
#define SAFETY_OFF 1000

void setup() {
Serial.begin(9600); // set the baud rate
}
void loop() {
  int red_button = analogRead(A1);
  int safety = analogRead(A0);

  if((red_button > BTN_PRESSED) && (safety > SAFETY_OFF)){
    Serial.println("eject");
    delay(1000);
  }
  else if(red_button > BTN_PRESSED){
    Serial.println("drop");
    delay(1000);
  }
  delay(500);
}
