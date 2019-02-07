# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from read_email import ReadEmail
from tts import TTS


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            28, 530, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 8, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            705, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(
            28, 530, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 8, 1)
        self.msgs_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.msgs_tableWidget.sizePolicy().hasHeightForWidth())
        self.msgs_tableWidget.setSizePolicy(sizePolicy)
        self.msgs_tableWidget.setObjectName("msgs_tableWidget")
        self.msgs_tableWidget.setColumnCount(4)
        self.msgs_tableWidget.setRowCount(0)
        self.msgs_tableWidget.setHorizontalHeaderLabels(
            ['Date', 'From', 'Subject', 'Message'])
        self.msgs_tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.msgs_tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.msgs_tableWidget, 1, 1, 1, 2)
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy)
        self.refresh_btn.setObjectName("refresh_btn")
        self.gridLayout.addWidget(self.refresh_btn, 2, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(
            705, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 2)
        self.labelfrom = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelfrom.sizePolicy().hasHeightForWidth())
        self.labelfrom.setSizePolicy(sizePolicy)
        self.labelfrom.setObjectName("labelfrom")
        self.gridLayout.addWidget(self.labelfrom, 4, 1, 1, 1)
        self.from_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.from_label.sizePolicy().hasHeightForWidth())
        self.from_label.setSizePolicy(sizePolicy)
        self.from_label.setText("")
        self.from_label.setObjectName("from_label")
        self.gridLayout.addWidget(self.from_label, 4, 2, 1, 1)
        self.labelsubject = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelsubject.sizePolicy().hasHeightForWidth())
        self.labelsubject.setSizePolicy(sizePolicy)
        self.labelsubject.setObjectName("labelsubject")
        self.gridLayout.addWidget(self.labelsubject, 5, 1, 1, 1)
        self.subject_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.subject_label.sizePolicy().hasHeightForWidth())
        self.subject_label.setSizePolicy(sizePolicy)
        self.subject_label.setText("")
        self.subject_label.setObjectName("subject_label")
        self.gridLayout.addWidget(self.subject_label, 5, 2, 1, 1)
        self.msgText = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.msgText.sizePolicy().hasHeightForWidth())
        self.msgText.setSizePolicy(sizePolicy)
        self.msgText.setObjectName("msgText")
        self.gridLayout.addWidget(self.msgText, 6, 1, 1, 2)
        self.readMsg_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.readMsg_btn.sizePolicy().hasHeightForWidth())
        self.readMsg_btn.setSizePolicy(sizePolicy)
        self.readMsg_btn.setObjectName("readMsg_btn")
        self.gridLayout.addWidget(self.readMsg_btn, 7, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.msgs_tableWidget.cellClicked.connect(
            self.cell_was_clicked)  # ==== TRIGGER
        self.refresh_btn.clicked.connect(self.readEmail)
        self.readMsg_btn.clicked.connect(self.text_to_speech)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.readEmail()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelfrom.setText(_translate("MainWindow", "From    :"))
        self.labelsubject.setText(_translate("MainWindow", "Subject :"))
        self.readMsg_btn.setText(_translate("MainWindow", "Read message"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def readEmail(self):
        self.read_email = ReadEmail()
        vals = self.read_email.read_email()

        print(vals)
        row_numbers = []
        column_numbers = []

        self.msgs_tableWidget.setRowCount(len(vals))

        for row_number, row_data in enumerate(vals):
            for column_number, data in enumerate(row_data):
                row_numbers.append(row_number)
                column_numbers.append(column_number)

        values = []

        for val in vals:
            for i in val:
                values.append(i)

        print(values)

        for i in range(len(values)):
            self.msgs_tableWidget.setItem(
                row_numbers[i], column_numbers[i], QtWidgets.QTableWidgetItem(str(values[i])))

    def cell_was_clicked(self, row, column):  # Fungsi trigger jika row diklik
        sent_from_item = self.msgs_tableWidget.item(row, 1)
        subject_item = self.msgs_tableWidget.item(row, 2)
        message_item = self.msgs_tableWidget.item(row, 3)

        self.sent_from = sent_from_item.text()
        self.subject = subject_item.text()
        self.message = message_item.text()

        self.from_label.setText(self.sent_from)
        self.subject_label.setText(self.subject)
        self.msgText.setPlainText(self.message)

    def text_to_speech(self):
        self.tts = TTS()
        text = self.msgText.toPlainText()
        self.tts.read_text(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
