import serial
import time
import threading


ser = serial.Serial('COM4', 115200, timeout=1)
datas = ""


# Classe pour lire le port serial dans le background
class SerialReaderThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    # Get data from port
    def run(self):
        global ser, datas
        while not self.stopped():
            datas = ser.read()
            print(datas)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
