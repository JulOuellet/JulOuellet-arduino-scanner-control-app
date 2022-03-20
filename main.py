import sys
from PySide6.QtWidgets import *
import interface


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = interface.MainApp()
    window.setWindowTitle('Arduino control app')
    window.resize(750, 720)
    window.show()

    sys.exit(app.exec())
