byte touchIn[2] = {ANALOG1, ANALOG2};
bool previousTouchState[2] = {false, false};
bool currentTouchState[2];

void touchSetup()
{
  pinMode(touchIn[0], INPUT);
  pinMode(touchIn[1], INPUT);
}
void read_doubleTouch()
{
  for (byte i = 0; i < 2; i++)
    currentTouchState[i] = digitalRead(touchIn[i]);
  if (currentTouchState[0] != previousTouchState[0] || currentTouchState[1] != previousTouchState[1])
  {
    delay(100); // read again for concurrent touches
    for (byte i = 0; i < 2; i++)
      currentTouchState[i] = digitalRead(touchIn[i]);
    if (currentTouchState[0] && currentTouchState[1])
    {
      beep(20, 50, 50, 3);
      tQueue->addTask('k', "bk", 1500);
      tQueue->addTask('k', "up", 1500);
    }
    else if (currentTouchState[0])
    {
      tQueue->addTask('b', "10,16,12,16,14,16"); // example using 'b' for ASCII commands. Not recommended because of low encoding efficiency.It uses 17 byes to encode 6 numbers
      tQueue->addTask('i', "0,90", 100);         // example using 'i' for ASCII commands. Not recommended because of low encoding efficiency. It uses 4 byes to encode 2 numbers
                                                 // the movement starts after the music
    }
    else if (currentTouchState[1])
    {
      int8_t mel[] = {17, 16, 19, 16, 21, 16, '~'}; // example using 'B' for Binary commands. it has to end up with '~' because regular 0 can be mistaken as '\0'.
      int8_t mov[] = {0, -90, '~'};                 // example using 'I' for Binary commands. it has to end up with '~' because regular 0 can be mistaken as '\0'.
      tQueue->addTask('I', mov, 100);               // the movement starts before the music
      tQueue->addTask('B', mel, 100);
    }
    else
    {
      // char mel[]={
      int8_t mel[] = {15, 16, 14, 16, 12, 16, '~'};
      tQueue->addTask('i', "");
      tQueue->addTask('k', "sit");
      tQueue->addTask('B', mel);
    }
    if (currentTouchState[0] || currentTouchState[1])
    {
      PT("Previous: ");
      PT(previousTouchState[0]);
      PT(previousTouchState[1]);
      PT("\tCurrent: ");
      PT(currentTouchState[0]);
      PTL(currentTouchState[1]);
    }
  }
  for (byte i = 0; i < 2; i++)
    previousTouchState[i] = currentTouchState[i];
}
