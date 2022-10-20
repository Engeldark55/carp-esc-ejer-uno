from PySide6.QtWidgets import QWidget
from view.Mensaje import Ui_Form_mensaje as msj

class Mensaje(QWidget, msj):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        