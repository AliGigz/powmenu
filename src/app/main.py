from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from app.widget import MainWidget
from app import config


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwrags):
        super(MainWindow, self).__init__(*args, **kwrags)
        self.init_ui()
        self.move_center()

    def init_ui(self):
        self.setWindowTitle("Powmenu")
        self.setStyleSheet(f"""
background-color: {config.BACKGROUND_COLOR};
color: {config.FORGROUND_COLOR};
        """)
        self.setFixedSize(*config.WINDOW_SIZE)
        self.central_widget = MainWidget()
        self.setCentralWidget(self.central_widget)

    def move_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

