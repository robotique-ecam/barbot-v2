#include <Arduino.h>
#include <AccelStepper.h>
#include <String.h>

#define DirPompe1 30
#define PasPompe1 31
#define DisablePompe1 8

#define DirPompe2 32
#define PasPompe2 33
#define DisablePompe2 9

#define DirPompe3 34
#define PasPompe3 35
#define DisablePompe3 10

#define DirPompe4 36
#define PasPompe4 37
#define DisablePompe4 11

#define DirPompe5 38
#define PasPompe5 39
#define DisablePompe5 12

#define DirPompe6 40
#define PasPompe6 41
#define DisablePompe6 13

#define DirCarpet 00
#define PasCarpet 000
#define motorInterfaceType 00 */

//AccelStepper stepper1 = AccelStepper(motorInterfaceType,PasCarpet,DirCarpet);

void ForceP(char num) {
  if (num=='1') {
    digitalWrite(DisablePompe1,LOW);
    digitalWrite(DirPompe1,HIGH);
    digitalWrite(PasPompe1,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe1,LOW);
    delayMicroseconds(500);
  }
  else if (num=='2') {
    digitalWrite(DisablePompe2,LOW);
    digitalWrite(DirPompe2,HIGH);
    digitalWrite(PasPompe2,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe2,LOW);
    delayMicroseconds(500);
  }
  else if (num=='3') {
    digitalWrite(DisablePompe3,LOW);
    digitalWrite(DirPompe3,HIGH);
    digitalWrite(PasPompe3,HIGH);
    delayMicroseconds(100);
    digitalWrite(PasPompe3,LOW);
    delayMicroseconds(100);
  }
  else if (num=='4') {
    digitalWrite(DisablePompe4,LOW);
    digitalWrite(DirPompe4,HIGH);
    digitalWrite(PasPompe4,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe4,LOW);
    delayMicroseconds(500);
  }
  else if (num=='5') {
    digitalWrite(DisablePompe5,LOW);
    digitalWrite(DirPompe5,HIGH);
    digitalWrite(PasPompe5,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe5,LOW);
    delayMicroseconds(500);
  }
  else if (num=='6') {
    digitalWrite(DisablePompe6,LOW);
    digitalWrite(DirPompe6,HIGH);
    digitalWrite(PasPompe6,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe6,LOW);
    delayMicroseconds(500);
  }
}

void ReverseP(char num) {
  if (num=='1') {
    digitalWrite(DisablePompe1,LOW);
    digitalWrite(DirPompe1,LOW);
    digitalWrite(PasPompe1,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe1,LOW);
    delayMicroseconds(500);
  }
  else if (num=='2') {
    digitalWrite(DisablePompe2,LOW);
    digitalWrite(DirPompe2,LOW);
    digitalWrite(PasPompe2,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe2,LOW);
    delayMicroseconds(500);
  }
  else if (num=='3') {
    digitalWrite(DisablePompe3,LOW);
    digitalWrite(DirPompe3,LOW);
    digitalWrite(PasPompe3,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe3,LOW);
    delayMicroseconds(500);
  }
  else if (num=='4') {
    digitalWrite(DisablePompe4,LOW);
    digitalWrite(DirPompe4,LOW);
    digitalWrite(PasPompe4,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe4,LOW);
    delayMicroseconds(500);
  }
  else if (num=='5') {
    digitalWrite(DisablePompe5,LOW);
    digitalWrite(DirPompe5,LOW);
    digitalWrite(PasPompe5,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe5,LOW);
    delayMicroseconds(500);
  }
  else if (num=='6') {
    digitalWrite(DisablePompe6,LOW);
    digitalWrite(DirPompe6,LOW);
    digitalWrite(PasPompe6,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe6,LOW);
    delayMicroseconds(500);
  }
}

void disablePump(char num) {
  if (num=='1') {
    digitalWrite(DisablePompe1,HIGH);
  }
  else if (num=='2') {
    digitalWrite(DisablePompe2,HIGH);
  }
  else if (num=='3') {
    digitalWrite(DisablePompe3,HIGH);
  }
  else if (num=='4') {
    digitalWrite(DisablePompe4,HIGH);
  }
  else if (num=='5') {
    digitalWrite(DisablePompe5,HIGH);
  }
  else if (num=='6') {
    digitalWrite(DisablePompe6,HIGH);
  }
}

void Pompe(char* message) {
  long ml = 0;
  ml = atoi(message + 3);
  char n = message[1];
  long step=ml*3200;

  for (int i=0;i<step;i++) {
    ForceP(n);
  }
}


/*
void Carpet(String message) {
  int step=0;
  step=message.substring(3).toInt();

  stepper1.setMaxSpeed(6000);
  stepper1.setAcceleration(12000);
  stepper1.moveTo(step);

  for (int i=0;i<step;i++) {
    if (stepper1.distanceToGo() == 0)
      stepper1.moveTo(-stepper1.currentPosition());
    stepper1.run();
  }
}
*/
