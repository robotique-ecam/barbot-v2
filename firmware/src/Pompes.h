#include <Arduino.h>
#include <AccelStepper.h>
#include <MultiStepper.h>
#include <String.h>


#define EnablePompe1 22
#define DirPompe1 23
#define PasPompe1 24

#define EnablePompe2 25
#define DirPompe2 26
#define PasPompe2 27

#define EnablePompe3 28
#define DirPompe3 29
#define PasPompe3 30

#define EnablePompe4 31
#define DirPompe4 32
#define PasPompe4 33

#define EnablePompe5 34
#define DirPompe5 35
#define PasPompe5 36

#define EnablePompe6 37
#define DirPompe6 38
#define PasPompe6 39




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
