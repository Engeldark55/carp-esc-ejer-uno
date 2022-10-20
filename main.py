from tkinter.messagebox import NO
from PySide6.QtWidgets import QApplication
from controller.app_main import Notas
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Notas()
    my_app.show()
    sys.exit(app.exec())

