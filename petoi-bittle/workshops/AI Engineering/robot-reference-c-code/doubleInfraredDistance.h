/*
Demo for the Petoi double infrared distance sensor
It works under the indoor lighting condition.

The robot will make different sound by the distance of the obstable in front of it.

When the robot is in static posture:
1. It will turn its head to the object in front of it.
2. When the view angle is larger than 75 degrees, the robot will turn its body to that direction.
3. If the object is too close, the robot will walk backward then walk forward, then sit.

When the robot is walking:
1. It will trot forward when the front is clear.
2. It will turn when there's an obstacle within 30cm.
3. It will retreat and turn if the obstacle is within 12cm.
4. It will rotate when the obstacle is within 4cm.

Rongzhong Li
Petoi LLC
2023 April 17
*/
#define READING_COUNT 30
#define SENSOR_DISPLACEMENT 3.7

// #ifdef NyBoard_V1_0
// #define NEOPIXEL_PIN 10 // the code for NeoPixels have to be shrinked to fit in the board
// #define NUMPIXELS 7
// #elif defined NyBoard_V1_2
// #define NEOPIXEL_PIN 10 // the code for NeoPixels have to be shrinked to fit in the board
// #define NUMPIXELS 1
// #endif

float fit(int d)
{
  if (d < 130)
    return d / 8.0;
  else
    return 4096.0 / (pow(4096 - d, 1.0 / 3) + 25) - 84;
}

#ifdef NEOPIXEL_PIN
#include <Adafruit_NeoPixel.h>
Adafruit_NeoPixel strip(NUMPIXELS, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800);
#endif

bool makeSound = true;

float kpDistance = 0.3;     // Proportional gain
float kiDistance = 0.1;     // Integral gain
float kdDistance = 0.1;     // Derivative gain
float setpoint = 0;         // Target value
float errorDistance = 0;    // Difference between setpoint and actual value
float integral = 0;         // Running sum of errors over time
float derivative = 0;       // Rate of change of errorDistance over time
float last_error = 0;       // errorDistance in the previous iteration
float currentXDistance = 0; // Control signal sent to the sensors

float d = SENSOR_DISPLACEMENT; // Displacement of sensors on the x-axis
int rawL, rawR;
float dL, dR, meanD, maxD, minD;
int meanA = 0, meanB = 0, diffA_B = 0, actualDiff = 0, last = 0;
int longThres = 20;
long leftCloseTimer, rightCloseTimer;

void resetPID()
{
  errorDistance = 0;
  last_error = 0;
  integral = 0;
  derivative = 0;
}

void distanceNaive(float dLeft, float dRight)
{ // a simple feedback loop without PID
  float minD = min(dLeft, dRight);
  float diff = dRight - dLeft;
  float offset = atan(diff / SENSOR_DISPLACEMENT) * degPerRad;

  if (periodGlobal == 1)
  { // posture
    if (minD < 20 && abs(offset) > 5 - minD / 5)
    {
      // PT("\tmin ");
      // PT(minD);
      // PT("\tdiff ");
      // PT(diff);
      // PT("\toffset ");
      // PT(offset);
      currentXDistance = min(90.0, max(-90.0, double(currentXDistance + offset / 10)));
      calibratedPWM(0, currentXDistance, 0.2);
      // PTL();
      FPS();
    }
  }
}

void distancePID(float dLeft, float dRight)
{
  // Read the current distances from the sensors
  if (minD < longThres && dL != 200 && dR != 200)
  {
    // Calculate the errorDistance between the setpoint and the actual values, taking into account the x-axis displacement
    // errorDistance = atan((dLeft - dRight) / SENSOR_DISPLACEMENT) * degPerRad;
    errorDistance = dLeft - dRight - setpoint;
    if (fabs(errorDistance) > 1)
    {
      // Calculate the integral and derivative terms
      integral = max(-900.0, min(900.0, double(integral + errorDistance)));
      derivative = errorDistance - last_error;

      // Calculate the control signal using the PID formula
      currentXDistance = -max(-75.0, min(75.0, double(kpDistance * errorDistance + kiDistance * integral + kdDistance * derivative)));
      // Send the control signal to the sensors to adjust their angles
      // token = T_INDEXED_SIMULTANEOUS_BIN;
      // newCmd[0] = 0;
      // newCmd[1] = currentXDistance;
      // newCmd[2] = 1;
      // newCmd[3] = 15;
      // // last = actualOffset;
      // cmdLen = 4;
      // newCmdIdx = 5;
      manualHeadQ = true;
      targetHead[0] = currentXDistance;
      int duty = currentAng[0] + max(-20, min(20, (targetHead[0] - currentAng[0])));
      calibratedPWM(0, duty, 0.5);
      // Save the current errorDistance for use in the next iteration
      last_error = errorDistance;
    }
  }
  // PT('\t');
  // PT(errorDistance);
  // PT('\t');
  // PT(integral);
  // PT('\t');
  // PT(derivative);
  // PT('\t');
  // PT(currentXDistance);
}

void doubleInfraredDistanceSetup()
{
// put your setup code here, to run once:
#ifdef NEOPIXEL_PIN
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
#endif
#ifdef LED_PIN
  pinMode(LED_PIN, OUTPUT);
#endif
  manualHeadQ = true;
}

void readDistancePins()
{
  // #ifdef BiBoard_V1_0
  //   rawL = analogRead(ANALOG4);
  //   rawR = analogRead(ANALOG3);
  // #else
  dL = fit(analogRead(ANALOG1));
  dR = fit(analogRead(ANALOG2));
  // #endif

  // meanD = (dL + dR) / 2;
  // maxD = max(dL, dR);
  // minD = min(dL, dR);
  if (0)
  {
    // PT("rL ");
    // PT(rawL);
    // PT("\trR ");
    // PT(rawR);
    PT("\tdL ");
    PT(dL);
    PT("\tdR ");
    PT(dR);
    PT("\tmD ");
    PT(meanD);
  }
}

void catchObject()
{
  while (dL < 30 || dR < 30)
  {
    readDistancePins();
    distancePID(dL, dR);
    if (dL < 10) // within capture range
      leftCloseTimer = millis();
    if (dR < 10) // within capture range
      rightCloseTimer = millis();
    // if (currentAng[2] < 20)
    calibratedPWM(2, min(float(80), 80 - (min(dL, dR) - 15) * 5)); // open pincer
    if (leftCloseTimer > 0 && leftCloseTimer > 0 && abs(leftCloseTimer - rightCloseTimer) < 50)
    {
      int8_t targetShift = (leftCloseTimer - rightCloseTimer); // evaluate the target's speed and direction
      PTHL("targetShift", targetShift);
      calibratedPWM(0, currentAng[0] + targetShift);
      calibratedPWM(1, 45);  // raise arm
      calibratedPWM(2, 120); // clip the pincer
      delay(1000);
      tQueue->addTask(T_INDEXED_SIMULTANEOUS_ASC, "0,0,1,0,2,0", 1000);
      leftCloseTimer = rightCloseTimer = -1;
    }
  }
}

void read_doubleInfraredDistance()
{
  readDistancePins();
  // if (makeSound && minD > longThres / 2 && maxD < longThres && periodGlobal == 1)
  //   beep(35 - meanD, meanD / 4);
#ifdef NEOPIXEL_PIN
  strip.clear();
  for (int i = 0; i < min(8 - sqrt(dL) * 1.4, strip.numPixels()); i++)
  {                                                                                              // For each pixel in strip..
    strip.setPixelColor(i, strip.Color(255 - meanD * 6, meanD * 6, 128 + currentXDistance * 2)); //  Set pixel's color (in RAM)
    strip.show();
  }
#endif
#ifdef LED_PIN
  if (LED_PIN == 10)
    digitalWrite(LED_PIN, 255 - meanD * 6 > 128);
  else
    analogWrite(LED_PIN, 255 - meanD * 6);
#endif
  if (dL < 1 || dR < 1)
  {
    readDistancePins();
    if (dL < 1 && dR < 1)
    {
      // makeSound = !makeSound;
      // tQueue->addTask('k', "bk", 1500);
      // tQueue->addTask('k', "wkF", 1500);
      // tQueue->addTask('k', "sit");
      // tQueue->addTask('i', "");
    }
  }
#ifdef ROBOT_ARM

#endif
  if (periodGlobal == 1)
  {
    distancePID(dL, dR);
    // if (currentXDistance < -75 || currentXDistance > 75) {
    //   if (currentXDistance < -75) {
    //     // tQueue->addTask('k', "vtR", 2000);
    //   } else {
    //     // tQueue->addTask('k', "vtL", 2000);
    //   }
    //   // tQueue->addTask('k', "sit");
    //   currentXDistance = 0;
    //   resetPID();
    // }
  }
  // distanceNaive(dL, dR);
  else if (periodGlobal > 1 && tQueue->cleared())
  { // gait
    tQueue->addTask('i', "");
    if (dL > longThres && dR > longThres)
    { // free to run
      tQueue->addTask('k', "trF");
      idleTimer = millis() + IDLE_TIME / 2;
      PTLF(" free");
    }
    else if (dL < longThres / 5 || dR < longThres / 5)
    { // too close. retreat
      tQueue->addTask('k', dL < dR ? "vtR" : "vtL", 2000);
      PTLF(" too close");
    }
    else
    {
      idleTimer = millis() + IDLE_TIME;
      if (abs(dR - dL) > 2)
      { // one side has longer free distance
        tQueue->addTask('k', dL < dR ? "trR" : "trL", 1000);
        PTLF("turn");
      }
      else if (dL < longThres / 2 || dR < longThres / 2)
      {
        tQueue->addTask('k', dL < dR ? "bkL" : "bkR", 1500);
        tQueue->addTask('k', dL < dR ? "trR" : "trL", 1500);
        PTLF(" retreat and turn");
      }
    }
  }
  // PTL();
}
