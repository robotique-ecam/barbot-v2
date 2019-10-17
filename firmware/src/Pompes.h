#include <Arduino.h>
#include <AccelStepper.h>
#include <String.h>

int dis, dir, pas;

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
  getPump(num, &dis, &dir, &pas);
  digitalWrite(dis,LOW);
  digitalWrite(dir,HIGH);
  digitalWrite(pas,HIGH);
  delayMicroseconds(500);
  digitalWrite(pas,LOW);
  delayMicroseconds(500);
}

void ReverseP(char num) {
  getPump(num, &dis, &dir, &pas);
  digitalWrite(dis,LOW);
  digitalWrite(dir,LOW);
  digitalWrite(pas,HIGH);
  delayMicroseconds(500);
  digitalWrite(pas,LOW);
  delayMicroseconds(500);
}

void disablePump(char num) {
  getPump(num, &dis, &dir, &pas);
  digitalWrite(dis,HIGH);
}

void Pompe(char* message) {
  long ml = 0;
  ml = atoi(message + 3);
  char n = message[1];
  long step=ml*50;
  //Serial.println("Enabling Pump " + message[1] + " for " + step + "ml...");
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

int getPump(char num, int *dis, int *dir, int *pas) {
  switch(num) {
    case '1':
      *dis = DisablePompe1;
      *dir = DirPompe1;
      *pas = PasPompe1;
      break;
    case '2':
      *dis = DisablePompe2;
      *dir = DirPompe2;
      *pas = PasPompe2;
      break;
    case '3':
      *dis = DisablePompe3;
      *dir = DirPompe3;
      *pas = PasPompe3;
      break;
    case '4':
      *dis = DisablePompe4;
      *dir = DirPompe4;
      *pas = PasPompe4;
      break;
    case '5':
      *dis = DisablePompe5;
      *dir = DirPompe5;
      *pas = PasPompe5;
      break;
    case '6':
      *dis = DisablePompe6;
      *dir = DirPompe6;
      *pas = PasPompe6;
      break;
  }
}
