#include <AccelStepper.h>
#include "Pompes.h"
#include <String.h>

char message[10];
void readSerial() {
  if(Serial.available()) {
    memset(message, 0, sizeof(message)); // Clear buffer
    Serial.readBytesUntil(';', message, 10);
  }
}

void setup() {
  pinMode(DirPompe1, OUTPUT);
  pinMode(PasPompe1, OUTPUT);
  pinMode(DirPompe2, OUTPUT);
  pinMode(PasPompe2, OUTPUT);
  pinMode(DirPompe3, OUTPUT);
  pinMode(PasPompe3, OUTPUT);
  pinMode(DirPompe4, OUTPUT);
  pinMode(PasPompe4, OUTPUT);
  pinMode(DirPompe5, OUTPUT);
  pinMode(PasPompe5, OUTPUT);
  pinMode(DirPompe6, OUTPUT);
  pinMode(PasPompe6, OUTPUT);
  pinMode(PompeDis, OUTPUT);
  pinMode(Distrib, OUTPUT);
  pinMode(DisablePompe1, OUTPUT);
  pinMode(DisablePompe2, OUTPUT);
  pinMode(DisablePompe3, OUTPUT);
  pinMode(DisablePompe4, OUTPUT);
  pinMode(DisablePompe5, OUTPUT);
  pinMode(DisablePompe6, OUTPUT);
  pinMode(DisableCarpet, OUTPUT);
  digitalWrite(DisablePompe1, HIGH);
  digitalWrite(DisablePompe2, HIGH);
  digitalWrite(DisablePompe3, HIGH);
  digitalWrite(DisablePompe4, HIGH);
  digitalWrite(DisablePompe5, HIGH);
  digitalWrite(DisablePompe6, HIGH);
  digitalWrite(DisableCarpet, HIGH);
  digitalWrite(PompeDis,LOW);
  digitalWrite(Distrib,HIGH);

  Serial.begin(9600);
}
void loop() {
  readSerial();

  if (message[0]=='F') {
    while (message[0]!='S') {
      readSerial();
      ForceP(message[1]);
    }
    disablePump(message[1]);
  }

  if (message[0]=='R') {
    while (message[0]!='S') {
      readSerial();
      ReverseP(message[1]);
    }
    disablePump(message[1]);
  }

  if (message[0]=='P') {
    carpet(message[1]);
    disablePump('C');
    Serial.println("OK");
    Pompe(message);
    disablePump(message[1]);
    Serial.println("OK");
  }

  if (message[0]=='E') {
    carpet(message[1]);
    disablePump('C');
  }

  if (message[0]=='G') {
    gobelet();
    Serial.println("OK");
  }

  message[0] = 0;
}
