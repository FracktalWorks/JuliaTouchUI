# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI_extended_abl.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setStyleSheet("QStatusBar {\n"
"    background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mainApplication = QtWidgets.QWidget(MainWindow)
        self.mainApplication.setObjectName("mainApplication")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainApplication)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.stackedWidget.setMinimumSize(QtCore.QSize(480, 320))
        self.stackedWidget.setMaximumSize(QtCore.QSize(480, 320))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("\n"
"background-color: rgb(40, 40, 40);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.loadingPage = QtWidgets.QWidget()
        self.loadingPage.setObjectName("loadingPage")
        self.LoadingLabel = QtWidgets.QLabel(self.loadingPage)
        self.LoadingLabel.setGeometry(QtCore.QRect(0, 0, 481, 321))
        self.LoadingLabel.setText("")
        self.LoadingLabel.setPixmap(QtGui.QPixmap("templates/img/splash.png"))
        self.LoadingLabel.setObjectName("LoadingLabel")
        self.loadingGif = QtWidgets.QLabel(self.loadingPage)
        self.loadingGif.setGeometry(QtCore.QRect(210, 210, 50, 50))
        self.loadingGif.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.loadingGif.setText("")
        self.loadingGif.setScaledContents(True)
        self.loadingGif.setObjectName("loadingGif")
        self.stackedWidget.addWidget(self.loadingPage)
        self.pgLock = QtWidgets.QWidget()
        self.pgLock.setObjectName("pgLock")
        self.pgLock_bt6 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt6.setGeometry(QtCore.QRect(120, 200, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt6.setFont(font)
        self.pgLock_bt6.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt6.setObjectName("pgLock_bt6")
        self.pgLock_bt0 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt0.setGeometry(QtCore.QRect(240, 260, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt0.setFont(font)
        self.pgLock_bt0.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt0.setObjectName("pgLock_bt0")
        self.pgLock_bt4 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt4.setGeometry(QtCore.QRect(360, 140, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt4.setFont(font)
        self.pgLock_bt4.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt4.setObjectName("pgLock_bt4")
        self.passwordlabel_4 = QtWidgets.QLabel(self.pgLock)
        self.passwordlabel_4.setGeometry(QtCore.QRect(20, 65, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.passwordlabel_4.setFont(font)
        self.passwordlabel_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwordlabel_4.setObjectName("passwordlabel_4")
        self.pgLock_btBackspace = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_btBackspace.setGeometry(QtCore.QRect(0, 260, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_btBackspace.setFont(font)
        self.pgLock_btBackspace.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_btBackspace.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("templates/img/backspace-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pgLock_btBackspace.setIcon(icon)
        self.pgLock_btBackspace.setIconSize(QtCore.QSize(35, 35))
        self.pgLock_btBackspace.setObjectName("pgLock_btBackspace")
        self.pgLock_btSubmit = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_btSubmit.setGeometry(QtCore.QRect(360, 260, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_btSubmit.setFont(font)
        self.pgLock_btSubmit.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_btSubmit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("templates/img/verification-mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pgLock_btSubmit.setIcon(icon1)
        self.pgLock_btSubmit.setIconSize(QtCore.QSize(35, 35))
        self.pgLock_btSubmit.setObjectName("pgLock_btSubmit")
        self.pgLock_bt9 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt9.setGeometry(QtCore.QRect(120, 260, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt9.setFont(font)
        self.pgLock_bt9.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt9.setObjectName("pgLock_bt9")
        self.pgLock_bt8 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt8.setGeometry(QtCore.QRect(360, 200, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt8.setFont(font)
        self.pgLock_bt8.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt8.setObjectName("pgLock_bt8")
        self.pgLock_bt1 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt1.setGeometry(QtCore.QRect(0, 140, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt1.setFont(font)
        self.pgLock_bt1.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt1.setObjectName("pgLock_bt1")
        self.passwordlabel_2 = QtWidgets.QLabel(self.pgLock)
        self.passwordlabel_2.setGeometry(QtCore.QRect(20, 20, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.passwordlabel_2.setFont(font)
        self.passwordlabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwordlabel_2.setObjectName("passwordlabel_2")
        self.pgLock_pin = QtWidgets.QLineEdit(self.pgLock)
        self.pgLock_pin.setGeometry(QtCore.QRect(220, 55, 241, 36))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        self.pgLock_pin.setFont(font)
        self.pgLock_pin.setStyleSheet("color: white;\n"
"background-color: rgb(40, 40, 40);\n"
"selection-color: rgb(40, 40, 40);\n"
"padding-top: 5;\n"
"border: 2px solid white;")
        self.pgLock_pin.setInputMask("")
        self.pgLock_pin.setMaxLength(8)
        self.pgLock_pin.setFrame(False)
        self.pgLock_pin.setAlignment(QtCore.Qt.AlignCenter)
        self.pgLock_pin.setReadOnly(True)
        self.pgLock_pin.setObjectName("pgLock_pin")
        self.pgLock_bt3 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt3.setGeometry(QtCore.QRect(240, 140, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt3.setFont(font)
        self.pgLock_bt3.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt3.setObjectName("pgLock_bt3")
        self.pgLock_bt7 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt7.setGeometry(QtCore.QRect(240, 200, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt7.setFont(font)
        self.pgLock_bt7.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt7.setObjectName("pgLock_bt7")
        self.passwordlabel_5 = QtWidgets.QLabel(self.pgLock)
        self.passwordlabel_5.setGeometry(QtCore.QRect(20, 110, 441, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.passwordlabel_5.setFont(font)
        self.passwordlabel_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwordlabel_5.setObjectName("passwordlabel_5")
        self.pgLock_HID = QtWidgets.QLabel(self.pgLock)
        self.pgLock_HID.setGeometry(QtCore.QRect(220, 20, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_HID.setFont(font)
        self.pgLock_HID.setStyleSheet("color: rgb(255, 255, 255);")
        self.pgLock_HID.setAlignment(QtCore.Qt.AlignCenter)
        self.pgLock_HID.setObjectName("pgLock_HID")
        self.pgLock_bt5 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt5.setGeometry(QtCore.QRect(0, 200, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt5.setFont(font)
        self.pgLock_bt5.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt5.setObjectName("pgLock_bt5")
        self.pgLock_bt2 = QtWidgets.QPushButton(self.pgLock)
        self.pgLock_bt2.setGeometry(QtCore.QRect(120, 140, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pgLock_bt2.setFont(font)
        self.pgLock_bt2.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-right: none;\n"
"border-bottom: none;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pgLock_bt2.setObjectName("pgLock_bt2")
        self.stackedWidget.addWidget(self.pgLock)
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.playPauseButton = QtWidgets.QPushButton(self.homePage)
        self.playPauseButton.setGeometry(QtCore.QRect(220, 240, 131, 61))
        self.playPauseButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.playPauseButton.setFont(font)
        self.playPauseButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.playPauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("templates/img/play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("templates/img/pause-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.playPauseButton.setIcon(icon2)
        self.playPauseButton.setIconSize(QtCore.QSize(30, 30))
        self.playPauseButton.setCheckable(True)
        self.playPauseButton.setChecked(False)
        self.playPauseButton.setAutoDefault(False)
        self.playPauseButton.setDefault(False)
        self.playPauseButton.setFlat(False)
        self.playPauseButton.setObjectName("playPauseButton")
        self.stopButton = QtWidgets.QPushButton(self.homePage)
        self.stopButton.setGeometry(QtCore.QRect(350, 240, 131, 61))
        self.stopButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.stopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("templates/img/video-player-stop-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setIconSize(QtCore.QSize(25, 25))
        self.stopButton.setObjectName("stopButton")
        self.line = QtWidgets.QFrame(self.homePage)
        self.line.setGeometry(QtCore.QRect(260, 90, 20, 111))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tool0Label = QtWidgets.QLabel(self.homePage)
        self.tool0Label.setGeometry(QtCore.QRect(40, 98, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0Label.setFont(font)
        self.tool0Label.setStyleSheet("\n"
"   color:  white;")
        self.tool0Label.setText("")
        self.tool0Label.setPixmap(QtGui.QPixmap("templates/img/Nozzle.png"))
        self.tool0Label.setScaledContents(True)
        self.tool0Label.setObjectName("tool0Label")
        self.FileNameLabel = QtWidgets.QLabel(self.homePage)
        self.FileNameLabel.setGeometry(QtCore.QRect(0, 170, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.FileNameLabel.setFont(font)
        self.FileNameLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.FileNameLabel.setObjectName("FileNameLabel")
        self.printTimeLabel = QtWidgets.QLabel(self.homePage)
        self.printTimeLabel.setGeometry(QtCore.QRect(0, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.printTimeLabel.setFont(font)
        self.printTimeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.printTimeLabel.setObjectName("printTimeLabel")
        self.fileName = QtWidgets.QLabel(self.homePage)
        self.fileName.setGeometry(QtCore.QRect(40, 170, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fileName.setScaledContents(True)
        self.fileName.setWordWrap(False)
        self.fileName.setObjectName("fileName")
        self.printTime = QtWidgets.QLabel(self.homePage)
        self.printTime.setGeometry(QtCore.QRect(100, 190, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        self.printTime.setFont(font)
        self.printTime.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.printTime.setObjectName("printTime")
        self.timeLeftLabel = QtWidgets.QLabel(self.homePage)
        self.timeLeftLabel.setGeometry(QtCore.QRect(0, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.timeLeftLabel.setFont(font)
        self.timeLeftLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.timeLeftLabel.setObjectName("timeLeftLabel")
        self.tool0TargetTemperature = QtWidgets.QLabel(self.homePage)
        self.tool0TargetTemperature.setGeometry(QtCore.QRect(40, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0TargetTemperature.setFont(font)
        self.tool0TargetTemperature.setStyleSheet("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.tool0TargetTemperature.setObjectName("tool0TargetTemperature")
        self.tool0TempBar = QtWidgets.QProgressBar(self.homePage)
        self.tool0TempBar.setGeometry(QtCore.QRect(80, 80, 16, 71))
        self.tool0TempBar.setStyleSheet("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.tool0TempBar.setMaximum(300)
        self.tool0TempBar.setProperty("value", 100)
        self.tool0TempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.tool0TempBar.setTextVisible(False)
        self.tool0TempBar.setOrientation(QtCore.Qt.Vertical)
        self.tool0TempBar.setObjectName("tool0TempBar")
        self.tool0ActualTemperature = QtWidgets.QLabel(self.homePage)
        self.tool0ActualTemperature.setGeometry(QtCore.QRect(35, 140, 71, 18))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tool0ActualTemperature.setFont(font)
        self.tool0ActualTemperature.setStyleSheet("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.tool0ActualTemperature.setObjectName("tool0ActualTemperature")
        self.menuButton = QtWidgets.QPushButton(self.homePage)
        self.menuButton.setGeometry(QtCore.QRect(0, 240, 111, 61))
        self.menuButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(13)
        self.menuButton.setFont(font)
        self.menuButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.menuButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("templates/img/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon4)
        self.menuButton.setIconSize(QtCore.QSize(40, 40))
        self.menuButton.setCheckable(False)
        self.menuButton.setAutoDefault(False)
        self.menuButton.setDefault(False)
        self.menuButton.setFlat(False)
        self.menuButton.setObjectName("menuButton")
        self.printPreviewMain = QtWidgets.QLabel(self.homePage)
        self.printPreviewMain.setGeometry(QtCore.QRect(280, 49, 191, 191))
        self.printPreviewMain.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.printPreviewMain.setText("")
        self.printPreviewMain.setPixmap(QtGui.QPixmap("templates/img/thumbnail.png"))
        self.printPreviewMain.setScaledContents(True)
        self.printPreviewMain.setObjectName("printPreviewMain")
        self.printProgressBar = QtWidgets.QProgressBar(self.homePage)
        self.printProgressBar.setGeometry(QtCore.QRect(0, 300, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.printProgressBar.setFont(font)
        self.printProgressBar.setStyleSheet("QProgressBar::chunk {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));\n"
"border: 1px solid green;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}\n"
"")
        self.printProgressBar.setMaximum(100)
        self.printProgressBar.setProperty("value", 0)
        self.printProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.printProgressBar.setTextVisible(True)
        self.printProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.printProgressBar.setObjectName("printProgressBar")
        self.timeLeft = QtWidgets.QLabel(self.homePage)
        self.timeLeft.setGeometry(QtCore.QRect(110, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        self.timeLeft.setFont(font)
        self.timeLeft.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.timeLeft.setWordWrap(False)
        self.timeLeft.setObjectName("timeLeft")
        self.printerStatus = QtWidgets.QLabel(self.homePage)
        self.printerStatus.setGeometry(QtCore.QRect(39, -2, 382, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.printerStatus.setFont(font)
        self.printerStatus.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 0);")
        self.printerStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.printerStatus.setWordWrap(True)
        self.printerStatus.setObjectName("printerStatus")
        self.controlButton = QtWidgets.QPushButton(self.homePage)
        self.controlButton.setGeometry(QtCore.QRect(110, 240, 111, 61))
        self.controlButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(13)
        self.controlButton.setFont(font)
        self.controlButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.controlButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("templates/img/settings-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.controlButton.setIcon(icon5)
        self.controlButton.setIconSize(QtCore.QSize(40, 40))
        self.controlButton.setCheckable(False)
        self.controlButton.setAutoDefault(False)
        self.controlButton.setDefault(False)
        self.controlButton.setFlat(False)
        self.controlButton.setObjectName("controlButton")
        self.printerStatusColour = QtWidgets.QLabel(self.homePage)
        self.printerStatusColour.setGeometry(QtCore.QRect(5, 6, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.printerStatusColour.setFont(font)
        self.printerStatusColour.setStyleSheet("     border: 1px solid rgb(87, 87, 87);\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:0, y2:0.534, stop:0 rgba(130, 203, 117, 255), stop:1 rgba(66, 191, 85, 255));")
        self.printerStatusColour.setText("")
        self.printerStatusColour.setAlignment(QtCore.Qt.AlignCenter)
        self.printerStatusColour.setObjectName("printerStatusColour")
        self.celciusLabel = QtWidgets.QLabel(self.homePage)
        self.celciusLabel.setGeometry(QtCore.QRect(100, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel.setFont(font)
        self.celciusLabel.setStyleSheet("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.celciusLabel.setObjectName("celciusLabel")
        self.statusBar = QtWidgets.QLabel(self.homePage)
        self.statusBar.setGeometry(QtCore.QRect(0, 0, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet("     border-bottom: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));")
        self.statusBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.statusBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusBar.setText("")
        self.statusBar.setObjectName("statusBar")
        self.celciusLabel_2 = QtWidgets.QLabel(self.homePage)
        self.celciusLabel_2.setGeometry(QtCore.QRect(220, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.celciusLabel_2.setFont(font)
        self.celciusLabel_2.setStyleSheet("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.celciusLabel_2.setObjectName("celciusLabel_2")
        self.bedTempBar = QtWidgets.QProgressBar(self.homePage)
        self.bedTempBar.setGeometry(QtCore.QRect(205, 80, 16, 71))
        self.bedTempBar.setStyleSheet("QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.522, y2:0, stop:0.0336134 rgba(74, 183, 255, 255), stop:1 rgba(53, 173, 242, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.bedTempBar.setMaximum(300)
        self.bedTempBar.setProperty("value", 10)
        self.bedTempBar.setAlignment(QtCore.Qt.AlignCenter)
        self.bedTempBar.setTextVisible(False)
        self.bedTempBar.setOrientation(QtCore.Qt.Vertical)
        self.bedTempBar.setObjectName("bedTempBar")
        self.bedActualTemperatute = QtWidgets.QLabel(self.homePage)
        self.bedActualTemperatute.setGeometry(QtCore.QRect(155, 140, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedActualTemperatute.setFont(font)
        self.bedActualTemperatute.setStyleSheet("\n"
"   color:  white;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.bedActualTemperatute.setObjectName("bedActualTemperatute")
        self.bedTargetTemperature = QtWidgets.QLabel(self.homePage)
        self.bedTargetTemperature.setGeometry(QtCore.QRect(155, 70, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedTargetTemperature.setFont(font)
        self.bedTargetTemperature.setStyleSheet("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.bedTargetTemperature.setObjectName("bedTargetTemperature")
        self.bedLabel = QtWidgets.QLabel(self.homePage)
        self.bedLabel.setGeometry(QtCore.QRect(150, 95, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.bedLabel.setFont(font)
        self.bedLabel.setStyleSheet("\n"
"   color:  white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.bedLabel.setText("")
        self.bedLabel.setPixmap(QtGui.QPixmap("templates/img/bed.png"))
        self.bedLabel.setScaledContents(True)
        self.bedLabel.setObjectName("bedLabel")
        self.ipStatus = QtWidgets.QLabel(self.homePage)
        self.ipStatus.setGeometry(QtCore.QRect(357, 0, 122, 20))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ipStatus.setFont(font)
        self.ipStatus.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 0);")
        self.ipStatus.setScaledContents(True)
        self.ipStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.ipStatus.setWordWrap(True)
        self.ipStatus.setObjectName("ipStatus")
        self.line.raise_()
        self.printPreviewMain.raise_()
        self.statusBar.raise_()
        self.playPauseButton.raise_()
        self.stopButton.raise_()
        self.tool0Label.raise_()
        self.FileNameLabel.raise_()
        self.printTimeLabel.raise_()
        self.fileName.raise_()
        self.printTime.raise_()
        self.timeLeftLabel.raise_()
        self.tool0TempBar.raise_()
        self.tool0ActualTemperature.raise_()
        self.tool0TargetTemperature.raise_()
        self.menuButton.raise_()
        self.timeLeft.raise_()
        self.controlButton.raise_()
        self.printProgressBar.raise_()
        self.printerStatus.raise_()
        self.printerStatusColour.raise_()
        self.celciusLabel.raise_()
        self.celciusLabel_2.raise_()
        self.bedTempBar.raise_()
        self.bedActualTemperatute.raise_()
        self.bedTargetTemperature.raise_()
        self.bedLabel.raise_()
        self.ipStatus.raise_()
        self.stackedWidget.addWidget(self.homePage)
        self.MenuPage = QtWidgets.QWidget()
        self.MenuPage.setObjectName("MenuPage")
        self.menuBackButton = QtWidgets.QPushButton(self.MenuPage)
        self.menuBackButton.setGeometry(QtCore.QRect(320, 160, 160, 160))
        self.menuBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.menuBackButton.setFont(font)
        self.menuBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.menuBackButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("templates/img/arrows-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBackButton.setIcon(icon6)
        self.menuBackButton.setIconSize(QtCore.QSize(50, 50))
        self.menuBackButton.setCheckable(False)
        self.menuBackButton.setObjectName("menuBackButton")
        self.menuControlButton = QtWidgets.QToolButton(self.MenuPage)
        self.menuControlButton.setGeometry(QtCore.QRect(160, 0, 160, 160))
        self.menuControlButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(18)
        self.menuControlButton.setFont(font)
        self.menuControlButton.setStyleSheet("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.menuControlButton.setIcon(icon5)
        self.menuControlButton.setIconSize(QtCore.QSize(80, 80))
        self.menuControlButton.setCheckable(False)
        self.menuControlButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuControlButton.setObjectName("menuControlButton")
        self.menuPrintButton = QtWidgets.QToolButton(self.MenuPage)
        self.menuPrintButton.setGeometry(QtCore.QRect(0, 0, 160, 160))
        self.menuPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(18)
        self.menuPrintButton.setFont(font)
        self.menuPrintButton.setStyleSheet("QToolButton {\n"
"    padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("templates/img/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuPrintButton.setIcon(icon7)
        self.menuPrintButton.setIconSize(QtCore.QSize(80, 80))
        self.menuPrintButton.setCheckable(False)
        self.menuPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuPrintButton.setObjectName("menuPrintButton")
        self.menuSettingsButton = QtWidgets.QToolButton(self.MenuPage)
        self.menuSettingsButton.setGeometry(QtCore.QRect(160, 160, 160, 160))
        self.menuSettingsButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(18)
        self.menuSettingsButton.setFont(font)
        self.menuSettingsButton.setStyleSheet("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("templates/img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSettingsButton.setIcon(icon8)
        self.menuSettingsButton.setIconSize(QtCore.QSize(80, 80))
        self.menuSettingsButton.setCheckable(False)
        self.menuSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuSettingsButton.setObjectName("menuSettingsButton")
        self.menuCartButton = QtWidgets.QToolButton(self.MenuPage)
        self.menuCartButton.setGeometry(QtCore.QRect(0, 160, 160, 160))
        self.menuCartButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(18)
        self.menuCartButton.setFont(font)
        self.menuCartButton.setStyleSheet("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("templates/img/cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCartButton.setIcon(icon9)
        self.menuCartButton.setIconSize(QtCore.QSize(80, 80))
        self.menuCartButton.setCheckable(False)
        self.menuCartButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuCartButton.setAutoRaise(False)
        self.menuCartButton.setObjectName("menuCartButton")
        self.menuCalibrateButton = QtWidgets.QToolButton(self.MenuPage)
        self.menuCalibrateButton.setGeometry(QtCore.QRect(320, 0, 160, 160))
        self.menuCalibrateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(18)
        self.menuCalibrateButton.setFont(font)
        self.menuCalibrateButton.setStyleSheet("QToolButton {\n"
"padding-top: 20px;\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("templates/img/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCalibrateButton.setIcon(icon10)
        self.menuCalibrateButton.setIconSize(QtCore.QSize(80, 80))
        self.menuCalibrateButton.setCheckable(False)
        self.menuCalibrateButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.menuCalibrateButton.setObjectName("menuCalibrateButton")
        self.menuSettingsButton.raise_()
        self.menuControlButton.raise_()
        self.menuCartButton.raise_()
        self.menuCalibrateButton.raise_()
        self.menuBackButton.raise_()
        self.menuPrintButton.raise_()
        self.stackedWidget.addWidget(self.MenuPage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.scrollArea = QtWidgets.QScrollArea(self.settingsPage)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 80px;\n"
"     margin: 70px 0 70px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 461, 630))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 3, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settingsBackButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.settingsBackButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.settingsBackButton.setFont(font)
        self.settingsBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.settingsBackButton.setText("")
        self.settingsBackButton.setIcon(icon6)
        self.settingsBackButton.setIconSize(QtCore.QSize(50, 50))
        self.settingsBackButton.setCheckable(False)
        self.settingsBackButton.setAutoDefault(False)
        self.settingsBackButton.setDefault(False)
        self.settingsBackButton.setFlat(False)
        self.settingsBackButton.setObjectName("settingsBackButton")
        self.verticalLayout.addWidget(self.settingsBackButton)
        self.networkSettingsButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.networkSettingsButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.networkSettingsButton.setFont(font)
        self.networkSettingsButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.networkSettingsButton.setIconSize(QtCore.QSize(40, 40))
        self.networkSettingsButton.setObjectName("networkSettingsButton")
        self.verticalLayout.addWidget(self.networkSettingsButton)
        self.displaySettingsButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.displaySettingsButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.displaySettingsButton.setFont(font)
        self.displaySettingsButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.displaySettingsButton.setIconSize(QtCore.QSize(40, 40))
        self.displaySettingsButton.setObjectName("displaySettingsButton")
        self.verticalLayout.addWidget(self.displaySettingsButton)
        self.pairPhoneButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pairPhoneButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.pairPhoneButton.setFont(font)
        self.pairPhoneButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pairPhoneButton.setIconSize(QtCore.QSize(40, 40))
        self.pairPhoneButton.setObjectName("pairPhoneButton")
        self.verticalLayout.addWidget(self.pairPhoneButton)
        self.OTAButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.OTAButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.OTAButton.setFont(font)
        self.OTAButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.OTAButton.setIconSize(QtCore.QSize(40, 40))
        self.OTAButton.setObjectName("OTAButton")
        self.verticalLayout.addWidget(self.OTAButton)
        self.versionButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.versionButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.versionButton.setFont(font)
        self.versionButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.versionButton.setIconSize(QtCore.QSize(40, 40))
        self.versionButton.setObjectName("versionButton")
        self.verticalLayout.addWidget(self.versionButton)
        self.restorePrintSettingsButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.restorePrintSettingsButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.restorePrintSettingsButton.setFont(font)
        self.restorePrintSettingsButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.restorePrintSettingsButton.setIconSize(QtCore.QSize(40, 40))
        self.restorePrintSettingsButton.setObjectName("restorePrintSettingsButton")
        self.verticalLayout.addWidget(self.restorePrintSettingsButton)
        self.restoreFactoryDefaultsButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.restoreFactoryDefaultsButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.restoreFactoryDefaultsButton.setFont(font)
        self.restoreFactoryDefaultsButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.restoreFactoryDefaultsButton.setIconSize(QtCore.QSize(40, 40))
        self.restoreFactoryDefaultsButton.setObjectName("restoreFactoryDefaultsButton")
        self.verticalLayout.addWidget(self.restoreFactoryDefaultsButton)
        self.restartButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.restartButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.restartButton.setFont(font)
        self.restartButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.restartButton.setIconSize(QtCore.QSize(40, 40))
        self.restartButton.setObjectName("restartButton")
        self.verticalLayout.addWidget(self.restartButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.settingsPage)
        self.QRCodePage = QtWidgets.QWidget()
        self.QRCodePage.setObjectName("QRCodePage")
        self.QRCodeBackButton = QtWidgets.QPushButton(self.QRCodePage)
        self.QRCodeBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.QRCodeBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.QRCodeBackButton.setFont(font)
        self.QRCodeBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.QRCodeBackButton.setText("")
        self.QRCodeBackButton.setIcon(icon6)
        self.QRCodeBackButton.setIconSize(QtCore.QSize(50, 50))
        self.QRCodeBackButton.setCheckable(False)
        self.QRCodeBackButton.setAutoDefault(False)
        self.QRCodeBackButton.setDefault(False)
        self.QRCodeBackButton.setFlat(False)
        self.QRCodeBackButton.setObjectName("QRCodeBackButton")
        self.QRCodeBackground = QtWidgets.QLabel(self.QRCodePage)
        self.QRCodeBackground.setGeometry(QtCore.QRect(120, 0, 251, 251))
        self.QRCodeBackground.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.QRCodeBackground.setText("")
        self.QRCodeBackground.setObjectName("QRCodeBackground")
        self.QRCodeLabel = QtWidgets.QLabel(self.QRCodePage)
        self.QRCodeLabel.setGeometry(QtCore.QRect(120, 0, 251, 251))
        self.QRCodeLabel.setStyleSheet("")
        self.QRCodeLabel.setText("")
        self.QRCodeLabel.setScaledContents(True)
        self.QRCodeLabel.setObjectName("QRCodeLabel")
        self.QRCodeBackground.raise_()
        self.QRCodeLabel.raise_()
        self.QRCodeBackButton.raise_()
        self.stackedWidget.addWidget(self.QRCodePage)
        self.wifiSettingsPage = QtWidgets.QWidget()
        self.wifiSettingsPage.setObjectName("wifiSettingsPage")
        self.wifiSettingsComboBox = QtWidgets.QComboBox(self.wifiSettingsPage)
        self.wifiSettingsComboBox.setGeometry(QtCore.QRect(0, 40, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        self.wifiSettingsComboBox.setFont(font)
        self.wifiSettingsComboBox.setStyleSheet(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}")
        self.wifiSettingsComboBox.setEditable(False)
        self.wifiSettingsComboBox.setMaxVisibleItems(8)
        self.wifiSettingsComboBox.setIconSize(QtCore.QSize(30, 30))
        self.wifiSettingsComboBox.setObjectName("wifiSettingsComboBox")
        self.ssidlabel = QtWidgets.QLabel(self.wifiSettingsPage)
        self.ssidlabel.setGeometry(QtCore.QRect(0, 0, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ssidlabel.setFont(font)
        self.ssidlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ssidlabel.setObjectName("ssidlabel")
        self.passwordlabel = QtWidgets.QLabel(self.wifiSettingsPage)
        self.passwordlabel.setGeometry(QtCore.QRect(0, 130, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwordlabel.setObjectName("passwordlabel")
        self.wifiSettingsDoneButton = QtWidgets.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsDoneButton.setGeometry(QtCore.QRect(0, 230, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.wifiSettingsDoneButton.setFont(font)
        self.wifiSettingsDoneButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.wifiSettingsDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsDoneButton.setObjectName("wifiSettingsDoneButton")
        self.wifiSettingsCancelButton = QtWidgets.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsCancelButton.setGeometry(QtCore.QRect(250, 230, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.wifiSettingsCancelButton.setFont(font)
        self.wifiSettingsCancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.wifiSettingsCancelButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsCancelButton.setObjectName("wifiSettingsCancelButton")
        self.wifiSettingsSSIDKeyboardButton = QtWidgets.QPushButton(self.wifiSettingsPage)
        self.wifiSettingsSSIDKeyboardButton.setGeometry(QtCore.QRect(419, 40, 62, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(19)
        self.wifiSettingsSSIDKeyboardButton.setFont(font)
        self.wifiSettingsSSIDKeyboardButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.wifiSettingsSSIDKeyboardButton.setIconSize(QtCore.QSize(40, 40))
        self.wifiSettingsSSIDKeyboardButton.setObjectName("wifiSettingsSSIDKeyboardButton")
        self.hiddenCheckBox = QtWidgets.QCheckBox(self.wifiSettingsPage)
        self.hiddenCheckBox.setGeometry(QtCore.QRect(0, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        self.hiddenCheckBox.setFont(font)
        self.hiddenCheckBox.setStyleSheet("QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(./templates/img/check-box.png);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(./templates/img/blank-check-box.png);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.hiddenCheckBox.setIconSize(QtCore.QSize(40, 40))
        self.hiddenCheckBox.setChecked(False)
        self.hiddenCheckBox.setObjectName("hiddenCheckBox")
        self.wifiSettingsComboBox.raise_()
        self.ssidlabel.raise_()
        self.passwordlabel.raise_()
        self.wifiSettingsSSIDKeyboardButton.raise_()
        self.wifiSettingsCancelButton.raise_()
        self.wifiSettingsDoneButton.raise_()
        self.hiddenCheckBox.raise_()
        self.stackedWidget.addWidget(self.wifiSettingsPage)
        self.ethSettingsPage = QtWidgets.QWidget()
        self.ethSettingsPage.setObjectName("ethSettingsPage")
        self.ethSettingsDoneButton = QtWidgets.QPushButton(self.ethSettingsPage)
        self.ethSettingsDoneButton.setGeometry(QtCore.QRect(0, 230, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.ethSettingsDoneButton.setFont(font)
        self.ethSettingsDoneButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.ethSettingsDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.ethSettingsDoneButton.setObjectName("ethSettingsDoneButton")
        self.ethSettingsCancelButton = QtWidgets.QPushButton(self.ethSettingsPage)
        self.ethSettingsCancelButton.setGeometry(QtCore.QRect(250, 230, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.ethSettingsCancelButton.setFont(font)
        self.ethSettingsCancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.ethSettingsCancelButton.setIconSize(QtCore.QSize(40, 40))
        self.ethSettingsCancelButton.setObjectName("ethSettingsCancelButton")
        self.ethStaticCheckBox = QtWidgets.QCheckBox(self.ethSettingsPage)
        self.ethStaticCheckBox.setGeometry(QtCore.QRect(10, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        self.ethStaticCheckBox.setFont(font)
        self.ethStaticCheckBox.setStyleSheet("QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(./templates/img/check-box.png);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(./templates/img/blank-check-box.png);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.ethStaticCheckBox.setIconSize(QtCore.QSize(40, 40))
        self.ethStaticCheckBox.setChecked(False)
        self.ethStaticCheckBox.setObjectName("ethStaticCheckBox")
        self.ethStaticSettings = QtWidgets.QWidget(self.ethSettingsPage)
        self.ethStaticSettings.setEnabled(True)
        self.ethStaticSettings.setGeometry(QtCore.QRect(0, 70, 481, 151))
        self.ethStaticSettings.setObjectName("ethStaticSettings")
        self.ethStaticIpLabel = QtWidgets.QLabel(self.ethStaticSettings)
        self.ethStaticIpLabel.setGeometry(QtCore.QRect(10, 10, 110, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ethStaticIpLabel.setFont(font)
        self.ethStaticIpLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ethStaticIpLabel.setObjectName("ethStaticIpLabel")
        self.ethStaticGatewayLabel = QtWidgets.QLabel(self.ethStaticSettings)
        self.ethStaticGatewayLabel.setGeometry(QtCore.QRect(10, 60, 110, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ethStaticGatewayLabel.setFont(font)
        self.ethStaticGatewayLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ethStaticGatewayLabel.setObjectName("ethStaticGatewayLabel")
        self.ethStaticGatewayKeyboardButton = QtWidgets.QPushButton(self.ethStaticSettings)
        self.ethStaticGatewayKeyboardButton.setGeometry(QtCore.QRect(420, 60, 60, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ethStaticGatewayKeyboardButton.setFont(font)
        self.ethStaticGatewayKeyboardButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.ethStaticGatewayKeyboardButton.setIconSize(QtCore.QSize(40, 40))
        self.ethStaticGatewayKeyboardButton.setObjectName("ethStaticGatewayKeyboardButton")
        self.ethStaticIpKeyboardButton = QtWidgets.QPushButton(self.ethStaticSettings)
        self.ethStaticIpKeyboardButton.setEnabled(True)
        self.ethStaticIpKeyboardButton.setGeometry(QtCore.QRect(420, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ethStaticIpKeyboardButton.setFont(font)
        self.ethStaticIpKeyboardButton.setAutoFillBackground(False)
        self.ethStaticIpKeyboardButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(0, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.ethStaticIpKeyboardButton.setIconSize(QtCore.QSize(40, 40))
        self.ethStaticIpKeyboardButton.setObjectName("ethStaticIpKeyboardButton")
        self.stackedWidget.addWidget(self.ethSettingsPage)
        self.networkSettingsPage = QtWidgets.QWidget()
        self.networkSettingsPage.setObjectName("networkSettingsPage")
        self.networkInfoButton = QtWidgets.QPushButton(self.networkSettingsPage)
        self.networkInfoButton.setGeometry(QtCore.QRect(0, 0, 480, 70))
        self.networkInfoButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.networkInfoButton.setFont(font)
        self.networkInfoButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.networkInfoButton.setIconSize(QtCore.QSize(40, 40))
        self.networkInfoButton.setObjectName("networkInfoButton")
        self.configureWifiButton = QtWidgets.QPushButton(self.networkSettingsPage)
        self.configureWifiButton.setGeometry(QtCore.QRect(0, 70, 480, 70))
        self.configureWifiButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.configureWifiButton.setFont(font)
        self.configureWifiButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.configureWifiButton.setIconSize(QtCore.QSize(40, 40))
        self.configureWifiButton.setObjectName("configureWifiButton")
        self.configureEthButton = QtWidgets.QPushButton(self.networkSettingsPage)
        self.configureEthButton.setGeometry(QtCore.QRect(0, 140, 480, 70))
        self.configureEthButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.configureEthButton.setFont(font)
        self.configureEthButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.configureEthButton.setIconSize(QtCore.QSize(40, 40))
        self.configureEthButton.setObjectName("configureEthButton")
        self.networkSettingsBackButton = QtWidgets.QPushButton(self.networkSettingsPage)
        self.networkSettingsBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.networkSettingsBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.networkSettingsBackButton.setFont(font)
        self.networkSettingsBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.networkSettingsBackButton.setText("")
        self.networkSettingsBackButton.setIcon(icon6)
        self.networkSettingsBackButton.setIconSize(QtCore.QSize(50, 50))
        self.networkSettingsBackButton.setCheckable(False)
        self.networkSettingsBackButton.setAutoDefault(False)
        self.networkSettingsBackButton.setDefault(False)
        self.networkSettingsBackButton.setFlat(False)
        self.networkSettingsBackButton.setObjectName("networkSettingsBackButton")
        self.stackedWidget.addWidget(self.networkSettingsPage)
        self.displaySettingsPage = QtWidgets.QWidget()
        self.displaySettingsPage.setObjectName("displaySettingsPage")
        self.displaySettingsBackButton = QtWidgets.QPushButton(self.displaySettingsPage)
        self.displaySettingsBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.displaySettingsBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.displaySettingsBackButton.setFont(font)
        self.displaySettingsBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.displaySettingsBackButton.setText("")
        self.displaySettingsBackButton.setIcon(icon6)
        self.displaySettingsBackButton.setIconSize(QtCore.QSize(50, 50))
        self.displaySettingsBackButton.setCheckable(False)
        self.displaySettingsBackButton.setAutoDefault(False)
        self.displaySettingsBackButton.setDefault(False)
        self.displaySettingsBackButton.setFlat(False)
        self.displaySettingsBackButton.setObjectName("displaySettingsBackButton")
        self.calibrateTouch = QtWidgets.QPushButton(self.displaySettingsPage)
        self.calibrateTouch.setGeometry(QtCore.QRect(0, 70, 480, 70))
        self.calibrateTouch.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.calibrateTouch.setFont(font)
        self.calibrateTouch.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.calibrateTouch.setIconSize(QtCore.QSize(40, 40))
        self.calibrateTouch.setObjectName("calibrateTouch")
        self.rotateDisplay = QtWidgets.QPushButton(self.displaySettingsPage)
        self.rotateDisplay.setGeometry(QtCore.QRect(0, 0, 480, 70))
        self.rotateDisplay.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.rotateDisplay.setFont(font)
        self.rotateDisplay.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.rotateDisplay.setIconSize(QtCore.QSize(40, 40))
        self.rotateDisplay.setObjectName("rotateDisplay")
        self.stackedWidget.addWidget(self.displaySettingsPage)
        self.rotateDisplaySettingsPage = QtWidgets.QWidget()
        self.rotateDisplaySettingsPage.setObjectName("rotateDisplaySettingsPage")
        self.rotateDisplaySettingsDoneButton = QtWidgets.QPushButton(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsDoneButton.setGeometry(QtCore.QRect(0, 230, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.rotateDisplaySettingsDoneButton.setFont(font)
        self.rotateDisplaySettingsDoneButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.rotateDisplaySettingsDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.rotateDisplaySettingsDoneButton.setObjectName("rotateDisplaySettingsDoneButton")
        self.rotateDisplaySettingsCancelButton = QtWidgets.QPushButton(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsCancelButton.setGeometry(QtCore.QRect(250, 230, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.rotateDisplaySettingsCancelButton.setFont(font)
        self.rotateDisplaySettingsCancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.rotateDisplaySettingsCancelButton.setIconSize(QtCore.QSize(40, 40))
        self.rotateDisplaySettingsCancelButton.setObjectName("rotateDisplaySettingsCancelButton")
        self.rotateDisplaySettingsComboBox = QtWidgets.QComboBox(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsComboBox.setGeometry(QtCore.QRect(10, 50, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        self.rotateDisplaySettingsComboBox.setFont(font)
        self.rotateDisplaySettingsComboBox.setStyleSheet(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}")
        self.rotateDisplaySettingsComboBox.setEditable(False)
        self.rotateDisplaySettingsComboBox.setMaxVisibleItems(8)
        self.rotateDisplaySettingsComboBox.setIconSize(QtCore.QSize(30, 30))
        self.rotateDisplaySettingsComboBox.setObjectName("rotateDisplaySettingsComboBox")
        self.rotateDisplaySettingsComboBox.addItem("")
        self.rotateDisplaySettingsComboBox.addItem("")
        self.rotateDisplaySettingsLabel = QtWidgets.QLabel(self.rotateDisplaySettingsPage)
        self.rotateDisplaySettingsLabel.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rotateDisplaySettingsLabel.setFont(font)
        self.rotateDisplaySettingsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.rotateDisplaySettingsLabel.setObjectName("rotateDisplaySettingsLabel")
        self.stackedWidget.addWidget(self.rotateDisplaySettingsPage)
        self.networkInfoPage = QtWidgets.QWidget()
        self.networkInfoPage.setObjectName("networkInfoPage")
        self.hostnameLabel = QtWidgets.QLabel(self.networkInfoPage)
        self.hostnameLabel.setGeometry(QtCore.QRect(10, 0, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hostnameLabel.setFont(font)
        self.hostnameLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.hostnameLabel.setObjectName("hostnameLabel")
        self.hostname = QtWidgets.QLabel(self.networkInfoPage)
        self.hostname.setGeometry(QtCore.QRect(10, 22, 240, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.hostname.setFont(font)
        self.hostname.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.hostname.setObjectName("hostname")
        self.wifiIpLabel = QtWidgets.QLabel(self.networkInfoPage)
        self.wifiIpLabel.setGeometry(QtCore.QRect(10, 90, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiIpLabel.setFont(font)
        self.wifiIpLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.wifiIpLabel.setObjectName("wifiIpLabel")
        self.wifiMac = QtWidgets.QLabel(self.networkInfoPage)
        self.wifiMac.setGeometry(QtCore.QRect(10, 110, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.wifiMac.setFont(font)
        self.wifiMac.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.wifiMac.setObjectName("wifiMac")
        self.lanIpLabel = QtWidgets.QLabel(self.networkInfoPage)
        self.lanIpLabel.setGeometry(QtCore.QRect(10, 170, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lanIpLabel.setFont(font)
        self.lanIpLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lanIpLabel.setObjectName("lanIpLabel")
        self.lanMac = QtWidgets.QLabel(self.networkInfoPage)
        self.lanMac.setGeometry(QtCore.QRect(10, 190, 240, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lanMac.setFont(font)
        self.lanMac.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lanMac.setObjectName("lanMac")
        self.networkInfoBackButton = QtWidgets.QPushButton(self.networkInfoPage)
        self.networkInfoBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.networkInfoBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.networkInfoBackButton.setFont(font)
        self.networkInfoBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.networkInfoBackButton.setText("")
        self.networkInfoBackButton.setIcon(icon6)
        self.networkInfoBackButton.setIconSize(QtCore.QSize(50, 50))
        self.networkInfoBackButton.setCheckable(False)
        self.networkInfoBackButton.setAutoDefault(False)
        self.networkInfoBackButton.setDefault(False)
        self.networkInfoBackButton.setFlat(False)
        self.networkInfoBackButton.setObjectName("networkInfoBackButton")
        self.wifiMacLabel = QtWidgets.QLabel(self.networkInfoPage)
        self.wifiMacLabel.setGeometry(QtCore.QRect(241, 90, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiMacLabel.setFont(font)
        self.wifiMacLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.wifiMacLabel.setObjectName("wifiMacLabel")
        self.lanMacLabel = QtWidgets.QLabel(self.networkInfoPage)
        self.lanMacLabel.setGeometry(QtCore.QRect(241, 170, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lanMacLabel.setFont(font)
        self.lanMacLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lanMacLabel.setObjectName("lanMacLabel")
        self.wifiIp = QtWidgets.QLabel(self.networkInfoPage)
        self.wifiIp.setGeometry(QtCore.QRect(241, 110, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.wifiIp.setFont(font)
        self.wifiIp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.wifiIp.setObjectName("wifiIp")
        self.lanIp = QtWidgets.QLabel(self.networkInfoPage)
        self.lanIp.setGeometry(QtCore.QRect(241, 190, 240, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lanIp.setFont(font)
        self.lanIp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lanIp.setObjectName("lanIp")
        self.wifiApLabel = QtWidgets.QLabel(self.networkInfoPage)
        self.wifiApLabel.setGeometry(QtCore.QRect(241, 0, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wifiApLabel.setFont(font)
        self.wifiApLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.wifiApLabel.setObjectName("wifiApLabel")
        self.wifiAp = QtWidgets.QLabel(self.networkInfoPage)
        self.wifiAp.setGeometry(QtCore.QRect(241, 22, 240, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.wifiAp.setFont(font)
        self.wifiAp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.wifiAp.setObjectName("wifiAp")
        self.hostnameLabel.raise_()
        self.wifiIpLabel.raise_()
        self.wifiMac.raise_()
        self.lanIpLabel.raise_()
        self.lanMac.raise_()
        self.networkInfoBackButton.raise_()
        self.hostname.raise_()
        self.wifiMacLabel.raise_()
        self.lanMacLabel.raise_()
        self.wifiIp.raise_()
        self.lanIp.raise_()
        self.wifiApLabel.raise_()
        self.wifiAp.raise_()
        self.stackedWidget.addWidget(self.networkInfoPage)
        self.OTAUpdatePage = QtWidgets.QWidget()
        self.OTAUpdatePage.setObjectName("OTAUpdatePage")
        self.updateListWidget = QtWidgets.QListWidget(self.OTAUpdatePage)
        self.updateListWidget.setGeometry(QtCore.QRect(0, 0, 481, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.updateListWidget.setFont(font)
        self.updateListWidget.setStyleSheet("\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 62px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QListView::item {\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"outline: none;\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.updateListWidget.setObjectName("updateListWidget")
        self.softwareUpdateBackButton = QtWidgets.QPushButton(self.OTAUpdatePage)
        self.softwareUpdateBackButton.setGeometry(QtCore.QRect(250, 250, 231, 71))
        self.softwareUpdateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.softwareUpdateBackButton.setFont(font)
        self.softwareUpdateBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.softwareUpdateBackButton.setText("")
        self.softwareUpdateBackButton.setIcon(icon6)
        self.softwareUpdateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.softwareUpdateBackButton.setCheckable(False)
        self.softwareUpdateBackButton.setAutoDefault(False)
        self.softwareUpdateBackButton.setDefault(False)
        self.softwareUpdateBackButton.setFlat(False)
        self.softwareUpdateBackButton.setObjectName("softwareUpdateBackButton")
        self.performUpdateButton = QtWidgets.QPushButton(self.OTAUpdatePage)
        self.performUpdateButton.setGeometry(QtCore.QRect(0, 250, 251, 71))
        self.performUpdateButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(17)
        self.performUpdateButton.setFont(font)
        self.performUpdateButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("templates/img/update-arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.performUpdateButton.setIcon(icon11)
        self.performUpdateButton.setIconSize(QtCore.QSize(40, 40))
        self.performUpdateButton.setCheckable(False)
        self.performUpdateButton.setAutoDefault(False)
        self.performUpdateButton.setDefault(False)
        self.performUpdateButton.setFlat(False)
        self.performUpdateButton.setObjectName("performUpdateButton")
        self.stackedWidget.addWidget(self.OTAUpdatePage)
        self.softwareUpdateProgressPage = QtWidgets.QWidget()
        self.softwareUpdateProgressPage.setObjectName("softwareUpdateProgressPage")
        self.logTextEdit = QtWidgets.QTextEdit(self.softwareUpdateProgressPage)
        self.logTextEdit.setGeometry(QtCore.QRect(0, 0, 481, 321))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(10)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setStyleSheet("QTextEdit{\n"
"background-color:  rgb(40, 40, 40);\n"
"/*font-color: white;*/\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 30px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"")
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.stackedWidget.addWidget(self.softwareUpdateProgressPage)
        self.firmwareUpdateProgressPage = QtWidgets.QWidget()
        self.firmwareUpdateProgressPage.setObjectName("firmwareUpdateProgressPage")
        self.firmwareUpdateLog = QtWidgets.QTextEdit(self.firmwareUpdateProgressPage)
        self.firmwareUpdateLog.setGeometry(QtCore.QRect(0, 0, 481, 250))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(12)
        self.firmwareUpdateLog.setFont(font)
        self.firmwareUpdateLog.setStyleSheet("QTextEdit{\n"
"background-color:  rgb(40, 40, 40);\n"
"/*font-color: white;*/\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid black; \n"
"border-radius: 5px;\n"
"background: rgb(40,40,40);\n"
"width: 30px;\n"
"}\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"border: 2px solid grey;\n"
"width: 5px;\n"
"height: 5px;\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"")
        self.firmwareUpdateLog.setReadOnly(True)
        self.firmwareUpdateLog.setObjectName("firmwareUpdateLog")
        self.firmwareUpdateBackButton = QtWidgets.QPushButton(self.firmwareUpdateProgressPage)
        self.firmwareUpdateBackButton.setEnabled(False)
        self.firmwareUpdateBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.firmwareUpdateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.firmwareUpdateBackButton.setFont(font)
        self.firmwareUpdateBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.firmwareUpdateBackButton.setText("")
        self.firmwareUpdateBackButton.setIcon(icon6)
        self.firmwareUpdateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.firmwareUpdateBackButton.setCheckable(False)
        self.firmwareUpdateBackButton.setAutoDefault(False)
        self.firmwareUpdateBackButton.setDefault(False)
        self.firmwareUpdateBackButton.setFlat(False)
        self.firmwareUpdateBackButton.setObjectName("firmwareUpdateBackButton")
        self.stackedWidget.addWidget(self.firmwareUpdateProgressPage)
        self.calibratePage = QtWidgets.QWidget()
        self.calibratePage.setObjectName("calibratePage")
        self.calibrateLabel = QtWidgets.QLabel(self.calibratePage)
        self.calibrateLabel.setGeometry(QtCore.QRect(20, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel.setFont(font)
        self.calibrateLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.calibrateLabel.setObjectName("calibrateLabel")
        self.calibrateBackButton = QtWidgets.QPushButton(self.calibratePage)
        self.calibrateBackButton.setGeometry(QtCore.QRect(320, 210, 161, 111))
        self.calibrateBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.calibrateBackButton.setFont(font)
        self.calibrateBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.calibrateBackButton.setText("")
        self.calibrateBackButton.setIcon(icon6)
        self.calibrateBackButton.setIconSize(QtCore.QSize(50, 50))
        self.calibrateBackButton.setCheckable(False)
        self.calibrateBackButton.setAutoDefault(False)
        self.calibrateBackButton.setDefault(False)
        self.calibrateBackButton.setFlat(False)
        self.calibrateBackButton.setObjectName("calibrateBackButton")
        self.nozzleOffsetButton = QtWidgets.QToolButton(self.calibratePage)
        self.nozzleOffsetButton.setGeometry(QtCore.QRect(160, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(17)
        self.nozzleOffsetButton.setFont(font)
        self.nozzleOffsetButton.setStyleSheet("QToolButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("templates/img/Nozzle Offset Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nozzleOffsetButton.setIcon(icon12)
        self.nozzleOffsetButton.setIconSize(QtCore.QSize(70, 70))
        self.nozzleOffsetButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.nozzleOffsetButton.setObjectName("nozzleOffsetButton")
        self.calibrationWizardButton = QtWidgets.QToolButton(self.calibratePage)
        self.calibrationWizardButton.setGeometry(QtCore.QRect(0, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.calibrationWizardButton.setFont(font)
        self.calibrationWizardButton.setStyleSheet("QToolButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton:focus {\n"
"    outline: none;\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("templates/img/magic-wand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calibrationWizardButton.setIcon(icon13)
        self.calibrationWizardButton.setIconSize(QtCore.QSize(60, 60))
        self.calibrationWizardButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.calibrationWizardButton.setObjectName("calibrationWizardButton")
        self.stackedWidget.addWidget(self.calibratePage)
        self.calibrationWizardPage = QtWidgets.QWidget()
        self.calibrationWizardPage.setObjectName("calibrationWizardPage")
        self.quickCalibrationButton = QtWidgets.QPushButton(self.calibrationWizardPage)
        self.quickCalibrationButton.setGeometry(QtCore.QRect(0, 180, 481, 71))
        self.quickCalibrationButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        self.quickCalibrationButton.setFont(font)
        self.quickCalibrationButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("templates/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quickCalibrationButton.setIcon(icon14)
        self.quickCalibrationButton.setIconSize(QtCore.QSize(15, 15))
        self.quickCalibrationButton.setCheckable(False)
        self.quickCalibrationButton.setAutoDefault(False)
        self.quickCalibrationButton.setDefault(False)
        self.quickCalibrationButton.setFlat(False)
        self.quickCalibrationButton.setObjectName("quickCalibrationButton")
        self.calibrationWizardLabel = QtWidgets.QLabel(self.calibrationWizardPage)
        self.calibrationWizardLabel.setGeometry(QtCore.QRect(10, 10, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.calibrationWizardLabel.setFont(font)
        self.calibrationWizardLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.calibrationWizardLabel.setObjectName("calibrationWizardLabel")
        self.calibrationWizardBackButton = QtWidgets.QPushButton(self.calibrationWizardPage)
        self.calibrationWizardBackButton.setGeometry(QtCore.QRect(0, 250, 481, 71))
        self.calibrationWizardBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.calibrationWizardBackButton.setFont(font)
        self.calibrationWizardBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.calibrationWizardBackButton.setText("")
        self.calibrationWizardBackButton.setIcon(icon6)
        self.calibrationWizardBackButton.setIconSize(QtCore.QSize(50, 50))
        self.calibrationWizardBackButton.setCheckable(False)
        self.calibrationWizardBackButton.setAutoDefault(False)
        self.calibrationWizardBackButton.setDefault(False)
        self.calibrationWizardBackButton.setFlat(False)
        self.calibrationWizardBackButton.setObjectName("calibrationWizardBackButton")
        self.stackedWidget.addWidget(self.calibrationWizardPage)
        self.quickStep1Page = QtWidgets.QWidget()
        self.quickStep1Page.setObjectName("quickStep1Page")
        self.calibrateLabel_6 = QtWidgets.QLabel(self.quickStep1Page)
        self.calibrateLabel_6.setGeometry(QtCore.QRect(10, 20, 461, 181))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_6.setFont(font)
        self.calibrateLabel_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.calibrateLabel_6.setWordWrap(True)
        self.calibrateLabel_6.setObjectName("calibrateLabel_6")
        self.quickStep1NextButton = QtWidgets.QPushButton(self.quickStep1Page)
        self.quickStep1NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep1NextButton.setFont(font)
        self.quickStep1NextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep1NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep1NextButton.setObjectName("quickStep1NextButton")
        self.quickStep1CancelButton = QtWidgets.QPushButton(self.quickStep1Page)
        self.quickStep1CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep1CancelButton.setFont(font)
        self.quickStep1CancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep1CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep1CancelButton.setObjectName("quickStep1CancelButton")
        self.printPreviewSelected_3 = QtWidgets.QLabel(self.quickStep1Page)
        self.printPreviewSelected_3.setGeometry(QtCore.QRect(160, 110, 150, 150))
        self.printPreviewSelected_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.printPreviewSelected_3.setText("")
        self.printPreviewSelected_3.setScaledContents(True)
        self.printPreviewSelected_3.setObjectName("printPreviewSelected_3")
        self.stackedWidget.addWidget(self.quickStep1Page)
        self.quickStep2Page = QtWidgets.QWidget()
        self.quickStep2Page.setObjectName("quickStep2Page")
        self.calibrateLabel_7 = QtWidgets.QLabel(self.quickStep2Page)
        self.calibrateLabel_7.setGeometry(QtCore.QRect(10, 20, 471, 131))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_7.setFont(font)
        self.calibrateLabel_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.calibrateLabel_7.setWordWrap(True)
        self.calibrateLabel_7.setObjectName("calibrateLabel_7")
        self.quickStep2NextButton = QtWidgets.QPushButton(self.quickStep2Page)
        self.quickStep2NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep2NextButton.setFont(font)
        self.quickStep2NextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep2NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep2NextButton.setObjectName("quickStep2NextButton")
        self.quickStep2CancelButton = QtWidgets.QPushButton(self.quickStep2Page)
        self.quickStep2CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep2CancelButton.setFont(font)
        self.quickStep2CancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep2CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep2CancelButton.setObjectName("quickStep2CancelButton")
        self.stackedWidget.addWidget(self.quickStep2Page)
        self.quickStep3Page = QtWidgets.QWidget()
        self.quickStep3Page.setObjectName("quickStep3Page")
        self.quickStep3CancelButton = QtWidgets.QPushButton(self.quickStep3Page)
        self.quickStep3CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep3CancelButton.setFont(font)
        self.quickStep3CancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep3CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep3CancelButton.setObjectName("quickStep3CancelButton")
        self.quickStep3NextButton = QtWidgets.QPushButton(self.quickStep3Page)
        self.quickStep3NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep3NextButton.setFont(font)
        self.quickStep3NextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep3NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep3NextButton.setObjectName("quickStep3NextButton")
        self.calibrateLabel_10 = QtWidgets.QLabel(self.quickStep3Page)
        self.calibrateLabel_10.setGeometry(QtCore.QRect(10, 20, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_10.setFont(font)
        self.calibrateLabel_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.calibrateLabel_10.setWordWrap(True)
        self.calibrateLabel_10.setObjectName("calibrateLabel_10")
        self.stackedWidget.addWidget(self.quickStep3Page)
        self.quickStep4Page = QtWidgets.QWidget()
        self.quickStep4Page.setObjectName("quickStep4Page")
        self.quickStep4CancelButton = QtWidgets.QPushButton(self.quickStep4Page)
        self.quickStep4CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep4CancelButton.setFont(font)
        self.quickStep4CancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep4CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep4CancelButton.setObjectName("quickStep4CancelButton")
        self.quickStep4NextButton = QtWidgets.QPushButton(self.quickStep4Page)
        self.quickStep4NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep4NextButton.setFont(font)
        self.quickStep4NextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep4NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep4NextButton.setObjectName("quickStep4NextButton")
        self.calibrateLabel_12 = QtWidgets.QLabel(self.quickStep4Page)
        self.calibrateLabel_12.setGeometry(QtCore.QRect(10, 20, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_12.setFont(font)
        self.calibrateLabel_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.calibrateLabel_12.setWordWrap(True)
        self.calibrateLabel_12.setObjectName("calibrateLabel_12")
        self.stackedWidget.addWidget(self.quickStep4Page)
        self.quickStep5Page = QtWidgets.QWidget()
        self.quickStep5Page.setObjectName("quickStep5Page")
        self.calibrateLabel_25 = QtWidgets.QLabel(self.quickStep5Page)
        self.calibrateLabel_25.setGeometry(QtCore.QRect(0, 20, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calibrateLabel_25.setFont(font)
        self.calibrateLabel_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.calibrateLabel_25.setWordWrap(True)
        self.calibrateLabel_25.setObjectName("calibrateLabel_25")
        self.quickStep5NextButton = QtWidgets.QPushButton(self.quickStep5Page)
        self.quickStep5NextButton.setGeometry(QtCore.QRect(0, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep5NextButton.setFont(font)
        self.quickStep5NextButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep5NextButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep5NextButton.setObjectName("quickStep5NextButton")
        self.quickStep5CancelButton = QtWidgets.QPushButton(self.quickStep5Page)
        self.quickStep5CancelButton.setGeometry(QtCore.QRect(240, 260, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.quickStep5CancelButton.setFont(font)
        self.quickStep5CancelButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.quickStep5CancelButton.setIconSize(QtCore.QSize(40, 40))
        self.quickStep5CancelButton.setObjectName("quickStep5CancelButton")
        self.stackedWidget.addWidget(self.quickStep5Page)
        self.nozzleOffsetPage = QtWidgets.QWidget()
        self.nozzleOffsetPage.setObjectName("nozzleOffsetPage")
        self.nozzleOffsetDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.nozzleOffsetPage)
        self.nozzleOffsetDoubleSpinBox.setGeometry(QtCore.QRect(60, 90, 321, 136))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        self.nozzleOffsetDoubleSpinBox.setFont(font)
        self.nozzleOffsetDoubleSpinBox.setStyleSheet("QDoubleSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QDoubleSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow { \n"
"image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow { \n"
"image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
"")
        self.nozzleOffsetDoubleSpinBox.setReadOnly(False)
        self.nozzleOffsetDoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.nozzleOffsetDoubleSpinBox.setAccelerated(True)
        self.nozzleOffsetDoubleSpinBox.setDecimals(2)
        self.nozzleOffsetDoubleSpinBox.setMinimum(-2.0)
        self.nozzleOffsetDoubleSpinBox.setMaximum(2.0)
        self.nozzleOffsetDoubleSpinBox.setSingleStep(0.05)
        self.nozzleOffsetDoubleSpinBox.setObjectName("nozzleOffsetDoubleSpinBox")
        self.nozzleOffsetSetButton = QtWidgets.QPushButton(self.nozzleOffsetPage)
        self.nozzleOffsetSetButton.setGeometry(QtCore.QRect(378, 92, 91, 132))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.nozzleOffsetSetButton.setFont(font)
        self.nozzleOffsetSetButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.nozzleOffsetSetButton.setText("")
        self.nozzleOffsetSetButton.setIcon(icon1)
        self.nozzleOffsetSetButton.setIconSize(QtCore.QSize(50, 50))
        self.nozzleOffsetSetButton.setObjectName("nozzleOffsetSetButton")
        self.feedRateLabelControlPage_3 = QtWidgets.QLabel(self.nozzleOffsetPage)
        self.feedRateLabelControlPage_3.setGeometry(QtCore.QRect(10, 0, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedRateLabelControlPage_3.setFont(font)
        self.feedRateLabelControlPage_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.feedRateLabelControlPage_3.setWordWrap(True)
        self.feedRateLabelControlPage_3.setObjectName("feedRateLabelControlPage_3")
        self.nozzleOffsetBackButton = QtWidgets.QPushButton(self.nozzleOffsetPage)
        self.nozzleOffsetBackButton.setGeometry(QtCore.QRect(0, 260, 480, 60))
        self.nozzleOffsetBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.nozzleOffsetBackButton.setFont(font)
        self.nozzleOffsetBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.nozzleOffsetBackButton.setText("")
        self.nozzleOffsetBackButton.setIcon(icon6)
        self.nozzleOffsetBackButton.setIconSize(QtCore.QSize(50, 50))
        self.nozzleOffsetBackButton.setCheckable(False)
        self.nozzleOffsetBackButton.setAutoDefault(False)
        self.nozzleOffsetBackButton.setDefault(False)
        self.nozzleOffsetBackButton.setFlat(False)
        self.nozzleOffsetBackButton.setObjectName("nozzleOffsetBackButton")
        self.printPreviewSelected_2 = QtWidgets.QLabel(self.nozzleOffsetPage)
        self.printPreviewSelected_2.setGeometry(QtCore.QRect(150, 90, 161, 161))
        self.printPreviewSelected_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.printPreviewSelected_2.setText("")
        self.printPreviewSelected_2.setPixmap(QtGui.QPixmap("templates/img/Nozzle Offset.png"))
        self.printPreviewSelected_2.setScaledContents(True)
        self.printPreviewSelected_2.setObjectName("printPreviewSelected_2")
        self.feedRateLabelControlPage_3.raise_()
        self.nozzleOffsetDoubleSpinBox.raise_()
        self.nozzleOffsetSetButton.raise_()
        self.nozzleOffsetBackButton.raise_()
        self.printPreviewSelected_2.raise_()
        self.stackedWidget.addWidget(self.nozzleOffsetPage)
        self.printLocationPage = QtWidgets.QWidget()
        self.printLocationPage.setObjectName("printLocationPage")
        self.fromUsbButton = QtWidgets.QPushButton(self.printLocationPage)
        self.fromUsbButton.setGeometry(QtCore.QRect(160, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.fromUsbButton.setFont(font)
        self.fromUsbButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("templates/img/usb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromUsbButton.setIcon(icon15)
        self.fromUsbButton.setIconSize(QtCore.QSize(40, 40))
        self.fromUsbButton.setObjectName("fromUsbButton")
        self.printFromLabel = QtWidgets.QLabel(self.printLocationPage)
        self.printFromLabel.setGeometry(QtCore.QRect(10, 80, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.printFromLabel.setFont(font)
        self.printFromLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.printFromLabel.setObjectName("printFromLabel")
        self.printLocationScreenBackButton = QtWidgets.QPushButton(self.printLocationPage)
        self.printLocationScreenBackButton.setGeometry(QtCore.QRect(320, 210, 161, 111))
        self.printLocationScreenBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.printLocationScreenBackButton.setFont(font)
        self.printLocationScreenBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.printLocationScreenBackButton.setText("")
        self.printLocationScreenBackButton.setIcon(icon6)
        self.printLocationScreenBackButton.setIconSize(QtCore.QSize(50, 50))
        self.printLocationScreenBackButton.setCheckable(False)
        self.printLocationScreenBackButton.setAutoDefault(False)
        self.printLocationScreenBackButton.setDefault(False)
        self.printLocationScreenBackButton.setFlat(False)
        self.printLocationScreenBackButton.setObjectName("printLocationScreenBackButton")
        self.fromLocalButton = QtWidgets.QPushButton(self.printLocationPage)
        self.fromLocalButton.setGeometry(QtCore.QRect(0, 210, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.fromLocalButton.setFont(font)
        self.fromLocalButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("templates/img/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fromLocalButton.setIcon(icon16)
        self.fromLocalButton.setIconSize(QtCore.QSize(40, 40))
        self.fromLocalButton.setObjectName("fromLocalButton")
        self.stackedWidget.addWidget(self.printLocationPage)
        self.fileListLocalPage = QtWidgets.QWidget()
        self.fileListLocalPage.setObjectName("fileListLocalPage")
        self.fileListWidget = QtWidgets.QListWidget(self.fileListLocalPage)
        self.fileListWidget.setGeometry(QtCore.QRect(0, 0, 321, 321))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(17)
        self.fileListWidget.setFont(font)
        self.fileListWidget.setStyleSheet("\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width\n"
" of the view */\n"
"    background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    color: black;\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border:  rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"     border: 1px solid rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     border: 1px solid  rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.fileListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fileListWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fileListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidget.setAutoScrollMargin(4)
        self.fileListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.fileListWidget.setObjectName("fileListWidget")
        self.localStorageBackButton = QtWidgets.QPushButton(self.fileListLocalPage)
        self.localStorageBackButton.setGeometry(QtCore.QRect(390, 210, 91, 111))
        self.localStorageBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.localStorageBackButton.setFont(font)
        self.localStorageBackButton.setStyleSheet("QPushButton {\n"
"        border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.localStorageBackButton.setText("")
        self.localStorageBackButton.setIcon(icon6)
        self.localStorageBackButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageBackButton.setCheckable(False)
        self.localStorageBackButton.setAutoDefault(False)
        self.localStorageBackButton.setDefault(False)
        self.localStorageBackButton.setFlat(False)
        self.localStorageBackButton.setObjectName("localStorageBackButton")
        self.localStorageSelectButton = QtWidgets.QPushButton(self.fileListLocalPage)
        self.localStorageSelectButton.setGeometry(QtCore.QRect(390, 0, 91, 111))
        self.localStorageSelectButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.localStorageSelectButton.setFont(font)
        self.localStorageSelectButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.localStorageSelectButton.setText("")
        self.localStorageSelectButton.setIcon(icon1)
        self.localStorageSelectButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageSelectButton.setCheckable(False)
        self.localStorageSelectButton.setAutoDefault(False)
        self.localStorageSelectButton.setDefault(False)
        self.localStorageSelectButton.setFlat(False)
        self.localStorageSelectButton.setObjectName("localStorageSelectButton")
        self.localStorageScrollDown = QtWidgets.QPushButton(self.fileListLocalPage)
        self.localStorageScrollDown.setGeometry(QtCore.QRect(310, 160, 81, 161))
        self.localStorageScrollDown.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.localStorageScrollDown.setFont(font)
        self.localStorageScrollDown.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.localStorageScrollDown.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("templates/img/arrows-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.localStorageScrollDown.setIcon(icon17)
        self.localStorageScrollDown.setIconSize(QtCore.QSize(40, 40))
        self.localStorageScrollDown.setCheckable(False)
        self.localStorageScrollDown.setAutoRepeat(True)
        self.localStorageScrollDown.setAutoExclusive(False)
        self.localStorageScrollDown.setAutoDefault(False)
        self.localStorageScrollDown.setDefault(False)
        self.localStorageScrollDown.setFlat(False)
        self.localStorageScrollDown.setObjectName("localStorageScrollDown")
        self.localStorageScrollUp = QtWidgets.QPushButton(self.fileListLocalPage)
        self.localStorageScrollUp.setGeometry(QtCore.QRect(310, 0, 81, 161))
        self.localStorageScrollUp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.localStorageScrollUp.setFont(font)
        self.localStorageScrollUp.setStyleSheet("QPushButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.localStorageScrollUp.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("templates/img/arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.localStorageScrollUp.setIcon(icon18)
        self.localStorageScrollUp.setIconSize(QtCore.QSize(40, 40))
        self.localStorageScrollUp.setCheckable(False)
        self.localStorageScrollUp.setAutoRepeat(True)
        self.localStorageScrollUp.setAutoExclusive(False)
        self.localStorageScrollUp.setAutoDefault(False)
        self.localStorageScrollUp.setDefault(False)
        self.localStorageScrollUp.setFlat(False)
        self.localStorageScrollUp.setObjectName("localStorageScrollUp")
        self.localStorageDeleteButton = QtWidgets.QPushButton(self.fileListLocalPage)
        self.localStorageDeleteButton.setGeometry(QtCore.QRect(390, 110, 91, 101))
        self.localStorageDeleteButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.localStorageDeleteButton.setFont(font)
        self.localStorageDeleteButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.localStorageDeleteButton.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("templates/img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.localStorageDeleteButton.setIcon(icon19)
        self.localStorageDeleteButton.setIconSize(QtCore.QSize(50, 50))
        self.localStorageDeleteButton.setCheckable(False)
        self.localStorageDeleteButton.setAutoDefault(False)
        self.localStorageDeleteButton.setDefault(False)
        self.localStorageDeleteButton.setFlat(False)
        self.localStorageDeleteButton.setObjectName("localStorageDeleteButton")
        self.stackedWidget.addWidget(self.fileListLocalPage)
        self.fileListUSBPage = QtWidgets.QWidget()
        self.fileListUSBPage.setObjectName("fileListUSBPage")
        self.USBStorageSaveButton = QtWidgets.QPushButton(self.fileListUSBPage)
        self.USBStorageSaveButton.setGeometry(QtCore.QRect(390, 110, 91, 101))
        self.USBStorageSaveButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.USBStorageSaveButton.setFont(font)
        self.USBStorageSaveButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.USBStorageSaveButton.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("templates/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.USBStorageSaveButton.setIcon(icon20)
        self.USBStorageSaveButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageSaveButton.setCheckable(False)
        self.USBStorageSaveButton.setAutoDefault(False)
        self.USBStorageSaveButton.setDefault(False)
        self.USBStorageSaveButton.setFlat(False)
        self.USBStorageSaveButton.setObjectName("USBStorageSaveButton")
        self.USBStorageScrollUp = QtWidgets.QPushButton(self.fileListUSBPage)
        self.USBStorageScrollUp.setGeometry(QtCore.QRect(310, 0, 81, 161))
        self.USBStorageScrollUp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.USBStorageScrollUp.setFont(font)
        self.USBStorageScrollUp.setStyleSheet("QPushButton {\n"
"\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.USBStorageScrollUp.setText("")
        self.USBStorageScrollUp.setIcon(icon18)
        self.USBStorageScrollUp.setIconSize(QtCore.QSize(40, 40))
        self.USBStorageScrollUp.setCheckable(False)
        self.USBStorageScrollUp.setAutoRepeat(True)
        self.USBStorageScrollUp.setAutoExclusive(False)
        self.USBStorageScrollUp.setAutoDefault(False)
        self.USBStorageScrollUp.setDefault(False)
        self.USBStorageScrollUp.setFlat(False)
        self.USBStorageScrollUp.setObjectName("USBStorageScrollUp")
        self.USBStorageSelectButton = QtWidgets.QPushButton(self.fileListUSBPage)
        self.USBStorageSelectButton.setGeometry(QtCore.QRect(390, 0, 91, 111))
        self.USBStorageSelectButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.USBStorageSelectButton.setFont(font)
        self.USBStorageSelectButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.USBStorageSelectButton.setText("")
        self.USBStorageSelectButton.setIcon(icon1)
        self.USBStorageSelectButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageSelectButton.setCheckable(False)
        self.USBStorageSelectButton.setAutoDefault(False)
        self.USBStorageSelectButton.setDefault(False)
        self.USBStorageSelectButton.setFlat(False)
        self.USBStorageSelectButton.setObjectName("USBStorageSelectButton")
        self.USBStorageBackButton = QtWidgets.QPushButton(self.fileListUSBPage)
        self.USBStorageBackButton.setGeometry(QtCore.QRect(390, 210, 91, 111))
        self.USBStorageBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.USBStorageBackButton.setFont(font)
        self.USBStorageBackButton.setStyleSheet("QPushButton {\n"
"        border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.USBStorageBackButton.setText("")
        self.USBStorageBackButton.setIcon(icon6)
        self.USBStorageBackButton.setIconSize(QtCore.QSize(50, 50))
        self.USBStorageBackButton.setCheckable(False)
        self.USBStorageBackButton.setAutoDefault(False)
        self.USBStorageBackButton.setDefault(False)
        self.USBStorageBackButton.setFlat(False)
        self.USBStorageBackButton.setObjectName("USBStorageBackButton")
        self.USBStorageScrollDown = QtWidgets.QPushButton(self.fileListUSBPage)
        self.USBStorageScrollDown.setGeometry(QtCore.QRect(310, 160, 81, 161))
        self.USBStorageScrollDown.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.USBStorageScrollDown.setFont(font)
        self.USBStorageScrollDown.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.USBStorageScrollDown.setText("")
        self.USBStorageScrollDown.setIcon(icon17)
        self.USBStorageScrollDown.setIconSize(QtCore.QSize(40, 40))
        self.USBStorageScrollDown.setCheckable(False)
        self.USBStorageScrollDown.setAutoRepeat(True)
        self.USBStorageScrollDown.setAutoExclusive(False)
        self.USBStorageScrollDown.setAutoDefault(False)
        self.USBStorageScrollDown.setDefault(False)
        self.USBStorageScrollDown.setFlat(False)
        self.USBStorageScrollDown.setObjectName("USBStorageScrollDown")
        self.fileListWidgetUSB = QtWidgets.QListWidget(self.fileListUSBPage)
        self.fileListWidgetUSB.setGeometry(QtCore.QRect(0, 0, 311, 321))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(17)
        self.fileListWidgetUSB.setFont(font)
        self.fileListWidgetUSB.setStyleSheet("\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width\n"
" of the view */\n"
"    background-color: rgb(255, 255, 255);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:!selected {\n"
"    color: black;\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border:  rgb(182, 182, 182);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"     border: 1px solid rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"     border: 1px solid  rgb(182, 182, 182);\n"
"    background-color: rgb(40,40,40);\n"
"outline: none;\n"
"}\n"
"\n"
"QListView::item:selected:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.fileListWidgetUSB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fileListWidgetUSB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fileListWidgetUSB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidgetUSB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileListWidgetUSB.setAutoScrollMargin(4)
        self.fileListWidgetUSB.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.fileListWidgetUSB.setObjectName("fileListWidgetUSB")
        self.USBStorageSaveButton.raise_()
        self.USBStorageSelectButton.raise_()
        self.USBStorageBackButton.raise_()
        self.fileListWidgetUSB.raise_()
        self.USBStorageScrollDown.raise_()
        self.USBStorageScrollUp.raise_()
        self.stackedWidget.addWidget(self.fileListUSBPage)
        self.printSelectedLocalPage = QtWidgets.QWidget()
        self.printSelectedLocalPage.setObjectName("printSelectedLocalPage")
        self.fileSelected = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.fileSelected.setGeometry(QtCore.QRect(10, 0, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.fileSelected.setFont(font)
        self.fileSelected.setStyleSheet("color:  white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fileSelected.setScaledContents(True)
        self.fileSelected.setWordWrap(True)
        self.fileSelected.setObjectName("fileSelected")
        self.fileSelectedBackButton = QtWidgets.QPushButton(self.printSelectedLocalPage)
        self.fileSelectedBackButton.setGeometry(QtCore.QRect(240, 230, 241, 91))
        self.fileSelectedBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.fileSelectedBackButton.setFont(font)
        self.fileSelectedBackButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.fileSelectedBackButton.setText("")
        self.fileSelectedBackButton.setIcon(icon6)
        self.fileSelectedBackButton.setIconSize(QtCore.QSize(50, 50))
        self.fileSelectedBackButton.setCheckable(False)
        self.fileSelectedBackButton.setAutoDefault(False)
        self.fileSelectedBackButton.setDefault(False)
        self.fileSelectedBackButton.setFlat(False)
        self.fileSelectedBackButton.setObjectName("fileSelectedBackButton")
        self.fileSelectedPrintButton = QtWidgets.QToolButton(self.printSelectedLocalPage)
        self.fileSelectedPrintButton.setGeometry(QtCore.QRect(0, 230, 241, 91))
        self.fileSelectedPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        self.fileSelectedPrintButton.setFont(font)
        self.fileSelectedPrintButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.fileSelectedPrintButton.setIcon(icon7)
        self.fileSelectedPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedPrintButton.setCheckable(False)
        self.fileSelectedPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedPrintButton.setObjectName("fileSelectedPrintButton")
        self.fileSizeSelected = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.fileSizeSelected.setGeometry(QtCore.QRect(60, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fileSizeSelected.setFont(font)
        self.fileSizeSelected.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fileSizeSelected.setScaledContents(True)
        self.fileSizeSelected.setObjectName("fileSizeSelected")
        self.fileDateSelected = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.fileDateSelected.setGeometry(QtCore.QRect(70, 90, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fileDateSelected.setFont(font)
        self.fileDateSelected.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fileDateSelected.setScaledContents(True)
        self.fileDateSelected.setObjectName("fileDateSelected")
        self.filePrintTimeSelected = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.filePrintTimeSelected.setGeometry(QtCore.QRect(130, 137, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filePrintTimeSelected.setFont(font)
        self.filePrintTimeSelected.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.filePrintTimeSelected.setScaledContents(True)
        self.filePrintTimeSelected.setObjectName("filePrintTimeSelected")
        self.filamentVolumeSelected = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.filamentVolumeSelected.setGeometry(QtCore.QRect(110, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filamentVolumeSelected.setFont(font)
        self.filamentVolumeSelected.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.filamentVolumeSelected.setScaledContents(True)
        self.filamentVolumeSelected.setObjectName("filamentVolumeSelected")
        self.fileSizeSelectedLabel = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.fileSizeSelectedLabel.setGeometry(QtCore.QRect(10, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fileSizeSelectedLabel.setFont(font)
        self.fileSizeSelectedLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.fileSizeSelectedLabel.setObjectName("fileSizeSelectedLabel")
        self.fileDateSelectedLabel = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.fileDateSelectedLabel.setGeometry(QtCore.QRect(10, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fileDateSelectedLabel.setFont(font)
        self.fileDateSelectedLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.fileDateSelectedLabel.setObjectName("fileDateSelectedLabel")
        self.filePrintTimeSelectedLabel = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.filePrintTimeSelectedLabel.setGeometry(QtCore.QRect(10, 110, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filePrintTimeSelectedLabel.setFont(font)
        self.filePrintTimeSelectedLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.filePrintTimeSelectedLabel.setWordWrap(True)
        self.filePrintTimeSelectedLabel.setObjectName("filePrintTimeSelectedLabel")
        self.filamentVolumeSelectedLabel = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.filamentVolumeSelectedLabel.setGeometry(QtCore.QRect(10, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filamentVolumeSelectedLabel.setFont(font)
        self.filamentVolumeSelectedLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.filamentVolumeSelectedLabel.setObjectName("filamentVolumeSelectedLabel")
        self.filamentLengthFileSelected = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.filamentLengthFileSelected.setGeometry(QtCore.QRect(110, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filamentLengthFileSelected.setFont(font)
        self.filamentLengthFileSelected.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.filamentLengthFileSelected.setScaledContents(True)
        self.filamentLengthFileSelected.setObjectName("filamentLengthFileSelected")
        self.filamentLengthSelectedLabel = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.filamentLengthSelectedLabel.setGeometry(QtCore.QRect(10, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filamentLengthSelectedLabel.setFont(font)
        self.filamentLengthSelectedLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.filamentLengthSelectedLabel.setObjectName("filamentLengthSelectedLabel")
        self.printPreviewSelected = QtWidgets.QLabel(self.printSelectedLocalPage)
        self.printPreviewSelected.setGeometry(QtCore.QRect(260, 20, 210, 210))
        self.printPreviewSelected.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.printPreviewSelected.setText("")
        self.printPreviewSelected.setPixmap(QtGui.QPixmap("templates/img/thumbnail.png"))
        self.printPreviewSelected.setScaledContents(True)
        self.printPreviewSelected.setObjectName("printPreviewSelected")
        self.printPreviewSelected.raise_()
        self.fileSelected.raise_()
        self.fileSelectedBackButton.raise_()
        self.fileSelectedPrintButton.raise_()
        self.fileSizeSelected.raise_()
        self.fileDateSelected.raise_()
        self.filePrintTimeSelected.raise_()
        self.filamentVolumeSelected.raise_()
        self.fileSizeSelectedLabel.raise_()
        self.fileDateSelectedLabel.raise_()
        self.filePrintTimeSelectedLabel.raise_()
        self.filamentVolumeSelectedLabel.raise_()
        self.filamentLengthFileSelected.raise_()
        self.filamentLengthSelectedLabel.raise_()
        self.stackedWidget.addWidget(self.printSelectedLocalPage)
        self.printSelectedUSBPage = QtWidgets.QWidget()
        self.printSelectedUSBPage.setObjectName("printSelectedUSBPage")
        self.fileSelectedUSBTransferButton = QtWidgets.QToolButton(self.printSelectedUSBPage)
        self.fileSelectedUSBTransferButton.setGeometry(QtCore.QRect(0, 230, 161, 91))
        self.fileSelectedUSBTransferButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        self.fileSelectedUSBTransferButton.setFont(font)
        self.fileSelectedUSBTransferButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.fileSelectedUSBTransferButton.setIcon(icon20)
        self.fileSelectedUSBTransferButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedUSBTransferButton.setCheckable(False)
        self.fileSelectedUSBTransferButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedUSBTransferButton.setObjectName("fileSelectedUSBTransferButton")
        self.printPreviewSelectedUSB = QtWidgets.QLabel(self.printSelectedUSBPage)
        self.printPreviewSelectedUSB.setGeometry(QtCore.QRect(130, 20, 210, 210))
        self.printPreviewSelectedUSB.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.printPreviewSelectedUSB.setText("")
        self.printPreviewSelectedUSB.setPixmap(QtGui.QPixmap("templates/img/thumbnail.png"))
        self.printPreviewSelectedUSB.setScaledContents(True)
        self.printPreviewSelectedUSB.setObjectName("printPreviewSelectedUSB")
        self.fileSelectedUSBBackButton = QtWidgets.QPushButton(self.printSelectedUSBPage)
        self.fileSelectedUSBBackButton.setGeometry(QtCore.QRect(320, 230, 161, 91))
        self.fileSelectedUSBBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.fileSelectedUSBBackButton.setFont(font)
        self.fileSelectedUSBBackButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.fileSelectedUSBBackButton.setText("")
        self.fileSelectedUSBBackButton.setIcon(icon6)
        self.fileSelectedUSBBackButton.setIconSize(QtCore.QSize(50, 50))
        self.fileSelectedUSBBackButton.setCheckable(False)
        self.fileSelectedUSBBackButton.setAutoDefault(False)
        self.fileSelectedUSBBackButton.setDefault(False)
        self.fileSelectedUSBBackButton.setFlat(False)
        self.fileSelectedUSBBackButton.setObjectName("fileSelectedUSBBackButton")
        self.fileSelectedUSBName = QtWidgets.QLabel(self.printSelectedUSBPage)
        self.fileSelectedUSBName.setGeometry(QtCore.QRect(0, 0, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fileSelectedUSBName.setFont(font)
        self.fileSelectedUSBName.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fileSelectedUSBName.setObjectName("fileSelectedUSBName")
        self.fileSelectedUSBPrintButton = QtWidgets.QToolButton(self.printSelectedUSBPage)
        self.fileSelectedUSBPrintButton.setGeometry(QtCore.QRect(160, 230, 161, 91))
        self.fileSelectedUSBPrintButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        self.fileSelectedUSBPrintButton.setFont(font)
        self.fileSelectedUSBPrintButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.fileSelectedUSBPrintButton.setIcon(icon7)
        self.fileSelectedUSBPrintButton.setIconSize(QtCore.QSize(40, 40))
        self.fileSelectedUSBPrintButton.setCheckable(False)
        self.fileSelectedUSBPrintButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.fileSelectedUSBPrintButton.setObjectName("fileSelectedUSBPrintButton")
        self.printPreviewSelectedUSB.raise_()
        self.fileSelectedUSBTransferButton.raise_()
        self.fileSelectedUSBBackButton.raise_()
        self.fileSelectedUSBName.raise_()
        self.fileSelectedUSBPrintButton.raise_()
        self.stackedWidget.addWidget(self.printSelectedUSBPage)
        self.controlPage = QtWidgets.QWidget()
        self.controlPage.setObjectName("controlPage")
        self.controlTabWidget = QtWidgets.QTabWidget(self.controlPage)
        self.controlTabWidget.setGeometry(QtCore.QRect(0, 0, 491, 321))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(12)
        self.controlTabWidget.setFont(font)
        self.controlTabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.controlTabWidget.setAutoFillBackground(False)
        self.controlTabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    position: absolute;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"   border-right: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    width: 69px;\n"
"     height: 50px;\n"
"    padding-left: 25px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"/*    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"*/\n"
"background-color: rgb(40, 40, 40);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:first {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"/*border-bottom-left-radius: 15px;*/\n"
"}\n"
"QTabBar::tab:last {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"QTabBar::tab:focus {\n"
"    outline: none;\n"
"}\n"
"QTabBar:focus {\n"
"    outline: none;\n"
"}")
        self.controlTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.controlTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.controlTabWidget.setIconSize(QtCore.QSize(45, 45))
        self.controlTabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.controlTabWidget.setUsesScrollButtons(False)
        self.controlTabWidget.setTabsClosable(False)
        self.controlTabWidget.setObjectName("controlTabWidget")
        self.feedRateTab = QtWidgets.QWidget()
        self.feedRateTab.setObjectName("feedRateTab")
        self.feedRateLabelControlPage = QtWidgets.QLabel(self.feedRateTab)
        self.feedRateLabelControlPage.setGeometry(QtCore.QRect(0, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.feedRateLabelControlPage.setFont(font)
        self.feedRateLabelControlPage.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.feedRateLabelControlPage.setObjectName("feedRateLabelControlPage")
        self.moveZMBabyStep = QtWidgets.QPushButton(self.feedRateTab)
        self.moveZMBabyStep.setGeometry(QtCore.QRect(310, 170, 161, 91))
        self.moveZMBabyStep.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveZMBabyStep.setFont(font)
        self.moveZMBabyStep.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-right-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveZMBabyStep.setText("")
        self.moveZMBabyStep.setIcon(icon18)
        self.moveZMBabyStep.setIconSize(QtCore.QSize(40, 40))
        self.moveZMBabyStep.setCheckable(False)
        self.moveZMBabyStep.setAutoDefault(False)
        self.moveZMBabyStep.setDefault(False)
        self.moveZMBabyStep.setFlat(False)
        self.moveZMBabyStep.setObjectName("moveZMBabyStep")
        self.setFeedRateButton = QtWidgets.QPushButton(self.feedRateTab)
        self.setFeedRateButton.setGeometry(QtCore.QRect(388, 12, 91, 117))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.setFeedRateButton.setFont(font)
        self.setFeedRateButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.setFeedRateButton.setText("")
        self.setFeedRateButton.setIcon(icon1)
        self.setFeedRateButton.setIconSize(QtCore.QSize(50, 50))
        self.setFeedRateButton.setObjectName("setFeedRateButton")
        self.flowRateLabelControlPage_5 = QtWidgets.QLabel(self.feedRateTab)
        self.flowRateLabelControlPage_5.setGeometry(QtCore.QRect(0, 130, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.flowRateLabelControlPage_5.setFont(font)
        self.flowRateLabelControlPage_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.flowRateLabelControlPage_5.setObjectName("flowRateLabelControlPage_5")
        self.moveZPBabyStep = QtWidgets.QPushButton(self.feedRateTab)
        self.moveZPBabyStep.setGeometry(QtCore.QRect(150, 170, 161, 91))
        self.moveZPBabyStep.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveZPBabyStep.setFont(font)
        self.moveZPBabyStep.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveZPBabyStep.setText("")
        self.moveZPBabyStep.setIcon(icon17)
        self.moveZPBabyStep.setIconSize(QtCore.QSize(40, 40))
        self.moveZPBabyStep.setCheckable(False)
        self.moveZPBabyStep.setAutoDefault(False)
        self.moveZPBabyStep.setDefault(False)
        self.moveZPBabyStep.setFlat(False)
        self.moveZPBabyStep.setObjectName("moveZPBabyStep")
        self.feedRateSpinBox = QtWidgets.QSpinBox(self.feedRateTab)
        self.feedRateSpinBox.setGeometry(QtCore.QRect(150, 10, 241, 121))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(24)
        self.feedRateSpinBox.setFont(font)
        self.feedRateSpinBox.setStyleSheet("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(40, 40, 40);\n"
"    /* background-color: rgb(255, 146, 57); */\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 54px;\n"
"    padding: 2px;\n"
"border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 54px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
"")
        self.feedRateSpinBox.setFrame(False)
        self.feedRateSpinBox.setReadOnly(False)
        self.feedRateSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.feedRateSpinBox.setAccelerated(True)
        self.feedRateSpinBox.setMinimum(50)
        self.feedRateSpinBox.setMaximum(200)
        self.feedRateSpinBox.setSingleStep(1)
        self.feedRateSpinBox.setProperty("value", 100)
        self.feedRateSpinBox.setObjectName("feedRateSpinBox")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("templates/img/FeedRate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon21.addPixmap(QtGui.QPixmap("templates/img/FeedRate_Selected.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.feedRateTab, icon21, "")
        self.temperatureTab = QtWidgets.QWidget()
        self.temperatureTab.setObjectName("temperatureTab")
        self.toolLabel = QtWidgets.QLabel(self.temperatureTab)
        self.toolLabel.setGeometry(QtCore.QRect(0, 20, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toolLabel.setFont(font)
        self.toolLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolLabel.setObjectName("toolLabel")
        self.cooldownButton = QtWidgets.QPushButton(self.temperatureTab)
        self.cooldownButton.setGeometry(QtCore.QRect(120, 210, 101, 60))
        self.cooldownButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.cooldownButton.setFont(font)
        self.cooldownButton.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.cooldownButton.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("templates/img/snowflake.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cooldownButton.setIcon(icon22)
        self.cooldownButton.setIconSize(QtCore.QSize(40, 40))
        self.cooldownButton.setObjectName("cooldownButton")
        self.fanOffButton = QtWidgets.QPushButton(self.temperatureTab)
        self.fanOffButton.setGeometry(QtCore.QRect(300, 210, 81, 60))
        self.fanOffButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.fanOffButton.setFont(font)
        self.fanOffButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.fanOffButton.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("templates/img/fan-black-silhouette-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fanOffButton.setIcon(icon23)
        self.fanOffButton.setIconSize(QtCore.QSize(40, 40))
        self.fanOffButton.setCheckable(False)
        self.fanOffButton.setAutoDefault(False)
        self.fanOffButton.setDefault(False)
        self.fanOffButton.setFlat(False)
        self.fanOffButton.setObjectName("fanOffButton")
        self.fanOnButton = QtWidgets.QPushButton(self.temperatureTab)
        self.fanOnButton.setGeometry(QtCore.QRect(220, 210, 81, 60))
        self.fanOnButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.fanOnButton.setFont(font)
        self.fanOnButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.fanOnButton.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("templates/img/fan-black-silhouette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fanOnButton.setIcon(icon24)
        self.fanOnButton.setIconSize(QtCore.QSize(40, 40))
        self.fanOnButton.setCheckable(False)
        self.fanOnButton.setAutoDefault(False)
        self.fanOnButton.setDefault(False)
        self.fanOnButton.setFlat(False)
        self.fanOnButton.setObjectName("fanOnButton")
        self.toolTempSpinBox = QtWidgets.QSpinBox(self.temperatureTab)
        self.toolTempSpinBox.setGeometry(QtCore.QRect(0, 58, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        self.toolTempSpinBox.setFont(font)
        self.toolTempSpinBox.setStyleSheet("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    /* background-color: rgb(255, 146, 57); */\n"
"   background-color: rgb(40, 40, 40);\n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
"")
        self.toolTempSpinBox.setReadOnly(False)
        self.toolTempSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.toolTempSpinBox.setAccelerated(True)
        self.toolTempSpinBox.setMaximum(300)
        self.toolTempSpinBox.setSingleStep(1)
        self.toolTempSpinBox.setProperty("value", 0)
        self.toolTempSpinBox.setObjectName("toolTempSpinBox")
        self.setToolTempButton = QtWidgets.QPushButton(self.temperatureTab)
        self.setToolTempButton.setGeometry(QtCore.QRect(159, 60, 71, 127))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.setToolTempButton.setFont(font)
        self.setToolTempButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-right-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.setToolTempButton.setText("")
        self.setToolTempButton.setIcon(icon1)
        self.setToolTempButton.setIconSize(QtCore.QSize(50, 50))
        self.setToolTempButton.setObjectName("setToolTempButton")
        self.bedTempSpinBox = QtWidgets.QSpinBox(self.temperatureTab)
        self.bedTempSpinBox.setGeometry(QtCore.QRect(241, 58, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        self.bedTempSpinBox.setFont(font)
        self.bedTempSpinBox.setStyleSheet("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
"")
        self.bedTempSpinBox.setReadOnly(False)
        self.bedTempSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.bedTempSpinBox.setAccelerated(True)
        self.bedTempSpinBox.setMaximum(150)
        self.bedTempSpinBox.setSingleStep(1)
        self.bedTempSpinBox.setProperty("value", 0)
        self.bedTempSpinBox.setObjectName("bedTempSpinBox")
        self.bedLabel_2 = QtWidgets.QLabel(self.temperatureTab)
        self.bedLabel_2.setGeometry(QtCore.QRect(341, 18, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bedLabel_2.setFont(font)
        self.bedLabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.bedLabel_2.setObjectName("bedLabel_2")
        self.setBedTempButton = QtWidgets.QPushButton(self.temperatureTab)
        self.setBedTempButton.setGeometry(QtCore.QRect(400, 60, 71, 127))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.setBedTempButton.setFont(font)
        self.setBedTempButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.setBedTempButton.setText("")
        self.setBedTempButton.setIcon(icon1)
        self.setBedTempButton.setIconSize(QtCore.QSize(50, 50))
        self.setBedTempButton.setObjectName("setBedTempButton")
        self.toolLabel.raise_()
        self.cooldownButton.raise_()
        self.fanOffButton.raise_()
        self.fanOnButton.raise_()
        self.setToolTempButton.raise_()
        self.toolTempSpinBox.raise_()
        self.bedTempSpinBox.raise_()
        self.bedLabel_2.raise_()
        self.setBedTempButton.raise_()
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("templates/img/thermometer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon25.addPixmap(QtGui.QPixmap("templates/img/thermometer_Selected.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.temperatureTab, icon25, "")
        self.motionTab = QtWidgets.QWidget()
        self.motionTab.setObjectName("motionTab")
        self.step1Button = QtWidgets.QPushButton(self.motionTab)
        self.step1Button.setGeometry(QtCore.QRect(102, 225, 100, 45))
        self.step1Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.step1Button.setFont(font)
        self.step1Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.step1Button.setIconSize(QtCore.QSize(40, 40))
        self.step1Button.setCheckable(False)
        self.step1Button.setAutoDefault(False)
        self.step1Button.setDefault(False)
        self.step1Button.setFlat(False)
        self.step1Button.setObjectName("step1Button")
        self.step10Button = QtWidgets.QPushButton(self.motionTab)
        self.step10Button.setGeometry(QtCore.QRect(201, 225, 100, 45))
        self.step10Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.step10Button.setFont(font)
        self.step10Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.step10Button.setIconSize(QtCore.QSize(40, 40))
        self.step10Button.setCheckable(False)
        self.step10Button.setAutoDefault(False)
        self.step10Button.setDefault(False)
        self.step10Button.setFlat(False)
        self.step10Button.setObjectName("step10Button")
        self.step100Button = QtWidgets.QPushButton(self.motionTab)
        self.step100Button.setGeometry(QtCore.QRect(300, 225, 101, 45))
        self.step100Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.step100Button.setFont(font)
        self.step100Button.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border-bottom: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.step100Button.setIconSize(QtCore.QSize(40, 40))
        self.step100Button.setCheckable(True)
        self.step100Button.setChecked(False)
        self.step100Button.setAutoDefault(False)
        self.step100Button.setDefault(False)
        self.step100Button.setFlat(False)
        self.step100Button.setObjectName("step100Button")
        self.moveYPButton = QtWidgets.QPushButton(self.motionTab)
        self.moveYPButton.setGeometry(QtCore.QRect(80, 6, 70, 70))
        self.moveYPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveYPButton.setFont(font)
        self.moveYPButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveYPButton.setText("")
        self.moveYPButton.setIcon(icon18)
        self.moveYPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveYPButton.setCheckable(False)
        self.moveYPButton.setAutoDefault(False)
        self.moveYPButton.setDefault(False)
        self.moveYPButton.setFlat(False)
        self.moveYPButton.setObjectName("moveYPButton")
        self.moveYMButton = QtWidgets.QPushButton(self.motionTab)
        self.moveYMButton.setGeometry(QtCore.QRect(80, 144, 70, 70))
        self.moveYMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveYMButton.setFont(font)
        self.moveYMButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveYMButton.setText("")
        self.moveYMButton.setIcon(icon17)
        self.moveYMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveYMButton.setCheckable(False)
        self.moveYMButton.setAutoDefault(False)
        self.moveYMButton.setDefault(False)
        self.moveYMButton.setFlat(False)
        self.moveYMButton.setObjectName("moveYMButton")
        self.moveXPButton = QtWidgets.QPushButton(self.motionTab)
        self.moveXPButton.setGeometry(QtCore.QRect(149, 75, 70, 70))
        self.moveXPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveXPButton.setFont(font)
        self.moveXPButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveXPButton.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("templates/img/arrows-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveXPButton.setIcon(icon26)
        self.moveXPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveXPButton.setCheckable(False)
        self.moveXPButton.setAutoDefault(False)
        self.moveXPButton.setDefault(False)
        self.moveXPButton.setFlat(False)
        self.moveXPButton.setObjectName("moveXPButton")
        self.moveXMButton = QtWidgets.QPushButton(self.motionTab)
        self.moveXMButton.setGeometry(QtCore.QRect(11, 75, 70, 70))
        self.moveXMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveXMButton.setFont(font)
        self.moveXMButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveXMButton.setText("")
        self.moveXMButton.setIcon(icon6)
        self.moveXMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveXMButton.setCheckable(False)
        self.moveXMButton.setAutoDefault(False)
        self.moveXMButton.setDefault(False)
        self.moveXMButton.setFlat(False)
        self.moveXMButton.setObjectName("moveXMButton")
        self.homeXYButton = QtWidgets.QPushButton(self.motionTab)
        self.homeXYButton.setGeometry(QtCore.QRect(80, 75, 70, 70))
        self.homeXYButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.homeXYButton.setFont(font)
        self.homeXYButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.homeXYButton.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("templates/img/home-icon-silhouette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeXYButton.setIcon(icon27)
        self.homeXYButton.setIconSize(QtCore.QSize(40, 40))
        self.homeXYButton.setCheckable(False)
        self.homeXYButton.setAutoDefault(False)
        self.homeXYButton.setDefault(False)
        self.homeXYButton.setFlat(False)
        self.homeXYButton.setObjectName("homeXYButton")
        self.homeZButton = QtWidgets.QPushButton(self.motionTab)
        self.homeZButton.setGeometry(QtCore.QRect(240, 75, 70, 70))
        self.homeZButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.homeZButton.setFont(font)
        self.homeZButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.homeZButton.setText("")
        self.homeZButton.setIcon(icon27)
        self.homeZButton.setIconSize(QtCore.QSize(40, 40))
        self.homeZButton.setCheckable(False)
        self.homeZButton.setAutoDefault(False)
        self.homeZButton.setDefault(False)
        self.homeZButton.setFlat(False)
        self.homeZButton.setObjectName("homeZButton")
        self.motorOffButton = QtWidgets.QPushButton(self.motionTab)
        self.motorOffButton.setGeometry(QtCore.QRect(400, 225, 81, 45))
        self.motorOffButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.motorOffButton.setFont(font)
        self.motorOffButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"     border-bottom: none; /* no border for a flat push button */\n"
" border-top-right-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.motorOffButton.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("templates/img/motor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.motorOffButton.setIcon(icon28)
        self.motorOffButton.setIconSize(QtCore.QSize(40, 40))
        self.motorOffButton.setCheckable(False)
        self.motorOffButton.setAutoDefault(False)
        self.motorOffButton.setDefault(False)
        self.motorOffButton.setFlat(False)
        self.motorOffButton.setObjectName("motorOffButton")
        self.moveZMButton = QtWidgets.QPushButton(self.motionTab)
        self.moveZMButton.setGeometry(QtCore.QRect(240, 6, 70, 70))
        self.moveZMButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveZMButton.setFont(font)
        self.moveZMButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveZMButton.setText("")
        self.moveZMButton.setIcon(icon18)
        self.moveZMButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZMButton.setCheckable(False)
        self.moveZMButton.setAutoDefault(False)
        self.moveZMButton.setDefault(False)
        self.moveZMButton.setFlat(False)
        self.moveZMButton.setObjectName("moveZMButton")
        self.moveZPButton = QtWidgets.QPushButton(self.motionTab)
        self.moveZPButton.setGeometry(QtCore.QRect(240, 144, 70, 70))
        self.moveZPButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.moveZPButton.setFont(font)
        self.moveZPButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.moveZPButton.setText("")
        self.moveZPButton.setIcon(icon17)
        self.moveZPButton.setIconSize(QtCore.QSize(40, 40))
        self.moveZPButton.setCheckable(False)
        self.moveZPButton.setAutoDefault(False)
        self.moveZPButton.setDefault(False)
        self.moveZPButton.setFlat(False)
        self.moveZPButton.setObjectName("moveZPButton")
        self.XYLabel = QtWidgets.QLabel(self.motionTab)
        self.XYLabel.setGeometry(QtCore.QRect(2, 10, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.XYLabel.setFont(font)
        self.XYLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.XYLabel.setObjectName("XYLabel")
        self.ZLabel = QtWidgets.QLabel(self.motionTab)
        self.ZLabel.setGeometry(QtCore.QRect(200, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ZLabel.setFont(font)
        self.ZLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ZLabel.setObjectName("ZLabel")
        self.retractButton = QtWidgets.QPushButton(self.motionTab)
        self.retractButton.setGeometry(QtCore.QRect(370, 110, 70, 81))
        self.retractButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.retractButton.setFont(font)
        self.retractButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.retractButton.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("templates/img/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retractButton.setIcon(icon29)
        self.retractButton.setIconSize(QtCore.QSize(40, 40))
        self.retractButton.setCheckable(False)
        self.retractButton.setAutoDefault(False)
        self.retractButton.setDefault(False)
        self.retractButton.setFlat(False)
        self.retractButton.setObjectName("retractButton")
        self.extruderButton = QtWidgets.QPushButton(self.motionTab)
        self.extruderButton.setGeometry(QtCore.QRect(370, 30, 70, 81))
        self.extruderButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(15)
        self.extruderButton.setFont(font)
        self.extruderButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.extruderButton.setText("")
        self.extruderButton.setIcon(icon14)
        self.extruderButton.setIconSize(QtCore.QSize(40, 40))
        self.extruderButton.setCheckable(False)
        self.extruderButton.setAutoDefault(False)
        self.extruderButton.setDefault(False)
        self.extruderButton.setFlat(False)
        self.extruderButton.setObjectName("extruderButton")
        self.ELabel = QtWidgets.QLabel(self.motionTab)
        self.ELabel.setGeometry(QtCore.QRect(320, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ELabel.setFont(font)
        self.ELabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ELabel.setObjectName("ELabel")
        self.moveByLabel = QtWidgets.QLabel(self.motionTab)
        self.moveByLabel.setGeometry(QtCore.QRect(10, 235, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.moveByLabel.setFont(font)
        self.moveByLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.moveByLabel.setObjectName("moveByLabel")
        self.moveByLabel.raise_()
        self.step1Button.raise_()
        self.step10Button.raise_()
        self.step100Button.raise_()
        self.moveYPButton.raise_()
        self.moveYMButton.raise_()
        self.moveXPButton.raise_()
        self.moveXMButton.raise_()
        self.homeXYButton.raise_()
        self.homeZButton.raise_()
        self.motorOffButton.raise_()
        self.moveZMButton.raise_()
        self.moveZPButton.raise_()
        self.XYLabel.raise_()
        self.ZLabel.raise_()
        self.retractButton.raise_()
        self.extruderButton.raise_()
        self.ELabel.raise_()
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("templates/img/Motion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon30.addPixmap(QtGui.QPixmap("templates/img/Motion_Selected.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.motionTab, icon30, "")
        self.filamentTab = QtWidgets.QWidget()
        self.filamentTab.setObjectName("filamentTab")
        self.changeFilamentButton = QtWidgets.QToolButton(self.filamentTab)
        self.changeFilamentButton.setGeometry(QtCore.QRect(0, 180, 240, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(12)
        self.changeFilamentButton.setFont(font)
        self.changeFilamentButton.setStyleSheet("QToolButton  {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton :pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QToolButton :flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton :default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton :focus {\n"
"    outline: none;\n"
"}")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("templates/img/changeFilament.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentButton.setIcon(icon31)
        self.changeFilamentButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.changeFilamentButton.setObjectName("changeFilamentButton")
        self.setFlowRateButton = QtWidgets.QPushButton(self.filamentTab)
        self.setFlowRateButton.setGeometry(QtCore.QRect(300, 30, 91, 132))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.setFlowRateButton.setFont(font)
        self.setFlowRateButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.setFlowRateButton.setText("")
        self.setFlowRateButton.setIcon(icon1)
        self.setFlowRateButton.setIconSize(QtCore.QSize(50, 50))
        self.setFlowRateButton.setObjectName("setFlowRateButton")
        self.flowRateSpinBox = QtWidgets.QSpinBox(self.filamentTab)
        self.flowRateSpinBox.setGeometry(QtCore.QRect(62, 28, 241, 136))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(24)
        self.flowRateSpinBox.setFont(font)
        self.flowRateSpinBox.setStyleSheet("QSpinBox {\n"
"    padding-right: 5px; /* make room for the arrows */\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"   \n"
"}\n"
"QSpinBox ::text:selected {\n"
"    background-color: rgb(255, 146, 57);\n"
"   \n"
"}\n"
"QSpinBox::up-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"\n"
"border-top-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px; }\n"
"\n"
"\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"border-bottom-left-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 61px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"     height: 40px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"\n"
"}\n"
"\n"
"")
        self.flowRateSpinBox.setFrame(False)
        self.flowRateSpinBox.setReadOnly(False)
        self.flowRateSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.flowRateSpinBox.setAccelerated(True)
        self.flowRateSpinBox.setMinimum(75)
        self.flowRateSpinBox.setMaximum(125)
        self.flowRateSpinBox.setSingleStep(1)
        self.flowRateSpinBox.setProperty("value", 100)
        self.flowRateSpinBox.setObjectName("flowRateSpinBox")
        self.flowRateLabelControlPage = QtWidgets.QLabel(self.filamentTab)
        self.flowRateLabelControlPage.setGeometry(QtCore.QRect(65, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.flowRateLabelControlPage.setFont(font)
        self.flowRateLabelControlPage.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.flowRateLabelControlPage.setObjectName("flowRateLabelControlPage")
        self.toggleFilamentSensorButton = QtWidgets.QToolButton(self.filamentTab)
        self.toggleFilamentSensorButton.setEnabled(True)
        self.toggleFilamentSensorButton.setGeometry(QtCore.QRect(240, 180, 240, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(12)
        self.toggleFilamentSensorButton.setFont(font)
        self.toggleFilamentSensorButton.setStyleSheet("QToolButton  {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton :pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"    /* #dadbde #f6f7fa */\n"
"}\n"
"\n"
"\n"
"QToolButton :flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QToolButton :default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QToolButton :focus {\n"
"    outline: none;\n"
"}")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("templates/img/filamentSensorOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.toggleFilamentSensorButton.setIcon(icon32)
        self.toggleFilamentSensorButton.setIconSize(QtCore.QSize(60, 60))
        self.toggleFilamentSensorButton.setCheckable(False)
        self.toggleFilamentSensorButton.setChecked(False)
        self.toggleFilamentSensorButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toggleFilamentSensorButton.setObjectName("toggleFilamentSensorButton")
        self.flowRateSpinBox.raise_()
        self.setFlowRateButton.raise_()
        self.flowRateLabelControlPage.raise_()
        self.changeFilamentButton.raise_()
        self.toggleFilamentSensorButton.raise_()
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("templates/img/Spool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon33.addPixmap(QtGui.QPixmap("templates/img/Spool_Selected.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon33.addPixmap(QtGui.QPixmap("png/Spool_Selected.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon33.addPixmap(QtGui.QPixmap("png/Spool.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon33.addPixmap(QtGui.QPixmap("png/Spool_Selected.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.controlTabWidget.addTab(self.filamentTab, icon33, "")
        self.controlBackButton = QtWidgets.QPushButton(self.controlPage)
        self.controlBackButton.setGeometry(QtCore.QRect(380, 0, 100, 50))
        self.controlBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.controlBackButton.setFont(font)
        self.controlBackButton.setStyleSheet("QPushButton {\n"
"    border: none; /* no border for a flat push button */\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    /*border-bottom-right-radius: 15px;*/\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.controlBackButton.setText("")
        self.controlBackButton.setIcon(icon6)
        self.controlBackButton.setIconSize(QtCore.QSize(40, 40))
        self.controlBackButton.setCheckable(False)
        self.controlBackButton.setAutoDefault(False)
        self.controlBackButton.setDefault(False)
        self.controlBackButton.setFlat(False)
        self.controlBackButton.setObjectName("controlBackButton")
        self.stackedWidget.addWidget(self.controlPage)
        self.changeFilamentPage = QtWidgets.QWidget()
        self.changeFilamentPage.setObjectName("changeFilamentPage")
        self.selectFilamentlabel = QtWidgets.QLabel(self.changeFilamentPage)
        self.selectFilamentlabel.setGeometry(QtCore.QRect(0, 0, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.selectFilamentlabel.setFont(font)
        self.selectFilamentlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.selectFilamentlabel.setObjectName("selectFilamentlabel")
        self.changeFilamentComboBox = QtWidgets.QComboBox(self.changeFilamentPage)
        self.changeFilamentComboBox.setGeometry(QtCore.QRect(0, 40, 481, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(24)
        self.changeFilamentComboBox.setFont(font)
        self.changeFilamentComboBox.setStyleSheet(" QScrollBar:vertical {\n"
"     border: 1px solid black;\n"
"border-radius: 5px;\n"
"    background-color: rgb(40,40,40);\n"
"     width: 60px;\n"
"     margin: 67px 0 67px 0;\n"
" }\n"
"\n"
"/* Sets up the color and height of handle */\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 5px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"min-height: 7px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height:65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid black;\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"     height: 65px;\n"
"border-radius: 5px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
" image: url(./templates/img/arrows.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"QScrollBar::down-arrow:vertical {\n"
" image: url(./templates/img/arrows-5.png);\n"
"    width: 40px;\n"
"    height: 40px;\n"
" padding: 5px;\n"
" }\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid black;\n"
"    padding: 0px 18px 0px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
"\n"
"QComboBox::item {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: white;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    width: 60px;\n"
"     height: 50px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"image: url(./templates/img/arrows-5.png);\n"
"width: 30px;\n"
"height: 30px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(40, 40, 40);\n"
"    background: white;\n"
"}")
        self.changeFilamentComboBox.setEditable(False)
        self.changeFilamentComboBox.setMaxVisibleItems(8)
        self.changeFilamentComboBox.setIconSize(QtCore.QSize(30, 30))
        self.changeFilamentComboBox.setObjectName("changeFilamentComboBox")
        self.changeFilamentLoadButton = QtWidgets.QPushButton(self.changeFilamentPage)
        self.changeFilamentLoadButton.setGeometry(QtCore.QRect(0, 170, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        self.changeFilamentLoadButton.setFont(font)
        self.changeFilamentLoadButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("templates/img/load.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentLoadButton.setIcon(icon34)
        self.changeFilamentLoadButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentLoadButton.setObjectName("changeFilamentLoadButton")
        self.changeFilamentUnloadButton = QtWidgets.QPushButton(self.changeFilamentPage)
        self.changeFilamentUnloadButton.setGeometry(QtCore.QRect(240, 170, 240, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        self.changeFilamentUnloadButton.setFont(font)
        self.changeFilamentUnloadButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("templates/img/unload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeFilamentUnloadButton.setIcon(icon35)
        self.changeFilamentUnloadButton.setIconSize(QtCore.QSize(60, 60))
        self.changeFilamentUnloadButton.setObjectName("changeFilamentUnloadButton")
        self.changeFilamentBackButton = QtWidgets.QPushButton(self.changeFilamentPage)
        self.changeFilamentBackButton.setGeometry(QtCore.QRect(0, 260, 480, 60))
        self.changeFilamentBackButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(9)
        self.changeFilamentBackButton.setFont(font)
        self.changeFilamentBackButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.changeFilamentBackButton.setText("")
        self.changeFilamentBackButton.setIcon(icon6)
        self.changeFilamentBackButton.setIconSize(QtCore.QSize(50, 50))
        self.changeFilamentBackButton.setCheckable(False)
        self.changeFilamentBackButton.setAutoDefault(False)
        self.changeFilamentBackButton.setDefault(False)
        self.changeFilamentBackButton.setFlat(False)
        self.changeFilamentBackButton.setObjectName("changeFilamentBackButton")
        self.stackedWidget.addWidget(self.changeFilamentPage)
        self.changeFilamentProgressPage = QtWidgets.QWidget()
        self.changeFilamentProgressPage.setObjectName("changeFilamentProgressPage")
        self.changeFilamentStatus = QtWidgets.QLabel(self.changeFilamentProgressPage)
        self.changeFilamentStatus.setGeometry(QtCore.QRect(0, 160, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.changeFilamentStatus.setFont(font)
        self.changeFilamentStatus.setStyleSheet("color: rgb(255, 255, 255);")
        self.changeFilamentStatus.setObjectName("changeFilamentStatus")
        self.changeFilamentProgress = QtWidgets.QProgressBar(self.changeFilamentProgressPage)
        self.changeFilamentProgress.setGeometry(QtCore.QRect(0, 190, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.changeFilamentProgress.setFont(font)
        self.changeFilamentProgress.setStyleSheet("QProgressBar::chunk {\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:0, y2:0.512, stop:0 rgba(255, 28, 35, 255), stop:1 rgba(255, 68, 74, 255));\n"
"border-bottom-right-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgb(87, 87, 87);\n"
" /*  border-bottom-left-radius: 10px;\n"
" border-bottom-right-radius: 10px;*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}\n"
"")
        self.changeFilamentProgress.setMaximum(100)
        self.changeFilamentProgress.setProperty("value", 0)
        self.changeFilamentProgress.setAlignment(QtCore.Qt.AlignCenter)
        self.changeFilamentProgress.setTextVisible(True)
        self.changeFilamentProgress.setOrientation(QtCore.Qt.Horizontal)
        self.changeFilamentProgress.setObjectName("changeFilamentProgress")
        self.changeFilamentNameOperation = QtWidgets.QLabel(self.changeFilamentProgressPage)
        self.changeFilamentNameOperation.setGeometry(QtCore.QRect(0, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.changeFilamentNameOperation.setFont(font)
        self.changeFilamentNameOperation.setStyleSheet("color: rgb(255, 255, 255);")
        self.changeFilamentNameOperation.setObjectName("changeFilamentNameOperation")
        self.changeFilamentBackButton2 = QtWidgets.QPushButton(self.changeFilamentProgressPage)
        self.changeFilamentBackButton2.setGeometry(QtCore.QRect(0, 230, 481, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(13)
        self.changeFilamentBackButton2.setFont(font)
        self.changeFilamentBackButton2.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.changeFilamentBackButton2.setText("")
        self.changeFilamentBackButton2.setIcon(icon6)
        self.changeFilamentBackButton2.setIconSize(QtCore.QSize(50, 50))
        self.changeFilamentBackButton2.setObjectName("changeFilamentBackButton2")
        self.label_2 = QtWidgets.QLabel(self.changeFilamentProgressPage)
        self.label_2.setGeometry(QtCore.QRect(190, 55, 100, 100))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("templates/img/changeFilament2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.changeFilamentProgressPage)
        self.changeFilamentExtrudePage = QtWidgets.QWidget()
        self.changeFilamentExtrudePage.setObjectName("changeFilamentExtrudePage")
        self.feedFilamentlabel = QtWidgets.QLabel(self.changeFilamentExtrudePage)
        self.feedFilamentlabel.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel.setFont(font)
        self.feedFilamentlabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.feedFilamentlabel.setObjectName("feedFilamentlabel")
        self.loadDoneButton = QtWidgets.QPushButton(self.changeFilamentExtrudePage)
        self.loadDoneButton.setGeometry(QtCore.QRect(0, 230, 480, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(16)
        self.loadDoneButton.setFont(font)
        self.loadDoneButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.loadDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.loadDoneButton.setObjectName("loadDoneButton")
        self.ExtrudeButton = QtWidgets.QPushButton(self.changeFilamentExtrudePage)
        self.ExtrudeButton.setGeometry(QtCore.QRect(0, 140, 480, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(16)
        self.ExtrudeButton.setFont(font)
        self.ExtrudeButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.ExtrudeButton.setIconSize(QtCore.QSize(40, 40))
        self.ExtrudeButton.setObjectName("ExtrudeButton")
        self.feedFilamentlabel_2 = QtWidgets.QLabel(self.changeFilamentExtrudePage)
        self.feedFilamentlabel_2.setGeometry(QtCore.QRect(10, 40, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_2.setFont(font)
        self.feedFilamentlabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.feedFilamentlabel_2.setObjectName("feedFilamentlabel_2")
        self.stackedWidget.addWidget(self.changeFilamentExtrudePage)
        self.changeFilamentRetractPage = QtWidgets.QWidget()
        self.changeFilamentRetractPage.setObjectName("changeFilamentRetractPage")
        self.feedFilamentlabel_3 = QtWidgets.QLabel(self.changeFilamentRetractPage)
        self.feedFilamentlabel_3.setGeometry(QtCore.QRect(10, 40, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_3.setFont(font)
        self.feedFilamentlabel_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.feedFilamentlabel_3.setObjectName("feedFilamentlabel_3")
        self.unloadDoneButton = QtWidgets.QPushButton(self.changeFilamentRetractPage)
        self.unloadDoneButton.setGeometry(QtCore.QRect(0, 230, 480, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(16)
        self.unloadDoneButton.setFont(font)
        self.unloadDoneButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.unloadDoneButton.setIconSize(QtCore.QSize(40, 40))
        self.unloadDoneButton.setObjectName("unloadDoneButton")
        self.feedFilamentlabel_4 = QtWidgets.QLabel(self.changeFilamentRetractPage)
        self.feedFilamentlabel_4.setGeometry(QtCore.QRect(10, 10, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.feedFilamentlabel_4.setFont(font)
        self.feedFilamentlabel_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.feedFilamentlabel_4.setObjectName("feedFilamentlabel_4")
        self.retractFilamentButton = QtWidgets.QPushButton(self.changeFilamentRetractPage)
        self.retractFilamentButton.setGeometry(QtCore.QRect(0, 140, 480, 91))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(16)
        self.retractFilamentButton.setFont(font)
        self.retractFilamentButton.setStyleSheet("QPushButton {\n"
"     border: 1px solid rgb(87, 87, 87);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.188, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.retractFilamentButton.setIconSize(QtCore.QSize(40, 40))
        self.retractFilamentButton.setObjectName("retractFilamentButton")
        self.stackedWidget.addWidget(self.changeFilamentRetractPage)
        MainWindow.setCentralWidget(self.mainApplication)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(29)
        self.controlTabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pgLock_bt6.setText(_translate("MainWindow", "6"))
        self.pgLock_bt0.setText(_translate("MainWindow", "0"))
        self.pgLock_bt4.setText(_translate("MainWindow", "4"))
        self.passwordlabel_4.setText(_translate("MainWindow", "User Number:"))
        self.pgLock_bt9.setText(_translate("MainWindow", "9"))
        self.pgLock_bt8.setText(_translate("MainWindow", "8"))
        self.pgLock_bt1.setText(_translate("MainWindow", "1"))
        self.passwordlabel_2.setText(_translate("MainWindow", "Machine ID:"))
        self.pgLock_pin.setText(_translate("MainWindow", "*******"))
        self.pgLock_bt3.setText(_translate("MainWindow", "3"))
        self.pgLock_bt7.setText(_translate("MainWindow", "7"))
        self.passwordlabel_5.setText(_translate("MainWindow", "Call 080 4709 1810 for support"))
        self.pgLock_HID.setText(_translate("MainWindow", "XXXX"))
        self.pgLock_bt5.setText(_translate("MainWindow", "5"))
        self.pgLock_bt2.setText(_translate("MainWindow", "2"))
        self.FileNameLabel.setText(_translate("MainWindow", "File:"))
        self.printTimeLabel.setText(_translate("MainWindow", "Print Time:"))
        self.fileName.setText(_translate("MainWindow", "fileName"))
        self.printTime.setText(_translate("MainWindow", "printTime"))
        self.timeLeftLabel.setText(_translate("MainWindow", "Time Left:"))
        self.tool0TargetTemperature.setText(_translate("MainWindow", "0"))
        self.tool0TempBar.setFormat(_translate("MainWindow", "%v"))
        self.tool0ActualTemperature.setText(_translate("MainWindow", "0"))
        self.printProgressBar.setFormat(_translate("MainWindow", "%p%"))
        self.timeLeft.setText(_translate("MainWindow", "timeLeft"))
        self.printerStatus.setText(_translate("MainWindow", "Status"))
        self.celciusLabel.setText(_translate("MainWindow", "°C"))
        self.celciusLabel_2.setText(_translate("MainWindow", "°C"))
        self.bedTempBar.setFormat(_translate("MainWindow", "%v"))
        self.bedActualTemperatute.setText(_translate("MainWindow", "0"))
        self.bedTargetTemperature.setText(_translate("MainWindow", "0"))
        self.ipStatus.setText(_translate("MainWindow", "Not Connected"))
        self.menuControlButton.setText(_translate("MainWindow", "Control"))
        self.menuPrintButton.setText(_translate("MainWindow", "Print"))
        self.menuSettingsButton.setText(_translate("MainWindow", "Settings"))
        self.menuCartButton.setText(_translate("MainWindow", "Cart"))
        self.menuCalibrateButton.setText(_translate("MainWindow", "Calibrate"))
        self.networkSettingsButton.setText(_translate("MainWindow", "Network Settings"))
        self.displaySettingsButton.setText(_translate("MainWindow", "Display Settings"))
        self.pairPhoneButton.setText(_translate("MainWindow", "Open in Smartphone"))
        self.OTAButton.setText(_translate("MainWindow", "Check for Updates"))
        self.versionButton.setText(_translate("MainWindow", "Version"))
        self.restorePrintSettingsButton.setText(_translate("MainWindow", "Restore Print Settings"))
        self.restoreFactoryDefaultsButton.setText(_translate("MainWindow", "Restore Factory Defaults"))
        self.restartButton.setText(_translate("MainWindow", "Restart"))
        self.ssidlabel.setText(_translate("MainWindow", "Enter SSID:"))
        self.passwordlabel.setText(_translate("MainWindow", "Enter Password:"))
        self.wifiSettingsDoneButton.setText(_translate("MainWindow", "Done"))
        self.wifiSettingsCancelButton.setText(_translate("MainWindow", "Cancel"))
        self.wifiSettingsSSIDKeyboardButton.setText(_translate("MainWindow", "..."))
        self.hiddenCheckBox.setText(_translate("MainWindow", "Hidden "))
        self.ethSettingsDoneButton.setText(_translate("MainWindow", "Done"))
        self.ethSettingsCancelButton.setText(_translate("MainWindow", "Cancel"))
        self.ethStaticCheckBox.setText(_translate("MainWindow", "Static IP"))
        self.ethStaticIpLabel.setText(_translate("MainWindow", "IP Address"))
        self.ethStaticGatewayLabel.setText(_translate("MainWindow", "Gateway"))
        self.ethStaticGatewayKeyboardButton.setText(_translate("MainWindow", "..."))
        self.ethStaticIpKeyboardButton.setText(_translate("MainWindow", "..."))
        self.networkInfoButton.setText(_translate("MainWindow", "Network Info"))
        self.configureWifiButton.setText(_translate("MainWindow", "Configure WiFi"))
        self.configureEthButton.setText(_translate("MainWindow", "Configure Ethernet"))
        self.calibrateTouch.setText(_translate("MainWindow", "Calibrate Touch"))
        self.rotateDisplay.setText(_translate("MainWindow", "Rotate Display"))
        self.rotateDisplaySettingsDoneButton.setText(_translate("MainWindow", "Done"))
        self.rotateDisplaySettingsCancelButton.setText(_translate("MainWindow", "Cancel"))
        self.rotateDisplaySettingsComboBox.setItemText(0, _translate("MainWindow", "Normal"))
        self.rotateDisplaySettingsComboBox.setItemText(1, _translate("MainWindow", "Flipped"))
        self.rotateDisplaySettingsLabel.setText(_translate("MainWindow", "Rotation"))
        self.hostnameLabel.setText(_translate("MainWindow", "mDNS URL"))
        self.hostname.setText(_translate("MainWindow", "Hostname"))
        self.wifiIpLabel.setText(_translate("MainWindow", "Wi-Fi MAC"))
        self.wifiMac.setText(_translate("MainWindow", "WiFi"))
        self.lanIpLabel.setText(_translate("MainWindow", "Ethernet MAC"))
        self.lanMac.setText(_translate("MainWindow", "Ethernet"))
        self.wifiMacLabel.setText(_translate("MainWindow", "Wi-Fi IP"))
        self.lanMacLabel.setText(_translate("MainWindow", "Ethernet IP"))
        self.wifiIp.setText(_translate("MainWindow", "WiFi"))
        self.lanIp.setText(_translate("MainWindow", "Ethernet"))
        self.wifiApLabel.setText(_translate("MainWindow", "Wi-Fi AP"))
        self.wifiAp.setText(_translate("MainWindow", "WiFi"))
        self.performUpdateButton.setText(_translate("MainWindow", "Update"))
        self.logTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gotham\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Software Update Starting, Please Wait....</p></body></html>"))
        self.firmwareUpdateLog.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gotham\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Firmware Update Starting, Please Wait....</span></p></body></html>"))
        self.calibrateLabel.setText(_translate("MainWindow", "Calibrate:"))
        self.nozzleOffsetButton.setText(_translate("MainWindow", "Height"))
        self.calibrationWizardButton.setText(_translate("MainWindow", "Wizard"))
        self.quickCalibrationButton.setText(_translate("MainWindow", "Quick Calibration"))
        self.calibrationWizardLabel.setText(_translate("MainWindow", "Calibration Wizard:"))
        self.calibrateLabel_6.setText(_translate("MainWindow", "We start by calibrating the print bed\'s level. A perfectly leveled bed is essential to get reliable printing performance."))
        self.quickStep1NextButton.setText(_translate("MainWindow", "Next"))
        self.quickStep1CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.calibrateLabel_7.setText(_translate("MainWindow", "Wait for all moves to finish and click Next"))
        self.quickStep2NextButton.setText(_translate("MainWindow", "Next"))
        self.quickStep2CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.quickStep3CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.quickStep3NextButton.setText(_translate("MainWindow", "Next"))
        self.calibrateLabel_10.setText(_translate("MainWindow", "Tighten right leveling screw untill nozzle just touches bed."))
        self.quickStep4CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.quickStep4NextButton.setText(_translate("MainWindow", "Next"))
        self.calibrateLabel_12.setText(_translate("MainWindow", "Do the same for the left screw"))
        self.calibrateLabel_25.setText(_translate("MainWindow", "Now tighten the center back  screw"))
        self.quickStep5NextButton.setText(_translate("MainWindow", "Next"))
        self.quickStep5CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.nozzleOffsetDoubleSpinBox.setSuffix(_translate("MainWindow", "mm"))
        self.feedRateLabelControlPage_3.setText(_translate("MainWindow", "Change the initial height for the first layer of the print. +ve value increases height, -ve value reduces it."))
        self.fromUsbButton.setText(_translate("MainWindow", "USB"))
        self.printFromLabel.setText(_translate("MainWindow", "Print From :"))
        self.fromLocalButton.setText(_translate("MainWindow", "Local "))
        self.fileSelected.setText(_translate("MainWindow", "You Selected: "))
        self.fileSelectedPrintButton.setText(_translate("MainWindow", "Print"))
        self.fileSizeSelected.setText(_translate("MainWindow", "Size"))
        self.fileDateSelected.setText(_translate("MainWindow", "Date"))
        self.filePrintTimeSelected.setText(_translate("MainWindow", "EST"))
        self.filamentVolumeSelected.setText(_translate("MainWindow", "Fil. Volume"))
        self.fileSizeSelectedLabel.setText(_translate("MainWindow", "Size:"))
        self.fileDateSelectedLabel.setText(_translate("MainWindow", "Date:"))
        self.filePrintTimeSelectedLabel.setText(_translate("MainWindow", "Estimated Print Time:"))
        self.filamentVolumeSelectedLabel.setText(_translate("MainWindow", "Volume:"))
        self.filamentLengthFileSelected.setText(_translate("MainWindow", "Fil. Length"))
        self.filamentLengthSelectedLabel.setText(_translate("MainWindow", "Length:"))
        self.fileSelectedUSBTransferButton.setText(_translate("MainWindow", "Save to Local"))
        self.fileSelectedUSBName.setText(_translate("MainWindow", "File Name"))
        self.fileSelectedUSBPrintButton.setText(_translate("MainWindow", "Print"))
        self.feedRateLabelControlPage.setText(_translate("MainWindow", "Feed Rate :"))
        self.flowRateLabelControlPage_5.setText(_translate("MainWindow", "Tune Bed Height during Print :"))
        self.feedRateSpinBox.setSuffix(_translate("MainWindow", "%"))
        self.toolLabel.setText(_translate("MainWindow", "Nozzle:"))
        self.toolTempSpinBox.setSuffix(_translate("MainWindow", "°C"))
        self.bedTempSpinBox.setSuffix(_translate("MainWindow", "°C"))
        self.bedLabel_2.setText(_translate("MainWindow", "Bed:"))
        self.step1Button.setText(_translate("MainWindow", "1 mm"))
        self.step10Button.setText(_translate("MainWindow", "10 mm"))
        self.step100Button.setText(_translate("MainWindow", "100 mm"))
        self.XYLabel.setText(_translate("MainWindow", "X/Y :"))
        self.ZLabel.setText(_translate("MainWindow", "Z:"))
        self.ELabel.setText(_translate("MainWindow", "E:"))
        self.moveByLabel.setText(_translate("MainWindow", "Move By:"))
        self.changeFilamentButton.setText(_translate("MainWindow", "Change Filament"))
        self.flowRateSpinBox.setSuffix(_translate("MainWindow", "%"))
        self.flowRateLabelControlPage.setText(_translate("MainWindow", "Flow Rate :"))
        self.toggleFilamentSensorButton.setText(_translate("MainWindow", "Filament/Door Sensor"))
        self.selectFilamentlabel.setText(_translate("MainWindow", "Select Filament :"))
        self.changeFilamentLoadButton.setText(_translate("MainWindow", "Load"))
        self.changeFilamentUnloadButton.setText(_translate("MainWindow", "Unload"))
        self.changeFilamentStatus.setText(_translate("MainWindow", "Heating ..."))
        self.changeFilamentProgress.setFormat(_translate("MainWindow", "%p%"))
        self.changeFilamentNameOperation.setText(_translate("MainWindow", "Loading Filament"))
        self.feedFilamentlabel.setText(_translate("MainWindow", "Feed Filament into Extruder"))
        self.loadDoneButton.setText(_translate("MainWindow", "Done"))
        self.ExtrudeButton.setText(_translate("MainWindow", "Extrude"))
        self.feedFilamentlabel_2.setText(_translate("MainWindow", "Click \"Extrude\" untill filament starts extruding"))
        self.feedFilamentlabel_3.setText(_translate("MainWindow", "Click \"Retract\" untill filament is removed"))
        self.unloadDoneButton.setText(_translate("MainWindow", "Done"))
        self.feedFilamentlabel_4.setText(_translate("MainWindow", "Retract Filament From Extruder"))
        self.retractFilamentButton.setText(_translate("MainWindow", "Retract"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

