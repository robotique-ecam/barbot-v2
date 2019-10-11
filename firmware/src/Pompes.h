#include <Arduino.h>
#include <AccelStepper.h>
#include <MultiStepper.h>
#include <String.h>


#define EnablePompe1 22
#define DirPompe1 30
#define PasPompe1 31

#define EnablePompe2 25
#define DirPompe2 32
#define PasPompe2 33

#define EnablePompe3 28
#define DirPompe3 34
#define PasPompe3 35

#define EnablePompe4 31
#define DirPompe4 36
#define PasPompe4 37

#define EnablePompe5 34
#define DirPompe5 38
#define PasPompe5 39

#define EnablePompe6 37
#define DirPompe6 40
#define PasPompe6 41

#define EnableCarpet 40
#define DirCarpet 42
#define PasCarpet 43
#define motorInterfaceType 1

AccelStepper stepper1 = AccelStepper(motorInterfaceType,PasCarpet,DirCarpet);


void ForceP(char num)
{
  if (num=='1')
  {
    digitalWrite(DirPompe1,HIGH);
    digitalWrite(EnablePompe1,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe1,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe1,LOW);
  }
  if (num=='2')
  {
    digitalWrite(DirPompe2,HIGH);
    digitalWrite(EnablePompe2,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe2,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe2,LOW);
  }
  if (num=='3')
  {
    digitalWrite(DirPompe3,HIGH);
    digitalWrite(EnablePompe3,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe3,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe3,LOW);
  }
  if (num=='4')
  {
    digitalWrite(DirPompe4,HIGH);
    digitalWrite(EnablePompe4,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe4,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe4,LOW);
  }
  if (num=='5')
  {
    digitalWrite(DirPompe5,HIGH);
    digitalWrite(EnablePompe5,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe5,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe5,LOW);
  }
  if (num=='6')
  {
    digitalWrite(DirPompe6,HIGH);
    digitalWrite(EnablePompe6,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe6,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe6,LOW);
  }


}
void ReverseP(char num)
{
  if (num=='1')
  {
    digitalWrite(DirPompe1,LOW);
    digitalWrite(EnablePompe1,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe1,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe1,LOW);
  }
  if (num=='2')
  {
    digitalWrite(DirPompe2,LOW);
    digitalWrite(EnablePompe2,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe2,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe2,LOW);
  }
  if (num=='3')
  {
    digitalWrite(DirPompe3,LOW);
    digitalWrite(EnablePompe3,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe3,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe3,LOW);
  }
  if (num=='4')
  {
    digitalWrite(DirPompe4,LOW);
    digitalWrite(EnablePompe4,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe4,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe4,LOW);
  }
  if (num=='5')
  {
    digitalWrite(DirPompe5,LOW);
    digitalWrite(EnablePompe5,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe5,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe5,LOW);
  }
  if (num=='6')
  {
    digitalWrite(DirPompe6,LOW);
    digitalWrite(EnablePompe6,LOW);
    delayMicroseconds(500);
    digitalWrite(PasPompe6,HIGH);
    delayMicroseconds(500);
    digitalWrite(PasPompe6,LOW);
  }

}


void Pompe(String message)
{
  int ml=0;
  ml=(int)(message[3,sizeof(message)-1]);
  char nPompe=message[1];
  int step=ml*3200;

  for (int i=0;i<step;i++)
  {
    ForceP(nPompe);
  }
}



void Carpet(String message)
{
  int step=0;
  step=message.substring(3).toInt();

  stepper1.setMaxSpeed(6000);
  stepper1.setAcceleration(12000);
  stepper1.moveTo(step);

  for (int i=0;i<step;i++)
  {
    if (stepper1.distanceToGo() == 0)
      stepper1.moveTo(-stepper1.currentPosition());
    stepper1.run();
  }
}
