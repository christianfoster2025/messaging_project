# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_contactdialogue.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 508)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 381, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header1 = QLabel(self.verticalLayoutWidget)
        self.header1.setObjectName(u"header1")
        self.header1.setMaximumSize(QSize(16777215, 31))

        self.verticalLayout.addWidget(self.header1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.alias_label = QLabel(self.verticalLayoutWidget)
        self.alias_label.setObjectName(u"alias_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.alias_label)

        self.alias_entry = QLineEdit(self.verticalLayoutWidget)
        self.alias_entry.setObjectName(u"alias_entry")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alias_entry.sizePolicy().hasHeightForWidth())
        self.alias_entry.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.alias_entry)

        self.wifi_mac_label = QLabel(self.verticalLayoutWidget)
        self.wifi_mac_label.setObjectName(u"wifi_mac_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.wifi_mac_label)

        self.wifi_mac_entry = QLineEdit(self.verticalLayoutWidget)
        self.wifi_mac_entry.setObjectName(u"wifi_mac_entry")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.wifi_mac_entry)

        self.bluetooth_mac_label = QLabel(self.verticalLayoutWidget)
        self.bluetooth_mac_label.setObjectName(u"bluetooth_mac_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.bluetooth_mac_label)

        self.bluetooth_mac_entry = QLineEdit(self.verticalLayoutWidget)
        self.bluetooth_mac_entry.setObjectName(u"bluetooth_mac_entry")
        sizePolicy.setHeightForWidth(self.bluetooth_mac_entry.sizePolicy().hasHeightForWidth())
        self.bluetooth_mac_entry.setSizePolicy(sizePolicy)
        self.bluetooth_mac_entry.setMaximumSize(QSize(300, 16777215))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.bluetooth_mac_entry)

        self.publickey_label = QLabel(self.verticalLayoutWidget)
        self.publickey_label.setObjectName(u"publickey_label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.publickey_label)

        self.publickey_entry = QLineEdit(self.verticalLayoutWidget)
        self.publickey_entry.setObjectName(u"publickey_entry")
        sizePolicy.setHeightForWidth(self.publickey_entry.sizePolicy().hasHeightForWidth())
        self.publickey_entry.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.publickey_entry)

        self.userid_label = QLabel(self.verticalLayoutWidget)
        self.userid_label.setObjectName(u"userid_label")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.userid_label)

        self.userid_entry = QLineEdit(self.verticalLayoutWidget)
        self.userid_entry.setObjectName(u"userid_entry")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.userid_entry)


        self.verticalLayout.addLayout(self.formLayout)

        self.form_submit = QDialogButtonBox(self.verticalLayoutWidget)
        self.form_submit.setObjectName(u"form_submit")
        self.form_submit.setOrientation(Qt.Horizontal)
        self.form_submit.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.form_submit)

        self.header2 = QLabel(self.verticalLayoutWidget)
        self.header2.setObjectName(u"header2")
        self.header2.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.header2)

        self.contact_info = QPlainTextEdit(self.verticalLayoutWidget)
        self.contact_info.setObjectName(u"contact_info")
        self.contact_info.setMinimumSize(QSize(361, 161))
        self.contact_info.setMaximumSize(QSize(361, 161))
        self.contact_info.setFrameShape(QFrame.NoFrame)
        self.contact_info.setFrameShadow(QFrame.Plain)
        self.contact_info.setReadOnly(True)
        self.contact_info.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.contact_info)


        self.retranslateUi(Dialog)
        self.form_submit.accepted.connect(Dialog.accept)
        self.form_submit.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.header1.setText(QCoreApplication.translate("Dialog", u"Add a Contact:", None))
        self.alias_label.setText(QCoreApplication.translate("Dialog", u"Enter Name:", None))
        self.wifi_mac_label.setText(QCoreApplication.translate("Dialog", u"Enter Wi-Fi MAC address:", None))
        self.bluetooth_mac_label.setText(QCoreApplication.translate("Dialog", u"Enter Bluetooth MAC address:", None))
        self.publickey_label.setText(QCoreApplication.translate("Dialog", u"Enter encryption Public key:", None))
        self.userid_label.setText(QCoreApplication.translate("Dialog", u"UserID:", None))
        self.header2.setText(QCoreApplication.translate("Dialog", u"Your Contact information:", None))
    # retranslateUi

