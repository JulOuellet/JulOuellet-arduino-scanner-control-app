import serial
import struct

port = None
ser = serial.Serial('COM4', 115200, timeout=None)
endScanFLag = b'\x02'


def convertByte(byte: bytes):
    return struct.unpack('<B', byte)[0]


def getScannedValues():
    data_array = []
    while True:
        byte_val = ser.read()
        int_val = convertByte(byte_val)
        data_array.append(int_val)
        if byte_val == endScanFLag:
            return data_array


def findArduinoPort():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'USB' in port.description:
            return port.device
        return None
