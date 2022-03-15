import serial
from PySide6.QtWidgets import *
from PySide6.QtGui import QCloseEvent
import sys


class ArduinoControl(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        # Define quit button
        btn_quit = QPushButton('Quitter', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(100, 100)

        # Define upc to test button
        btn_test_upc = QPushButton('Tester un code UPC', self)
        btn_test_upc.clicked.connect(self.upcInputEvent)
        btn_test_upc.move(300, 100)

        # Define window settings
        self.setGeometry(1280, 720, 1280, 720)
        self.setWindowTitle('Arduino Control Panel')
        self.show()

    def upcInputEvent(self):
        upc_num, result = QInputDialog.getInt(self, 'Input Dialog', "Entrer le numéro UPC du produit à tester : ")
        if result:
            print(upc_num)

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def run():
    app = QApplication(sys.argv)
    arduinoControl = ArduinoControl()
    app.exec()


if __name__ == '__main__':
    run()
