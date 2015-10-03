void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  int input = analogRead(A1);
  Serial.println(input);
  delay(500);
  // put your main code here, to run repeatedly:

}
