import serial

PORT = "COM10"
serialArduino = serial.Serial(PORT,9600)
print("ok")


while True:
    serialArduino.write("ola".encode('utf-8'))
    print(".")
