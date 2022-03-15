import serial


serialComm = serial.Serial('COM5', 9600, timeout=1)

while 1:
    data = serialComm.readline()
    print(data.decode())
