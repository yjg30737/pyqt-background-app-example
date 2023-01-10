import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        menu = QMenu()

        action = QAction("Quit", self)

        action.triggered.connect(app.quit)

        menu.addAction(action)

        # Create the tray icon
        tray_icon = QSystemTrayIcon(app)
        tray_icon.setIcon(QIcon('Stark-icon.png'))
        tray_icon.activated.connect(self.__activated)

        # Set the tray icon's menu
        tray_icon.setContextMenu(menu)

        # Show the tray icon
        tray_icon.show()

    def __activated(self, reason):
        if reason == 3:
            self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # to make this able to operate background even if this got closed
    app.setQuitOnLastWindowClosed(False)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
