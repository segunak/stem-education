#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Petoi.py - Single File Petoi Bittle X Robot Dog Controller

This file combines the original Petoi Python files into a single import:
- SerialCommunication.py
- ardSerial.py  
- PetoiRobot.py
- config.py

This enables programmatic control of the Petoi Bittle X Robot Dog with just one import.

Usage:
    from Petoi import *
    
    # Connect to robot
    autoConnect()
    
    # Send commands
    sendSkillStr("ksit", 1)  # Make robot sit
    sendSkillStr("kup", 1)   # Make robot stand
    
    # Close connection
    closePort()

Original files are preserved in the 'original-petoi-files' folder.
"""

import binascii
import serial  # need to install pyserial first
import serial.tools.list_ports
import logging
import time
import threading
import sys
import os
import platform
import struct
import re
import tkinter as tk
import copy
import glob

# =============================================================================
# CONFIG MODULE (from config.py)
# =============================================================================

model_ = ''
version_ = ''
modelList = []
useMindPlus = True

# =============================================================================
# SERIAL COMMUNICATION MODULE (from SerialCommunication.py)
# =============================================================================

# global variables
# whether the serial port is created successfully or not
Ret = False
# list of serial port number
port_list_number = []
# list of serial port names
port_list_name = []

class Communication(object):
    """
    Python serial communication package class
    """
    # initialization
    def __init__(self, com, bps, timeout):
        self.port = com  # serial port number
        self.bps = bps  # baud rate
        self.timeout = timeout  # timeout
        self.main_engine = None  # global serial communication object
        global Ret
        Ret = False
        self.data = None
        self.b_c_text = None

        try:
            # open the serial port and get the serial port object
            self.main_engine = serial.Serial(self.port, self.bps, timeout=self.timeout)
            # determine whether the opening is successful
            if self.main_engine.is_open:
                Ret = True
                # print("Ret = ", Ret)
        except Exception as e:
            print("---Exception---：", e)

    def Print_Name(self):
        """
        Print the basic information of the device
        """
        print(self.main_engine.name)  # device name
        print(self.main_engine.port)  # read or write port
        print(self.main_engine.baudrate)  # baud rate
        print(self.main_engine.bytesize)  # byte size
        print(self.main_engine.parity)  # parity
        print(self.main_engine.stopbits)  # stop bits
        print(self.main_engine.timeout)  # read timeout setting
        print(self.main_engine.writeTimeout)  # write timeout setting
        print(self.main_engine.xonxoff)  # software flow control setting
        print(self.main_engine.rtscts)  # hardware (RTS/CTS) flow control setting
        print(self.main_engine.dsrdtr)  # hardware (DSR/DTR) flow control setting
        print(self.main_engine.interCharTimeout)  # character interval timeout

    def Open_Engine(self):
        """
        open serial port
        """
        global Ret
        # If the serial port is not open, open the serial port
        if not self.main_engine.is_open:
            self.main_engine.open()
            Ret = True

    def Close_Engine(self):
        """
        close serial port
        """
        global Ret
        # print("self.main_engine.is_open：" + str(self.main_engine.is_open))  # check if the serial port is open
        # determine whether to open
        if self.main_engine.is_open:
            self.main_engine.close()  # close serial port
            Ret = False

    @staticmethod
    def Print_Used_Com():
        """
        print the list of available serial ports
        """
        port_list_name.clear()
        port_list_number.clear()

        port_list = list(serial.tools.list_ports.comports())

        if port_list:
            for each_port in port_list:
                port_list_number.append(each_port[0])
                port_list_name.append(each_port[1])

        return port_list_number

    def Read_Size(self, size):
        """
        Receive data of specified size
        :param size:
        :return:
        """
        return self.main_engine.read(size=size)

    def Read_Line(self):
        """
        Receive a line of data
        :return:
        """
        return self.main_engine.readline()

    def Send_data(self, data):
        """
        send data
        :param data:
        """
        self.main_engine.write(data)

    def Receive_data(self, way):
        """
        receive data
        :param way:
        """
        # Receiving data cyclically, this is an endless loop,
        # which can be implemented by threads
        print("Start receiving data：")
        bWaitRec = True
        while bWaitRec:
            try:
                # byte-by-byte reception
                if self.main_engine.in_waiting:
                    if way == 0:
                        for i in range(self.main_engine.in_waiting):
                            print("receive ascii data：" + str(self.Read_Size(1)))
                    if way == 1:
                        # overall reception
                        self.data = self.main_engine.read(self.main_engine.in_waiting).decode("utf-8")  # method 1
                        print("receive ascii data：", self.data)

                        # if data is empty, exit the receiving loop
                        if self.data.strip() == '':
                            bWaitRec = False
            except Exception as e:
                print("Exception report：", e)

        print("Data received！")

# =============================================================================
# SERIAL COMMUNICATION FUNCTIONS (from ardSerial.py)
# =============================================================================

FORMAT = '%(asctime)-15s %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

def printH(head, value):
    print(head, end=' ')
    print(value)

if not useMindPlus:
    try:
        import tkinter as tk
        import tkinter.messagebox
        sys.path.append("../pyUI")
        from translate import *
        language = languageList['English']

        def txt(key):
            global language
            logger.debug(f"config.strLan is: {config.strLan}.")
            language = languageList[config.strLan]
            return language.get(key, textEN[key])
    except ImportError:
        # Fallback if translate module is not available
        language = {}
        def txt(key):
            return key
else:
    def txt(key):
        return key

logger.info("ardSerial date: Feb. 27, 2025")

def encode(in_str, encoding='utf-8'):
    if isinstance(in_str, bytes):
        return in_str
    else:
        return in_str.encode(encoding)

delayBetweenSlice = 0.001

def serialWriteNumToByte(port, token, var=None):  # Only to be used for c m u b I K L o within Python
    logger.debug(f'serialWriteNumToByte, token={token}, var={var}')
    in_str = ""
    if var is None:
        var = []
    if token == 'K':
        period = var[0]
        if period > 0:
            skillHeader = 4
        else:
            skillHeader = 7
            
        if period > 1:
            frameSize = 8  # gait
        elif period == 1:
            frameSize = 16  # posture
        else:
            frameSize = 20  # behavior
            
        # divide large angles by 2
        angleRatio = 1
        for row in range(abs(period)):
            for angle in var[skillHeader + row * frameSize:skillHeader + row * frameSize + min(16,frameSize)]:
                if angle > 125 or angle < -125:
                    angleRatio = 2
                    break
            if angleRatio == 2:
                break
        
        if angleRatio == 2:
            var[3] = 2
            for row in range(abs(period)):
                for i in range(skillHeader + row * frameSize,skillHeader + row * frameSize + min(16,frameSize)):
                    var[i] //= 2
            printH('rescaled:\n', var)
            
        var = list(map(int, var))
        in_str = token.encode() + struct.pack('b' * len(var), *var) + '~'.encode()

    else:
        if token.isupper():
            if len(var) > 0:
                message = list(map(int, var))
                if token == 'B':
                    for l in range(len(message)//2):
                        message[l*2+1] *= 8  # change 1 to 8 to save time for tests
                        logger.debug(f"{message[l*2]},{message[l*2+1]}")
            if token == 'W' or token == 'C':
                in_str = struct.pack('B' * len(message), *message)    # B - unsigned char
            else:
                in_str = struct.pack('b' * len(message), *message)    # b - signed char
            in_str = token.encode() + in_str + '~'.encode()

        else:
            message = ""
            for element in var:
                message += (str(round(element)) + " ")
            in_str = token.encode() + encode(message) + '\n'.encode()

    slice = 0
    while len(in_str) > slice:
        if len(in_str) - slice >= 20:
            port.Send_data(in_str[slice:slice+20])
        else:
            port.Send_data(in_str[slice:])
        slice += 20
        time.sleep(delayBetweenSlice)
    logger.debug(f"!!!! {in_str}")

def serialWriteByte(port, var=None):
    logger.debug(f'serial_write_byte, var={var}')
    if var is None:
        var = []
    token = var[0][0]
    if (token == 'c' or token == 'm' or token == 'i' or token == 'b' or token == 'u' or token == 't') and len(var) >= 2:
        in_str = ""
        for element in var:
            in_str = in_str + element + " "
        in_str += '\n'
    elif token == 'L' or token == 'I':
        if len(var[0]) > 1:
            var.insert(1, var[0][1:])
        var[1:] = list(map(int, var[1:]))
        in_str = token.encode() + struct.pack('b' * (len(var) - 1), *var[1:]) + '~'.encode()
    elif token == 'w' or token == 'k' or token == 'X' or token == 'g':
        in_str = var[0] + '\n'
    else:
        in_str = token + '\n'
    logger.debug(f"!!!!!!! {in_str}")
    port.Send_data(encode(in_str))
    time.sleep(0.01)

def printSerialMessage(port, token, timeout=0):
    if token == 'k' or token == 'K':
        threshold = 8
    else:
        threshold = 3
    if 'X' in token:
        token = 'X'
    startTime = time.time()
    allPrints = ''
    while True:
        time.sleep(0.001)
        if port:
            response = port.main_engine.readline().decode('ISO-8859-1')
            if response != '':
                logger.debug(f"response is: {response}")
                responseTrim = response.split('\r')[0]
                logger.debug(f"responseTrim is: {responseTrim}")
                if responseTrim.lower() == token.lower(): 
                    return [response, allPrints]
                elif token == 'p' and responseTrim == 'k':
                    return [response, allPrints]
                else:
                    allPrints += response
        now = time.time()
        if (now - startTime) > threshold:
            threshold += 2
            if threshold > 10:
                return -1
        if 0 < timeout < now - startTime:
            return -1

def sendTask(PortList, port, task, timeout=0):
    logger.debug(f"{task}")
    global returnValue
    if port:
        token = task[0]
        if token == 'K' or token == 'L' or token == 'I':
            serialWriteNumToByte(port, token, task[1])
        else:
            serialWriteByte(port, task)
        lastMessage = printSerialMessage(port, token, timeout)
    else:
        lastMessage = -1
    returnValue = lastMessage
    return lastMessage

def sendTaskParallel(ports, task, timeout=0):
    global returnValue
    threads = list()
    for p in ports:
        thread = threading.Thread(target=sendTask, args=(ports, p, task, timeout))
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    return returnValue

def splitTaskForLargeAngles(task):
    token = task[0]
    queue = list()
    if len(task) > 2 and (token == 'L' or token == 'I'):
        angleList = task[1]
        for i in range(len(angleList)):
            if abs(angleList[i]) > 125:
                angleList[i] = 125 if angleList[i] > 0 else -125
        queue.append(task)
    else:
        queue.append(task)
    return queue

def send(port, task, timeout=0):
    if isinstance(port, dict):
        returnResult = sendTaskParallel(list(port.keys()), task, timeout)
    elif isinstance(port, list):
        returnResult = sendTaskParallel(port, task, timeout)
    queue = splitTaskForLargeAngles(task)
    for task in queue:
        returnResult = sendTask(port, list(port.keys())[0] if isinstance(port, dict) else port[0], task, timeout)
    return returnResult

def keepReadingInput(ports):
    while True and len(ports):
        time.sleep(0.1)

def closeSerialBehavior(port):
    try:
        port.Close_Engine()
    except Exception as e:
        logger.error(f"Error closing port: {e}")
    logger.info("close the serial port.")

def closeAllSerial(ports, clearPorts=True):
    if clearPorts is True:
        ports.clear()
    for p in ports:
        closeSerialBehavior(p)
    if clearPorts is True:
        ports.clear()

# Posture definitions
balance = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 30, 30, 30, 30, 30, 30, 30, 30]
buttUp = [1, 0, 15, 1, 20, 40, 0, 0, 5, 5, 3, 3, 90, 90, 45, 45, -60, -60, 5, 5]
calib = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dropped = [1, 0, -75, 1, 0, 30, 0, 0, -5, -5, 15, 15, -75, -75, 45, 45, 60, 60, -30, -30]
lifted = [1, 0, 75, 1, 0, -20, 0, 0, 0, 0, 0, 0, 60, 60, 75, 75, 45, 45, 75, 75]
rest = [1, 0, 0, 1, -30, -80, -45, 0, -3, -3, 3, 3, 70, 70, 70, 70, -55, -55, -55, -55]
sit = [1, 0, -30, 1, 0, 0, -45, 0, -5, -5, 20, 20, 45, 45, 105, 105, 45, 45, -45, -45]
stretch = [1, 0, 20, 1, 0, 30, 0, 0, -5, -5, 0, 0, -75, -75, 30, 30, 60, 60, 0, 0]
zero = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

balanceNybble = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 30, 30, -30, -30, 30, 30, -30, -30]
buttUpNybble = [1, 0, 15, 1, 20, 40, 0, 0, 5, 5, 3, 3, 90, 90, -45, -45, -60, -60, -5, -5]
droppedNybble = [1, 0, 75, 1, 0, 30, 0, 0, -5, -5, 15, 15, -75, -75, -60, -60, 60, 60, 30, 30]
liftedNybble = [1, 0, -75, 1, 0, -70, 0, 0, 0, 0, 0, 0, 55, 55, 20, 20, 45, 45, 0, 0]
restNybble = [1, 0, 0, 1, -30, -80, -45, 0, -3, -3, 3, 3, 60, 60, -60, -60, -45, -45, 45, 45]
sitNybble = [1, 0, -20, 1, 10, -20, -60, 0, -5, -5, 20, 20, 30, 30, -90, -90, 60, 60, 45, 45]
strNybble = [1, 0, 15, 1, 10, 70, -30, 0, -5, -5, 0, 0, -75, -75, -45, -45, 60, 60, -45, -45]
zeroNybble = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

postureTableBittle = {
    "balance": balance,
    "buttUp": buttUp,
    "dropped": dropped,
    "lifted": lifted,
    "rest": rest,
    "sit": sit,
    "str": stretch,
    "zero": zero
}

postureTableNybble = {
    "balance": balanceNybble,
    "buttUp": buttUpNybble,
    "dropped": droppedNybble,
    "lifted": liftedNybble,
    "rest": restNybble,
    "sit": sitNybble,
    "str": strNybble,
    "zero": zeroNybble
}

postureTableDoF16 = {
    "balance": balance,
    "rest": rest,
    "zero": zero,
    "sit": sit,
    "str": stretch,
    "dropped": dropped,
    "buttUp": buttUp,
    "lifted": lifted,
}

postureDict = {
    'Nybble': postureTableNybble,
    'Bittle': postureTableBittle,
    'Bittle X': postureTableBittle,
    'DoF16': postureTableDoF16
}

model = 'Bittle'
postureTable = postureDict[model]

def schedulerToSkill(ports, testSchedule):
    compactSkillData = []
    newSkill = []
    outputStr = ""

    for task in testSchedule:
        compactSkillData.append(task)
    if len(compactSkillData) > 0:
        print('int8_t skill[] PROGMEM = {')
    else:
        print('int8_t skill[] PROGMEM = {};')
    angleRatio = 1
    for row in compactSkillData:
        print(outputStr)
    print('};')
    newSkill = list(map(lambda x: x // angleRatio, newSkill))
    newSkill = [-len(compactSkillData), 0, 0, angleRatio, 0, 0, 0] + newSkill
    print(newSkill)
    send(ports, ['K', newSkill, 1])

def getModelAndVersion(result):
    if result != -1:
        pass
    model_ = 'Bittle'
    version_ = 'Unknown'
    
def deleteDuplicatedUsbSerial(list):
    for item in list:
        if 'usbmodem' in item:
            return [item]
    return list
    
def testPort(PortList, serialObject, p):
    global goodPortCount
    try:
        serialObject.Send_data(encode('k'))
        time.sleep(0.5)
        response = serialObject.Read_Line()
        if response:
            logger.info(f"Port {p} responded: {response}")
            PortList[serialObject] = p
            goodPortCount += 1
    except Exception as e:
        logger.error(f"Error testing port {p}: {e}")

def checkPortList(PortList, allPorts, needTesting=True):
    threads = list()
    global goodPortCount
    goodPortCount = 0

    for p in reversed(allPorts):
        serialObject = Communication(p, 115200, 1)
        if needTesting is True:
            thread = threading.Thread(target=testPort, args=(PortList, serialObject, p))
            threads.append(thread)
            thread.start()
        else:
            PortList[serialObject] = p

    if needTesting is True:
        for t in threads:
            t.join()

def keepCheckingPort(portList, cond1=None, check=True, updateFunc=lambda: None):
    global portStrList
    allPorts = Communication.Print_Used_Com()
    logger.debug(f"allPorts is {allPorts}")
    if cond1 is None:
        cond1 = lambda: len(portList) == 0

    while cond1():
        allPorts = Communication.Print_Used_Com()
        allPorts = deleteDuplicatedUsbSerial(allPorts)
        checkPortList(portList, allPorts, check)
        updateFunc()
        time.sleep(0.5)

def showSerialPorts(allPorts):
    if os.name == 'posix' and sys.platform.lower()[:5] == 'linux':
        allPorts.append('/dev/ttyS0')
        
    allPorts = deleteDuplicatedUsbSerial(allPorts)
    for index in range(len(allPorts)):
        print(f"{index}: {allPorts[index]}")
    print("\n*** Available serial ports: ***")
    print(*allPorts, sep="\n")
    if platform.system() != "Windows":
        print("On macOS and Linux, you might need to use 'sudo' to access the serial port.")

def connectPort(PortList, needTesting=True, needSendTask=True):
    global initialized
    global goodPortCount
    allPorts = Communication.Print_Used_Com()
    showSerialPorts(allPorts)

    if len(allPorts) > 0:
        checkPortList(PortList, allPorts, needTesting)
    initialized = True
    if len(PortList) == 0:
        print("No available serial ports found.")
    else:
        print(f"Connected to {len(PortList)} port(s)")

def replug(PortList, needSendTask=True):
    global timePassed
    print('Please disconnect and reconnect the device from the COMPUTER side')
    
    window = tk.Tk()
    window.geometry('+800+500')
    def on_closing():
        window.destroy()
    window.protocol('WM_DELETE_WINDOW', on_closing)
    
    if not useMindPlus:
        window.title(txt('Replug mode'))
    else:
        window.title('Replug mode')

    thres = 10
    print('Counting down to manual mode:')
    
    def bCallback():
        window.destroy()
        
    labelC = tk.Label(window, font='sans 14 bold', justify='left')
    if not useMindPlus:
        labelC['text'] = txt('Replug prompt')
    else:
        labelC['text'] = 'Replug prompt'
    labelC.grid(row=0, column=0)
    
    if not useMindPlus:
        buttonC = tk.Button(window, text=txt('Confirm'), command=bCallback)
    else:
        buttonC = tk.Button(window, text='Confirm', command=bCallback)
    buttonC.grid(row=1, column=0, pady=10)
    labelT = tk.Label(window, font='sans 14 bold')

def selectList(PortList, ls, win, needSendTask=True):
    pass

def manualSelect(PortList, window, needSendTask=True):
    pass

goodPorts = {}
portStrList = []
initialized = False
goodPortCount = 0
sync = 0
lock = threading.Lock()
returnValue = ''
timePassed = 0

# =============================================================================
# ROBOT CONTROL FUNCTIONS (from PetoiRobot.py)
# =============================================================================

if platform.system() == "Windows":
    seperation = '\\'
    homeDri = os.getenv('HOMEDRIVE') 
    homePath = os.getenv('HomePath') 
    configDir = homeDri + homePath
else:
    seperation = '/'
    home = os.getenv('HOME') 
    configDir = home 
configDir = configDir + seperation + '.config' + seperation + 'Petoi'

modelName = 'Bittle'
intoCameraMode = False
intoGestureMode = False

printH("Mind+ date: ", "Feb 25, 2025")

def makeDirectory(path):
    path = path.strip()
    path = path.rstrip("\\").rstrip("/")
    
    isExists = os.path.exists(path)
    
    if not isExists:
        if path.split(seperation)[-1] == "BittleX+Arm":
            path = seperation.join(path.split(seperation)[:-1]) + seperation + "BittleR"
            if not os.path.exists(path):
                # Create the directory if it does not exist
                path = seperation.join(path.split(seperation)[:-1]) + seperation + "BittleX+Arm"
                os.makedirs(path)
                print(path + ' creat successfully')
            else:
                # Change the directory name "BittleR" to "BittleX+Arm"
                os.rename(path, seperation.join(path.split(seperation)[:-1]) + seperation + "BittleX+Arm")
        else:
            # Create the directory if it does not exist
            os.makedirs(path)
            print(path + ' creat successfully')
        return True
    else:
        print(path + ' already exists')
        return False

makeDirectory(configDir)

def file_name(file_dir):
    File_Name = []
    for files in os.listdir(file_dir):
        if os.path.splitext(files)[1] == '.md':
            File_Name.append(files.split('.')[0])
    return File_Name

BittleData = '''# Token
K

# Data
{
  -5,  0,   0, 1,
   1,  2,   3,
   0,-20, -60,   0,   0,   0,   0,   0,  35,  30, 120, 105,  75,  60, -40, -30,     4, 2, 0, 0,
  35, -5, -60,   0,   0,   0,   0,   0, -75,  30, 125,  95,  40,  75, -45, -30,    10, 0, 0, 0,
  40,  0, -35,   0,   0,   0,   0,   0, -60,  30, 125,  95,  60,  75, -45, -30,    10, 0, 0, 0,
   0,  0, -45,   0,  -5,  -5,  20,  20,  45,  45, 105, 105,  45,  45, -45, -45,     8, 0, 0, 0,
   0,  0,   0,   0,   0,   0,   0,   0,  30,  30,  30,  30,  30,  30,  30,  30,     5, 0, 0, 0,
};'''

NybbleData = '''# Token
K

# Data
{
  -5,   0,   0,   1,
   2,   3,   3,
   0, -20, -65,   0,   0,   0,   0,   0,  30,  30, -90, -90,  60,  60,  45,  45,   8,   1,   0,   0,
   0, -20, -65,   0,   0,   0,   0,   0,  30,  41, -90, -72,  60,  46,  45,   5,   8,   2,   0,   0,
  35, -15, -65,   0,  -3,  -3,   3,   3, -75,  41, -85, -72,  40,  65,  60,   0,   8,   0,   0,   0,
  40, -10, -55,   0,  -3,  -3,   3,   3, -60,  41, -80, -79,  60,  65,  60,   0,   4,   0,   0,   0,
   0,   0,   0,   0,   0,   0,   0,   0,  30,  41, -30, -30,  30,  30, -30, -30,  12,   0,   0,   0,
};'''

BittleRData = '''# Token
K

# Data
{
  -6, 0, 0, 1,
   1, 2, 3,
   0, -20,   0,   0,   0,   0,   0,   0,  35,  30, 120, 105,  75,  60, -40, -30,	 8, 2, 0, 0,
  -5,  -5,   0,   0,   0,   0,   0,   0, -99,  30, 125,  95,  40,  75, -45, -30,	10, 0, 0, 0,
   0,  -5,   0,   0,   0,   0,   0,   0, -90,  30, 125,  95,  62,  75, -45, -30,	10, 0, 0, 0,
 -15,  -5,   0,   0,   0,   0,   0,   0, -90,  30, 125,  95,  62,  75, -45, -30,	 8, 0, 0, 0,
   0,  -5,   0,   0,  -5,  -5,  20,  20,  45,  45, 105, 105,  45,  45, -45, -45,	 8, 0, 0, 0,
   0,   0,   0,   0,   0,   0,   0,   0,  30,  30,  30,  30,  30,  30,  30,  30,	 8, 0, 0, 0,
};'''

modelDict = {'Bittle': BittleData, 'Nybble': NybbleData, 'BittleX+Arm': BittleRData}

def creatSkillFile():
    for key in modelDict:
        modelDir = configDir + seperation + 'SkillLibrary' + seperation + key
        makeDirectory(modelDir)
        filePath = modelDir + seperation + 'skillFileName.md'
        if not os.path.exists(filePath):
            try:
                with open(filePath, 'w+', encoding="utf-8") as f:
                    f.write(modelDict[key])
                    time.sleep(0.1)
            except Exception as e:
                return False, 'save failed:{}'.format(e)

creatSkillFile()

def deacGyro():
    boardVer = version_
    if boardVer and boardVer[0] == 'N':
        res = send(goodPorts, ['g', 0])
    else:
        res = send(goodPorts, ['G', 0])
    logger.debug(f'gyro status:{res}')
    if res != -1 and res[0][0] in ['G', 'g']:
        print("Gyro deactivated")

def getAngleList():
    token = 'j'
    task = [token, 0]
    rawData = send(goodPorts, task)

    logger.debug(f'rawData={rawData}')
    p = re.compile(r'^(.*),', re.MULTILINE)
    for one in p.findall(rawData[1]):
        angle = one
    strAngleList = angle.split(',')
    logger.debug(f'strAngleList={strAngleList}')
    angleList = list(map(lambda x: int(x), strAngleList))
    logger.debug(f'angleList={angleList}')
    return angleList

def getAngle(index):
    token = 'j' 
    task = [token, [index], 0]
    rawData = send(goodPorts, task)
    if rawData != -1:
        return int(rawData[1].split(',')[0])

def getCurAng(index):
    currentVal = getAngle(index)
    return currentVal

def absValList(num1, num2):
    return [(int(num1), num2)]

def relativeValList(index, symbol, angle):
    return [(int(index), int(symbol), angle)]

def rotateJoints(token, var, delayTime):
    newList = []
    for iA in var:
        newList.extend(iA)
    sendLongCmd(token, newList, delayTime)

def play(token, var, delayTime):
    newList = []
    for iA in var:
        newList.append(iA)
    sendLongCmd(token, newList, delayTime)

def printSkillFileName():
    skillDir = configDir + seperation + 'SkillLibrary' + seperation + model_
    if os.path.exists(skillDir):
        skill_file_name = file_name(skillDir)
        print("*** The skill names you can call are as follows: ***")
        for skillName in skill_file_name:
            print(skillName.replace('.md', ''))
        print("******************************")

def openPort(port):
    allPorts = Communication.Print_Used_Com()
    showSerialPorts(allPorts)
    if platform.system() != "Windows" and '/dev' not in port:
        port = '/dev/' + port
    serialObject = Communication(port, 115200, 1)
    testPort(goodPorts, serialObject, port.split('/')[-1])
    t = 3
    print('Time delay after open port: ', str(t))
    time.sleep(t)
    printSkillFileName()

def autoConnect():
    connectPort(goodPorts)
    logger.debug(f'goodPorts: {goodPorts}')
    printSkillFileName()
    deacGyro()

def sendSkillStr(skillStr, delayTime):
    logger.debug(f'skillStr={skillStr}')
    send(goodPorts, [skillStr, delayTime])

def loadSkill(fileName, delayTime):
    if ".md" in fileName:
        skillFilePath = configDir + seperation + 'SkillLibrary' + seperation + model_ + seperation + fileName
    else:
        skillFilePath = configDir + seperation + 'SkillLibrary' + seperation + model_ + seperation + fileName + '.md'

    logger.debug(f'skillFilePath:{skillFilePath}')

    with open(skillFilePath, "r", encoding='utf-8') as f:
        lines = f.readlines()
    skillDataString = ''.join((str(x) for x in lines))
    logger.debug(f'skillDataString:{skillDataString}')
    skillDataString = ''.join(skillDataString.split()).split('{')[1].split('}')[0].split(',')
    logger.debug(f'skillDataString:{skillDataString}')
    if skillDataString[-1] == '':
        skillDataString = skillDataString[:-1]
    cmdList = list(map(int, skillDataString))
    logger.debug(f'cmdList:{cmdList}')

    token = 'K'
    send(goodPorts, [token, cmdList, delayTime])

def sendCmdStr(cmdStr, delayTime):
    logger.debug(f'serialCmd={cmdStr}')
    if cmdStr != '':
        send(goodPorts, [cmdStr, delayTime])

def sendLongCmd(token, var, delayTime):
    var = list(map(int, var))
    send(goodPorts, [token, var, delayTime])

def getValue(task, dataType="int"):
    rawData = send(goodPorts, task)
    if rawData != -1:
        if dataType == "int":
            return int(rawData[1])
        elif dataType == "float":
            return float(rawData[1])
        else:
            return rawData[1]

def readAnalogValue(pin):
    task = ['A', [pin], 0]
    return getValue(task)

def readDigitalValue(pin):
    task = ['D', [pin], 0]
    return getValue(task)

def readUltrasonicDistance(triggerPin, echoPin):
    task = ['U', [triggerPin, echoPin], 0]
    return getValue(task)

def writeAnalogValue(pin, val):
    task = ['a', [pin, val], 0]
    send(goodPorts, task)

def writeDigitalValue(pin, val):
    task = ['d', [pin, val], 0]
    send(goodPorts, task)

def closePort():
    closeAllSerial(list(goodPorts.keys()))

# =============================================================================
# MAIN FUNCTIONS FOR EASY IMPORT
# =============================================================================

def txt(key):
    """Fallback function for text translation"""
    return key

# Export all the main functions that users will need
__all__ = [
    'Communication',
    'autoConnect',
    'sendSkillStr', 
    'loadSkill',
    'sendCmdStr',
    'sendLongCmd',
    'play',
    'rotateJoints',
    'deacGyro',
    'getAngle',
    'getAngleList',
    'readAnalogValue',
    'readDigitalValue',
    'readUltrasonicDistance',
    'writeAnalogValue',
    'writeDigitalValue',
    'closePort',
    'openPort',
    'printSkillFileName'
]
