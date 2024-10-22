import os
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)

        self.set_layout()
        self.add_buttons()
        self.set_buttons_ui()
        self.set_actions()

    def set_layout(self):
        self._layout = QGridLayout()
        self.setLayout(self._layout)

    def add_buttons(self):
        self.poweroff = QPushButton()
        self.poweroff_label = QLabel("Poweroff")
        self._layout.addWidget(self.poweroff, 0, 0)
        self._layout.addWidget(self.poweroff_label, 1, 0)

        self.reboot = QPushButton()
        self.reboot_label = QLabel("Reboot")
        self._layout.addWidget(self.reboot, 0, 1)
        self._layout.addWidget(self.reboot_label, 1, 1)

        self.sleep = QPushButton()
        self.sleep_label = QLabel("Sleep")
        self._layout.addWidget(self.sleep, 0, 2)
        self._layout.addWidget(self.sleep_label, 1, 2)

        self.logout = QPushButton()
        self.logout_label = QLabel("Logout")
        self._layout.addWidget(self.logout, 0, 3)
        self._layout.addWidget(self.logout_label, 1, 3)

        self.exit = QPushButton()
        self.exit_label = QLabel("Exit")
        self._layout.addWidget(self.exit, 0, 4)
        self._layout.addWidget(self.exit_label, 1, 4)

    def set_buttons_ui(self):
        self.poweroff.setIcon(QIcon(os.path.join("/home/ali/Dev/powmenu/src/app/icons/poweroff.png")))
        self.poweroff.setIconSize(QSize(int(self.width() / 5), self.height()))
        self.poweroff.setStyleSheet("border: none;")
        self.poweroff_label.setAlignment(Qt.AlignCenter)

        self.reboot.setIcon(QIcon(os.path.join("/home/ali/Dev/powmenu/src/app/icons/reboot.png")))
        self.reboot.setIconSize(QSize(int(self.width() / 5), self.height()))
        self.reboot.setStyleSheet("border: none;")
        self.reboot_label.setAlignment(Qt.AlignCenter)

        self.sleep.setIcon(QIcon(os.path.join("/home/ali/Dev/powmenu/src/app/icons/sleep.png")))
        self.sleep.setIconSize(QSize(int(self.width() / 5), self.height()))
        self.sleep.setStyleSheet("border: none;")
        self.sleep_label.setAlignment(Qt.AlignCenter)

        self.logout.setIcon(QIcon(os.path.join("/home/ali/Dev/powmenu/src/app/icons/logout.png")))
        self.logout.setIconSize(QSize(int(self.width() / 5), self.height()))
        self.logout.setStyleSheet("border: none;")
        self.logout_label.setAlignment(Qt.AlignCenter)

        self.exit.setIcon(QIcon(os.path.join("/home/ali/Dev/powmenu/src/app/icons/exit.png")))
        self.exit.setIconSize(QSize(int(self.width() / 5), self.height()))
        self.exit.setStyleSheet("border: none;")
        self.exit_label.setAlignment(Qt.AlignCenter)

    def set_actions(self):
        self.poweroff.clicked.connect(lambda: os.system("poweroff"))
        self.reboot.clicked.connect(lambda: os.system("reboot"))
        self.sleep.clicked.connect(lambda: os.system("systemctl suspend"))
        self.logout.clicked.connect(lambda: os.system("pkill -KILL -u {}".format(os.getlogin())))
        self.exit.clicked.connect(lambda: sys.exit())


