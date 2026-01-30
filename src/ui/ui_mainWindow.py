# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowDiQsmL.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.appContainer = QStackedWidget(self.centralwidget)
        self.appContainer.setObjectName(u"appContainer")
        self.homeScreen = QWidget()
        self.homeScreen.setObjectName(u"homeScreen")
        self.gridLayout_2 = QGridLayout(self.homeScreen)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mainLayout = QGridLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.loadProjectBtn = QPushButton(self.homeScreen)
        self.loadProjectBtn.setObjectName(u"loadProjectBtn")

        self.mainLayout.addWidget(self.loadProjectBtn, 1, 1, 1, 1)

        self.settingsBtn = QPushButton(self.homeScreen)
        self.settingsBtn.setObjectName(u"settingsBtn")

        self.mainLayout.addWidget(self.settingsBtn, 3, 1, 1, 1)

        self.newProjectBtn = QPushButton(self.homeScreen)
        self.newProjectBtn.setObjectName(u"newProjectBtn")

        self.mainLayout.addWidget(self.newProjectBtn, 0, 1, 1, 1)

        self.copyrightLabel = QLabel(self.homeScreen)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.copyrightLabel, 4, 0, 1, 3)


        self.gridLayout_2.addLayout(self.mainLayout, 1, 0, 1, 1)

        self.titleLabel = QLabel(self.homeScreen)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout_2.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.appContainer.addWidget(self.homeScreen)
        self.projectScreen = QWidget()
        self.projectScreen.setObjectName(u"projectScreen")
        self.gridLayout_3 = QGridLayout(self.projectScreen)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.appContainer.addWidget(self.projectScreen)

        self.gridLayout.addWidget(self.appContainer, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        self.appContainer.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Redstone - v2026.1", None))
        self.loadProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Load Project", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.newProjectBtn.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.copyrightLabel.setText(QCoreApplication.translate("MainWindow", u"Created by Joel Da Dev - Copyright 2026", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Redstone</span></p><p align=\"center\"><span style=\" font-size:12pt;\">By JoelDaDev - v2026.1</span></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

