import database
from PySide6.QtCore import QAbstractTableModel, Qt


class ScannedProductTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scannedProductList = []
        self.headers = ['UPC', 'Format', 'Description', 'Prix']
        self.database = database.Database()

    def rowCount(self, parent=None):
        return len(self.scannedProductList)

    def columnCount(self, parent=None):
        return len(self.headers)

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

    def add_product(self, upc: str) -> bool:
        row = self.database.getCodeData(upc)
        if row is None:
            return False

        self.scannedProductList.append(row)
        self.layoutChanged.emit()
        return True

    def clear_facture(self):
        self.scannedProductList.clear()
        self.layoutChanged.emit()
