import serial
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def connect():
    global serialArduino
    for t in range(2,30):
        try:
            PORT = "COM{}".format(t)
            serialArduino = serial.Serial("COM10", 115200)
            print("connected")
            # break
            return 0
        except:
            if t == 29:
                print("cant connect")
                # exit()
                return 1
            pass

while connect() == 1:
    pass

text = ""
previusText = "-1"


while True:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # meter delays a todo esto
    
    aux = str(serialArduino.readline())
    text = aux[aux.index("'") + 1 : aux.index("r") - 1]

    print(aux)

    # filtro
    if  text != previusText:
        try:
            if  int(text) >= int(previusText) + 2 or int(text) <= int(previusText) - 2:
                previusText = text
                text = ""
            elif previusText == "-1":
                previusText = text
                text = ""
        except:
            pass

    if previusText != "":
        try:
            y = int(previusText)
        except:
            y = 0
    else:
        y = 0

    a = ((y/100)*65)-65
    if a < -64:
        a = -65
    
    try:
        volume.SetMasterVolumeLevel(float(a), None)
    except:
        pass
