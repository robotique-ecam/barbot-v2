#include <Arduino.h>
#include <String.h>

int dis, dir, pas;

#define DirPompe1 22
#define PasPompe1 23
#define DisablePompe1 8

#define DirPompe2 26
#define PasPompe2 27
#define DisablePompe2 9

#define DirPompe3 32
#define PasPompe3 33
#define DisablePompe3 10

#define DirPompe4 34
#define PasPompe4 35
#define DisablePompe4 11

#define DirPompe5 38
#define PasPompe5 39
#define DisablePompe5 12

#define DirPompe6 44
#define PasPompe6 45
#define DisablePompe6 13

#define DirCarpet 46
#define PasCarpet 47
#define DisableCarpet 2

#define EnableGob 3
#define DirGob 4

void getPump(char num, int *dis, int *dir, int *pas) {
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
    case 'C':
      *dis = DisableCarpet;
      *dir = DirCarpet;
      *pas = PasCarpet;
      break;
  }
}

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
  long step=ml*10;
  for (int i=0;i<step;i++) {
    ForceP(n);
  }
}

void gobelet() {
  digitalWrite(EnableGob, HIGH);
  digitalWrite(DirGob, LOW);
  delay(3000);
  digitalWrite(DirGob, HIGH);
  delay(1000);
  digitalWrite(EnableGob, LOW);
  delay(1500);
}

int currentPos = 0;
void carpet(char num) {
  if(num == 'n') {
    switch(currentPos) {
      case 1:
        //Move from 1 to end
        for (int i=0;i<5000;i++) {
          ForceP('C');
        }
        break;
      case 2:
        //Move from 2 to end
        for (int i=0;i<2500;i++) {
          ForceP('C');
        }
        break;
    }
    currentPos = 0;
  }
  else if(num == '1' || num == '2' || num == '3') {
    switch(currentPos) {
      case 0:
        //Move from start to 1
        for (int i=0;i<2500;i++) {
          ForceP('C');
        }
        break;
      case 1:
        //Not move
        break;
      case 2:
        //Move from 2 to 1
        for (int i=0;i<2500;i++) {
          ReverseP('C');
        }
        break;
    }
    currentPos = 1;
  }
  else if(num == '4' || num == '5' || num == '6') {
    switch(currentPos) {
      case 0:
        //Move from start to 2
        for (int i=0;i<5000;i++) {
          ForceP('C');
        }
        break;
      case 1:
        //Move from 1 to 2
        for (int i=0;i<2500;i++) {
          ForceP('C');
        }
        break;
      case 2:
        //Not move
        break;
    }
    currentPos = 2;
  }
}
