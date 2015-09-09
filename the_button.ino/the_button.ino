#define ON 1023

void setup() {
Serial.begin(9600); // set the baud rate
}
void loop() {
  int red_button = analogRead(A1);
  int safety = analogRead(A0);
  if((red_button == ON) && (safety == ON)){
    Serial.println("drop");
    delay(1000);
  }
  else if(red_button == ON){
    Serial.println("eject");
    delay(1000); // delay for 1/10 of a second
  }
  delay(100);
}
