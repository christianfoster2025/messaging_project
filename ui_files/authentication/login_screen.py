# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, Messaging_App):
        if not Messaging_App.objectName():
            Messaging_App.setObjectName(u"Messaging_App")
        Messaging_App.resize(412, 367)
        Messaging_App.setStyleSheet(u"font: 12pt \"Franklin Gothic Book\";\n"
"background-color:white;\n"
"\n"
"")
        self.centralwidget = QWidget(Messaging_App)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 60, 211, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.username_entry = QLineEdit(self.verticalLayoutWidget)
        self.username_entry.setObjectName(u"username_entry")

        self.verticalLayout.addWidget(self.username_entry)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.password_entry = QLineEdit(self.verticalLayoutWidget)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_entry)

        self.errorlabel = QLabel(self.verticalLayoutWidget)
        self.errorlabel.setObjectName(u"errorlabel")
        self.errorlabel.setStyleSheet(u"color:rgb(255, 0, 0)")

        self.verticalLayout.addWidget(self.errorlabel)

        self.submit_form = QPushButton(self.verticalLayoutWidget)
        self.submit_form.setObjectName(u"submit_form")
        self.submit_form.setMinimumSize(QSize(0, 30))
        self.submit_form.setStyleSheet(u"background-color: #4693F5;\n"
"color:white;\n"
"border: 1px solid #ffffff;\n"
"border-radius:8px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.submit_form)

        self.submit_form_2 = QPushButton(self.verticalLayoutWidget)
        self.submit_form_2.setObjectName(u"submit_form_2")
        self.submit_form_2.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Franklin Gothic Book"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.submit_form_2.setFont(font)
        self.submit_form_2.setStyleSheet(u"background-color: #4693F5;\n"
"color:white;\n"
"border: 1px solid #ffffff;\n"
"border-radius:8px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.submit_form_2)

        Messaging_App.setCentralWidget(self.centralwidget)

        self.retranslateUi(Messaging_App)

        QMetaObject.connectSlotsByName(Messaging_App)
    # setupUi

    def retranslateUi(self, Messaging_App):
        Messaging_App.setWindowTitle(QCoreApplication.translate("Messaging_App", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Messaging_App", u"Log in:", None))
        self.label_2.setText(QCoreApplication.translate("Messaging_App", u"Enter Your Username:", None))
        self.username_entry.setText("")
        self.username_entry.setPlaceholderText(QCoreApplication.translate("Messaging_App", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Messaging_App", u"Enter your Password:", None))
        self.password_entry.setPlaceholderText(QCoreApplication.translate("Messaging_App", u"Password", None))
        self.errorlabel.setText("")
        self.submit_form.setText(QCoreApplication.translate("Messaging_App", u"Log in", None))
        self.submit_form_2.setText(QCoreApplication.translate("Messaging_App", u"Forgot Password", None))
    # retranslateUi

