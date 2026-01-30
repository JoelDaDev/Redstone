# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newProjectozExOZ.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGraphicsView,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        self.packIconView = QGraphicsView(Dialog)
        self.packIconView.setObjectName(u"packIconView")
        self.packIconView.setGeometry(QRect(10, 20, 64, 64))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 20, 181, 18))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 40, 181, 41))
        self.packIconButton = QPushButton(Dialog)
        self.packIconButton.setObjectName(u"packIconButton")
        self.packIconButton.setGeometry(QRect(10, 20, 64, 64))
        self.packIconButton.setFlat(True)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 371, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.packTitle = QLineEdit(self.gridLayoutWidget)
        self.packTitle.setObjectName(u"packTitle")

        self.gridLayout.addWidget(self.packTitle, 1, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.packDescription = QLineEdit(self.gridLayoutWidget)
        self.packDescription.setObjectName(u"packDescription")

        self.gridLayout.addWidget(self.packDescription, 2, 2, 1, 1)

        self.packNamespace = QLineEdit(self.gridLayoutWidget)
        self.packNamespace.setObjectName(u"packNamespace")

        self.gridLayout.addWidget(self.packNamespace, 3, 2, 1, 1)

        self.packVersion = QComboBox(self.gridLayoutWidget)
        self.packVersion.setObjectName(u"packVersion")

        self.gridLayout.addWidget(self.packVersion, 4, 2, 1, 1)

        self.createProjectBtn = QPushButton(self.gridLayoutWidget)
        self.createProjectBtn.setObjectName(u"createProjectBtn")

        self.gridLayout.addWidget(self.createProjectBtn, 5, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"New Project", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.packIconButton.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Namespace", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Version", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.createProjectBtn.setText(QCoreApplication.translate("Dialog", u"Create Project", None))
    # retranslateUi

