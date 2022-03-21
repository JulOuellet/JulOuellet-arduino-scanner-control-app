import sys
from PySide6.QtWidgets import *
import interface
import serial_thread


app = QApplication(sys.argv)
serialThread = serial_thread.SerialReaderThread()

serialThread.start()
window = interface.MainApp()
window.setWindowTitle('Arduino control app')
window.resize(750, 720)
window.show()

sys.exit(app.exec())
