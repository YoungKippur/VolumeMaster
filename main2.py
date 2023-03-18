import serial
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

PORT = input("Ingrese el puerto serie: ")
serialArduino = serial.Serial(PORT, 9600)

text = ""
previusText = ""
ind = [0,0,0]
r = 0

while True:
    aux = str(serialArduino.readline())
    aux = aux[aux.index("'") + 1 : aux.index("r") - 1]

    for m in re.finditer(',', aux):
        ind[r] = m.start()
        r = r + 1
        if r == 3:
            r = 0
    
    val1 = aux[0 : ind[0]]
    val2 = aux[ind[0]+1 : ind[1]]
    val3 = aux[ind[1]+1 : ind[2]]
    val4 = aux[ind[2]+1 :] # last
    
    print(val1,val2,val3,val4)