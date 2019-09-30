#include <Arduino.h>
#include <AccelStepper.h>
#include <MultiStepper.h>
#include <Pompes.h>
#include <String.h>

void setup() {
  Serial.begin(9600);
  //Config driver 1,2,4,5,6 LOW et 3 HIGH
}
void loop()
{
  String message="";
  message=Serial.read();


  if (message[0]=='F')
  {
    while (message[0]!='S')
    {
      message=Serial.read();
      ForceP(message[1]);
    }
  }


  if (message[0]=='R')
  {
    while (message[0]!='S')
    {
      message=Serial.read();
      ReverseP(message[1]);
    }
  }

  if (message[0]=='P')
  {
    Pompe(message);
    Serial.println("ok"); 
  }




}
