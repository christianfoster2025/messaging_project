# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_reset_pw.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(412, 369)
        Dialog.setStyleSheet(u"font: 12pt \"Franklin Gothic Book\";\n"
"background-color:white;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Franklin Gothic Book"])
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.username_entry = QLineEdit(Dialog)
        self.username_entry.setObjectName(u"username_entry")

        self.verticalLayout.addWidget(self.username_entry)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.password_entry = QLineEdit(Dialog)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_entry)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.confirm_password = QLineEdit(Dialog)
        self.confirm_password.setObjectName(u"confirm_password")
        self.confirm_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.confirm_password)

        self.errorlabel = QLabel(Dialog)
        self.errorlabel.setObjectName(u"errorlabel")
        self.errorlabel.setStyleSheet(u"color:rgb(255, 0, 0)")

        self.verticalLayout.addWidget(self.errorlabel)

        self.submit_form = QPushButton(Dialog)
        self.submit_form.setObjectName(u"submit_form")
        self.submit_form.setMinimumSize(QSize(0, 30))
        self.submit_form.setStyleSheet(u"background-color: #4693F5;\n"
"color:white;\n"
"border: 1px solid #ffffff;\n"
"border-radius:8px;\n"
"")

        self.verticalLayout.addWidget(self.submit_form)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Reset Password:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Enter your username:", None))
        self.username_entry.setText("")
        self.username_entry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Create a new password:", None))
        self.password_entry.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Confirm your new password:", None))
        self.confirm_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.errorlabel.setText("")
        self.submit_form.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
    # retranslateUi

