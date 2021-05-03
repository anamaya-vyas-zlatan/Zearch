from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        #initializing the homescreen
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #adding navbaar
        navbar =QToolBar()
        self.addToolBar(navbar)

        #adding back option
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        #adding forward option
        frwd_button = QAction('Forward', self)
        frwd_button.triggered.connect(self.browser.forward)
        navbar.addAction(frwd_button)

        #adding reload option
        rel_button = QAction('Reload', self)
        rel_button.triggered.connect(self.browser.reload)
        navbar.addAction(rel_button)

        #redirect to home option
        home = QAction('Zearch', self)
        home.triggered.connect(self.navigate_home)
        navbar.addAction(home)

        #adding search bar in navbar
        self.url_bar =QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)

        #updating the url in search bar
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName('Zearch')
window = MainWindow()
app.exec_()