# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import ui.res_rc

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(798, 414)
        SettingsWindow.setMaximumSize(QSize(798, 414))
        SettingsWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/res/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsWindow.setWindowIcon(icon)
        SettingsWindow.setDocumentMode(False)
        SettingsWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(SettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_vendor = QLabel(self.groupBox)
        self.label_vendor.setObjectName(u"label_vendor")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_vendor.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_vendor)

        self.lineEdit_vendor = QLineEdit(self.groupBox)
        self.lineEdit_vendor.setObjectName(u"lineEdit_vendor")
        self.lineEdit_vendor.setMaxLength(64)
        self.lineEdit_vendor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_vendor.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_vendor)

        self.label_model = QLabel(self.groupBox)
        self.label_model.setObjectName(u"label_model")
        self.label_model.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_model)

        self.lineEdit_model = QLineEdit(self.groupBox)
        self.lineEdit_model.setObjectName(u"lineEdit_model")
        self.lineEdit_model.setMaxLength(64)
        self.lineEdit_model.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_model.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_model)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_lot_count = QLabel(self.groupBox_2)
        self.label_lot_count.setObjectName(u"label_lot_count")
        self.label_lot_count.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_lot_count)

        self.lineEdit_lot_count = QLineEdit(self.groupBox_2)
        self.lineEdit_lot_count.setObjectName(u"lineEdit_lot_count")
        self.lineEdit_lot_count.setMaxLength(11)
        self.lineEdit_lot_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_lot_count.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_lot_count)

        self.label_lot_count_2 = QLabel(self.groupBox_2)
        self.label_lot_count_2.setObjectName(u"label_lot_count_2")
        self.label_lot_count_2.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_lot_count_2)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox)


        self.verticalLayout_4.addLayout(self.formLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_set_settings = QPushButton(self.centralwidget)
        self.pushButton_set_settings.setObjectName(u"pushButton_set_settings")
        font2 = QFont()
        font2.setPointSize(30)
        self.pushButton_set_settings.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_set_settings)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.label_vendor.setText(QCoreApplication.translate("SettingsWindow", u"Vendor:", None))
        self.label_model.setText(QCoreApplication.translate("SettingsWindow", u"Model:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SettingsWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_lot_count.setText(QCoreApplication.translate("SettingsWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432 \u043b\u043e\u0442\u0435:", None))
        self.label_lot_count_2.setText(QCoreApplication.translate("SettingsWindow", u"\u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0441\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0442\u044c ?", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SettingsWindow", u"2 SN", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SettingsWindow", u"3 SN", None))

        self.pushButton_set_settings.setText(QCoreApplication.translate("SettingsWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c", None))
    # retranslateUi

