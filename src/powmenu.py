import sys
from PyQt5.QtWidgets import QApplication
from app.main import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    powmenu = MainWindow()
    powmenu.show()
    sys.exit(app.exec())

