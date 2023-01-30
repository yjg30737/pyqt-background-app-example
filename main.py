import sys
import threading
import time
import asyncio

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QPushButton, QWidget, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        menu = QMenu()

        action = QAction("Quit", self)
        action.setIcon(QIcon('close.svg'))

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

        threadBtn = QPushButton('Execute Thread')
        threadBtn.clicked.connect(self.__executeThread)

        asyncBtn = QPushButton('Execute async-await')
        asyncBtn.clicked.connect(self.__executeAsyncAwait)

        lay = QVBoxLayout()
        lay.addWidget(threadBtn)
        lay.addWidget(asyncBtn)

        self.setLayout(lay)

    def __executeThread(self):
        t = threading.Thread(target=self.__waitThread)
        t.daemon = True
        t.start()

    def __executeAsyncAwait(self):
        asyncio.run(self.__waitAsyncAwait())

    def __waitThread(self):
        time.sleep(5)
        print("Finished thread")

    async def __waitAsyncAwait(self):
        await asyncio.sleep(5)
        print("Finished async-await")

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
