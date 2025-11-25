# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1522, 1020)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 1481, 951))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(390, 860, 1081, 91))
        self.send_bar = QHBoxLayout(self.horizontalLayoutWidget)
        self.send_bar.setObjectName(u"send_bar")
        self.send_bar.setContentsMargins(0, 0, 0, 0)
        self.message_input = QTextEdit(self.horizontalLayoutWidget)
        self.message_input.setObjectName(u"message_input")
        font = QFont()
        font.setPointSize(13)
        self.message_input.setFont(font)

        self.send_bar.addWidget(self.message_input)

        self.send_button = QPushButton(self.horizontalLayoutWidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setMaximumSize(QSize(90, 90))

        self.send_bar.addWidget(self.send_button)

        self.horizontalLayoutWidget_2 = QWidget(self.frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 20, 1451, 71))
        self.contact_bar = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.contact_bar.setObjectName(u"contact_bar")
        self.contact_bar.setContentsMargins(0, 0, 0, 0)
        self.add_contact_button = QPushButton(self.horizontalLayoutWidget_2)
        self.add_contact_button.setObjectName(u"add_contact_button")
        self.add_contact_button.setMaximumSize(QSize(200, 90))

        self.contact_bar.addWidget(self.add_contact_button)

        self.horizontalSpacer = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.contact_bar.addItem(self.horizontalSpacer)

        self.current_contact = QLabel(self.horizontalLayoutWidget_2)
        self.current_contact.setObjectName(u"current_contact")
        font1 = QFont()
        font1.setPointSize(16)
        self.current_contact.setFont(font1)

        self.contact_bar.addWidget(self.current_contact)

        self.exit_button = QPushButton(self.horizontalLayoutWidget_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMaximumSize(QSize(60, 90))

        self.contact_bar.addWidget(self.exit_button)

        self.messages_scroll = QScrollArea(self.frame)
        self.messages_scroll.setObjectName(u"messages_scroll")
        self.messages_scroll.setGeometry(QRect(390, 110, 1081, 731))
        self.messages_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1079, 729))
        self.messages_scroll.setWidget(self.scrollAreaWidgetContents)
        self.Contactlist_scroll = QScrollArea(self.frame)
        self.Contactlist_scroll.setObjectName(u"Contactlist_scroll")
        self.Contactlist_scroll.setGeometry(QRect(20, 110, 361, 821))
        self.Contactlist_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 359, 819))
        self.Contactlist_scroll.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1522, 39))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.add_contact_button.setText(QCoreApplication.translate("MainWindow", u"add new contact", None))
        self.current_contact.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"exit", None))
    # retranslateUi

