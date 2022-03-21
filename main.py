import sys
from PySide6.QtWidgets import *
import interface
import communication


app = QApplication(sys.argv)
comm = communication.SerialReaderThread()

comm.start()
window = interface.MainApp()
window.setWindowTitle('Arduino control app')
window.resize(750, 720)
window.show()

sys.exit(app.exec())
