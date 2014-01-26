import fcntl
import smbus
import time
from logo import *
from fonts import *


OLED_ADDRESS = 0x3c
OLED_COMMAND = 0x80
OLED_DATA = 0x40

bus = smbus.SMBus(1)

#Rutina display

def init_oled():
    SendCommand(0xae)
    time.sleep(0.050)
    SendCommand(0xaf)
    time.sleep(0.050)
    return


def SendChar(data):
    bus.write_byte_data(OLED_ADDRESS, OLED_DATA, data)
    return


def SendCommand(command):
    bus.write_byte_data(OLED_ADDRESS, OLED_COMMAND, command)
    return


def SetXY(row, col):
    SendCommand(0xb0 + row)
    SendCommand(0x00 + (8 * col & 0x0f))
    SendCommand(0x10 + ((8 * col >> 4) & 0x0f))
    return


def ClearDisplay():
    SendCommand(0xa6)
    for i in range(8):
        SetXY(i, 0)
        for j in range(128):
            SendChar(0)
    return


def SendString(string):
    for i in string:
        for j in range(8):
            SendChar(myfont[ord(i) - 0x20][j])
    return


def SendBigNumber(number, x, y):
    SetXY(x, y)
    salto = 0
    #string = str(number)
    #for i in string:
    for j in range(96):
        SendChar(bigNumbers[number][j])
        if salto == 23:
            salto = 0
            x += 1
            SetXY(x, y)
        else:
            salto += 1
    return


def SendBigNumberString(number, x, y):
    string = str(number)
    for i in string:
        SendBigNumber(ord(i)-0x30, x, y)
        y += 3

    return



def SendImage(image):

    SetXY(0, 0)
    #SendCommand(0xae)
    SendCommand(0x20)
    SendCommand(0x00)
    for i in range(1024):
        SendChar(image[i])
    SendCommand(0xaf)
    return


def InitHorizontalScroll():
    SendCommand(0x26)
    SendCommand(0x00)
    SendCommand(0x00)
    SendCommand(0x07)
    SendCommand(0x07)
    SendCommand(0x2f)
    return


def StopScroll():
#  SendCommand(0x2e)
    SendCommand(0x2e)
    SendCommand(0x20)
    SendCommand(0x00)
    ClearDisplay()
    #SendImage(Aula30)
    return


init_oled()
ClearDisplay()

while(1):
    SendBigNumberString(1974, 2, 1)
    time.sleep(3)
    SendBigNumberString(2013, 2, 1)
    time.sleep(3)
    SendImage(Aula30)
    time.sleep(3)
    ClearDisplay()

#SendCommand(0xa7)


