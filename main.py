import serial
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent


class ArduinoControl(QWidget):

    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):
        btn_quit = QPushButton('Quitter', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(100, 100)

        self.setGeometry(1280, 720, 1280, 720)
        self.setWindowTitle('Arduino Control Panel')
        self.show()

    def closeEvent(self, event:QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def run():
    app = QApplication([])
    arduinoControl = ArduinoControl()
    app.exec()


if __name__ == '__main__':
    run()
