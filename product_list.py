import database
from PySide6.QtCore import QAbstractTableModel, Qt


class ScannedProductTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scannedProductList = []
        self.headers = ['Code UPC', 'Format', 'Description du produit', 'Prix']
        self.database = database.Database()
        self.totalPrice = 0.0

    def rowCount(self, parent=None):
        return len(self.scannedProductList)

    def columnCount(self, parent=None):
        return len(self.headers)

    def removeLine(self, indices: list[int]):
        for i in indices:
            self.totalPrice -= self.scannedProductList[i.row()][3]
            self.scannedProductList.pop(i.row())
        self.layoutChanged.emit()

    def data(self, index, role=None):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.scannedProductList[index.row()][index.column()]

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return None

    def addProductToList(self, upc: str) -> bool:
        newLine = self.database.getCodeData(upc)
        if newLine is None:
            return False

        self.totalPrice += newLine[3]
        self.scannedProductList.append(newLine)
        self.layoutChanged.emit()
        return True

    def clearProductsList(self):
        self.scannedProductList.clear()
        self.totalPrice = 0.00
        self.layoutChanged.emit()

    def getTotalPrice(self) -> str:
        total_str = str.format("{:.2f} $", self.totalPrice)
        return total_str
