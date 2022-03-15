import serial
from PySide6.QtWidgets import *
from PySide6.QtGui import QCloseEvent
import sys
import csv


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):

        # Define upc to test button
        btn_test_upc = QPushButton('Tester un code UPC', self)
        btn_test_upc.clicked.connect(self.upcInputEvent)
        btn_test_upc.move(100, 300)

        # Define quit button
        btn_quit = QPushButton('Quitter', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(100, 100)

        # Define window settings
        self.setGeometry(1280, 720, 1280, 720)
        self.setWindowTitle('Arduino Control Panel')
        self.show()

    def upcInputEvent(self):
        upc_num, result = QInputDialog.getText(self, 'Input Dialog', "Entrer le numéro UPC du produit à tester : ")
        if result:
            upc_num = int(upc_num)
            return findProduct(upc_num)

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def findProduct(value):
    with open(r'DB/upcPrice.txt', 'r') as file:
        reader = csv.reader(file)

        for line in reader:
            print("searching...")
            if int(line[0]) == value:
                upc_found = line
                print(upc_found)
                break
    return upc_found


def run():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec()


if __name__ == '__main__':
    run()
