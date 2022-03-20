import product_list
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


codeDeTest = "074312842306"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.mainWindow = MainWindow()
        self.setCentralWidget(self.mainWindow)


class MainApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Setup products table
        self.productsList_model = product_list.ScannedProductTableModel()
        self.productsList_table = QTableView()
        self.productsList_table.setModel(self.productsList_model)
        self.productsList_table.horizontalHeader().setStretchLastSection(True)
        self.productsList_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.productsList_model.addProductToList(codeDeTest)

        # Setup total price label and layout
        self.total_price_layout = QFormLayout()
        self.total_price = QLabel()
        self.total_price_layout.addRow("Total: ", self.total_price)
        self.total_price_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.total_price_layout.setLabelAlignment(Qt.AlignRight)
        self.updateTotalPrice()

        # Setup buttons and input text box
        self.upc_input = QLineEdit()
        self.upc_input.setPlaceholderText("Entrer un numéro UPC")
        self.add_product = QPushButton("Ajouter manuellement un produit à la liste")
        self.delete_lines = QPushButton("Effacer les produits sélectionnés")
        self.clear_list = QPushButton("Effacer tous les produits de la liste")

        # Setup controls layout
        self.controls_layout = QFormLayout()
        self.controls_layout.addRow("Code UPC : ", self.upc_input)
        self.controls_layout.addRow(self.add_product)
        self.controls_layout.addRow(self.delete_lines)
        self.controls_layout.addRow(self.clear_list)
        self.controls_layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)

        # Setup main layout for products list and total price
        self.list_and_total_layout = QHBoxLayout()
        # self.list_and_total_layout = QVBoxLayout()
        self.list_and_total_layout.addWidget(self.productsList_table)
        self.list_and_total_layout.addLayout(self.total_price_layout)

        # Setup main layout for controls and product list
        self.controls_and_list_layout = QVBoxLayout()
        self.controls_and_list_layout.addLayout(self.controls_layout)
        self.controls_and_list_layout.addLayout(self.list_and_total_layout)
        self.controls_and_list_layout.setStretchFactor(self.list_and_total_layout, 1)
        self.setLayout(self.controls_and_list_layout)
        self.productsList_table.resizeColumnsToContents()

        self.setActions()

    def setActions(self):
        self.add_product.clicked.connect(self.addProductToList)
        self.clear_list.clicked.connect(self.clearProductsList)
        self.productsList_model.layoutChanged.connect(self.updateTotalPrice)
        self.delete_lines.clicked.connect(self.removeProducts)

    def addProductToList(self):
        upc = self.upc_input.text()

        # Valider le format du code upc
        if len(upc) != 12 or not upc.isdigit() or not self.productsList_model.addProductToList(upc):
            popupMessage("Le code UPC entré n'est pas valide")

    def clearProductsList(self):
        self.productsList_model.clearProductsList()

    def removeProducts(self):
        self.productsList_model.removeLine(self.productsList_table.selectedIndexes())

    def updateTotalPrice(self):
        self.total_price.setText(self.productsList_model.getTotalPrice())


def popupMessage(msg: str):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText(msg)
    msg_box.setWindowTitle("Erreur")
    msg_box.exec()
