# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowFVyVlY.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
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
        self.newProjectScreen = QWidget()
        self.newProjectScreen.setObjectName(u"newProjectScreen")
        self.gridLayout_3 = QGridLayout(self.newProjectScreen)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.projectName = QLineEdit(self.newProjectScreen)
        self.projectName.setObjectName(u"projectName")

        self.gridLayout_4.addWidget(self.projectName, 3, 2, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.projectNamespace = QLineEdit(self.newProjectScreen)
        self.projectNamespace.setObjectName(u"projectNamespace")
        self.projectNamespace.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.projectNamespace.setDragEnabled(False)

        self.gridLayout_4.addWidget(self.projectNamespace, 4, 2, 1, 1)

        self.minecraftVersion = QComboBox(self.newProjectScreen)
        self.minecraftVersion.setObjectName(u"minecraftVersion")

        self.gridLayout_4.addWidget(self.minecraftVersion, 8, 2, 1, 1)

        self.label_3 = QLabel(self.newProjectScreen)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 5, 1, 1, 1)

        self.projectAuthor = QLineEdit(self.newProjectScreen)
        self.projectAuthor.setObjectName(u"projectAuthor")

        self.gridLayout_4.addWidget(self.projectAuthor, 6, 2, 1, 1)

        self.projectDescription = QPlainTextEdit(self.newProjectScreen)
        self.projectDescription.setObjectName(u"projectDescription")

        self.gridLayout_4.addWidget(self.projectDescription, 5, 2, 1, 1)

        self.label = QLabel(self.newProjectScreen)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 3, 1, 1, 1)

        self.projectVersion = QLineEdit(self.newProjectScreen)
        self.projectVersion.setObjectName(u"projectVersion")

        self.gridLayout_4.addWidget(self.projectVersion, 7, 2, 1, 1)

        self.label_4 = QLabel(self.newProjectScreen)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 6, 1, 1, 1)

        self.label_6 = QLabel(self.newProjectScreen)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 7, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.label_5 = QLabel(self.newProjectScreen)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 8, 1, 1, 1)

        self.label_2 = QLabel(self.newProjectScreen)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 2, 1, 1, 2)

        self.newProjLabel = QLabel(self.newProjectScreen)
        self.newProjLabel.setObjectName(u"newProjLabel")

        self.gridLayout_4.addWidget(self.newProjLabel, 1, 1, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 1, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.appContainer.addWidget(self.newProjectScreen)

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
        self.projectNamespace.setInputMask("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Project Name:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pack Version:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Minecraft Version:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Namespace:", None))
        self.newProjLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">New Project</span></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

