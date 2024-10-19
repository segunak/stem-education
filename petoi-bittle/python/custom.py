from PetoiRobot import *

autoConnect();

# Disable voice module
sendCmdStr("XAd", 0);

# # Reduce beep volume
# sendCmdStr("b2", 1);

# Rename bluetooth
sendCmdStr("nCLTBittle2", 0);

closePort();