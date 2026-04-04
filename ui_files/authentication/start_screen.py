# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_start.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(412, 367)
        MainWindow.setStyleSheet(u"font: 12pt \"Franklin Gothic Book\";\n"
"background-color:white;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.choice_login = QPushButton(self.centralwidget)
        self.choice_login.setObjectName(u"choice_login")
        self.choice_login.setMinimumSize(QSize(0, 30))
        self.choice_login.setStyleSheet(u"background-color: #4693F5;\n"
"color:white;\n"
"border: 1px solid #ffffff;\n"
"border-radius:8px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.choice_login)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.choice_signup = QPushButton(self.centralwidget)
        self.choice_signup.setObjectName(u"choice_signup")
        self.choice_signup.setMinimumSize(QSize(0, 30))
        self.choice_signup.setStyleSheet(u"background-color: #4693F5;\n"
"color:white;\n"
"border: 1px solid #ffffff;\n"
"border-radius:8px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.choice_signup)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Messaging Project!", None))
        self.choice_login.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Or", None))
        self.choice_signup.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
    # retranslateUi

