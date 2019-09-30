#include <Arduino.h>
#include <AccelStepper.h>


#define dirPin 2
#define stepPin 3
#define motorInterfaceType 1


AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);


void setup() {
  // Microsteps are set to 1/32
  // Therefore 200 x 32 = 6 400 gives
  // Set the maximum speed in steps per second:
  stepper.setMaxSpeed(6400);
}

void loop() {
  // Set the speed in steps per second:
  stepper.setSpeed(6400);
  // Step the motor with a constant speed as set by setSpeed():
  stepper.runSpeed();
}
