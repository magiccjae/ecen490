#include "BMSerial.h"
#include "RoboClaw.h"

#define address1 0x80
#define address2 0x81

RoboClaw roboClaw1(3,4);
RoboClaw roboClaw2(5,6);


void setup() {
  Serial.begin(9600);
  Serial.print("setup\n");
  roboClaw1.begin(9600);
  roboClaw2.begin(9600);
}

void loop() {
  Serial.print("looping\n");
  roboClaw1.ForwardM1(address1,16); //start Motor1 forward at half speed
  roboClaw1.ForwardM2(address1,16); //start Motor2 forward at half speed  
  roboClaw2.ForwardM1(address2,16);
  delay(2000);
}
