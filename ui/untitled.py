# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1430, 812)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1430, 605))
        icon = QIcon()
        icon.addFile(u":/res/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow \n"
"{\n"
"	background-color: #2137fb;\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #333399;\n"
"    color: #999;\n"
"};\n"
"QMenuBar::item\n"
"{\n"
"    background-color: #333399;\n"
"    color: #999;\n"
"};\n"
"QMenuBar::item::selected\n"
"{\n"
"    background-color: #3399cc;\n"
"    color: #fff;\n"
"};\n"
"QMenu\n"
"{\n"
"    background-color: #3399cc;\n"
"    color: #fff;\n"
"};\n"
"QMenu::item::selected\n"
"{\n"
"    background-color: #333399;\n"
"    color: #999;\n"
"};")
        self.action_new_project = QAction(MainWindow)
        self.action_new_project.setObjectName(u"action_new_project")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_close = QAction(MainWindow)
        self.action_close.setObjectName(u"action_close")
        self.action_set_parameters = QAction(MainWindow)
        self.action_set_parameters.setObjectName(u"action_set_parameters")
        self.action_set_default_parameters = QAction(MainWindow)
        self.action_set_default_parameters.setObjectName(u"action_set_default_parameters")
        self.action_saveas = QAction(MainWindow)
        self.action_saveas.setObjectName(u"action_saveas")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_instruction = QAction(MainWindow)
        self.action_instruction.setObjectName(u"action_instruction")
        self.action_about_programs = QAction(MainWindow)
        self.action_about_programs.setObjectName(u"action_about_programs")
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.action_set_config = QAction(MainWindow)
        self.action_set_config.setObjectName(u"action_set_config")
        font = QFont()
        font.setPointSize(24)
        self.action_set_config.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.groupBox_model = QGroupBox(self.centralwidget)
        self.groupBox_model.setObjectName(u"groupBox_model")
        font1 = QFont()
        self.groupBox_model.setFont(font1)
        self.groupBox_model.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-color: none;\n"
"    margin-top: 60px;\n"
"    font-size: 40px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 150px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_model.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_model)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_vender = QLabel(self.groupBox_model)
        self.label_vender.setObjectName(u"label_vender")
        font2 = QFont()
        font2.setPointSize(60)
        font2.setBold(True)
        self.label_vender.setFont(font2)
        self.label_vender.setStyleSheet(u"color: white")
        self.label_vender.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_vender)

        self.label_model = QLabel(self.groupBox_model)
        self.label_model.setObjectName(u"label_model")
        self.label_model.setFont(font2)
        self.label_model.setStyleSheet(u"color: white")
        self.label_model.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_model)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.groupBox_model)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_date = QGroupBox(self.centralwidget)
        self.groupBox_date.setObjectName(u"groupBox_date")
        self.groupBox_date.setFont(font1)
        self.groupBox_date.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-color: none;\n"
"    margin-top: 60px;\n"
"    font-size: 40px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 150px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_date)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_date = QLabel(self.groupBox_date)
        self.label_date.setObjectName(u"label_date")
        font3 = QFont()
        font3.setPointSize(40)
        font3.setBold(True)
        self.label_date.setFont(font3)
        self.label_date.setStyleSheet(u"color: white")
        self.label_date.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_date)


        self.verticalLayout_4.addWidget(self.groupBox_date)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-color: none;\n"
"    margin-top: 60px;\n"
"    font-size: 40px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 150px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_lot_count = QLabel(self.groupBox)
        self.label_lot_count.setObjectName(u"label_lot_count")
        self.label_lot_count.setFont(font3)
        self.label_lot_count.setStyleSheet(u"color: white")
        self.label_lot_count.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_lot_count)

        self.label_sn_counts = QLabel(self.groupBox)
        self.label_sn_counts.setObjectName(u"label_sn_counts")
        self.label_sn_counts.setFont(font3)
        self.label_sn_counts.setStyleSheet(u"color: white")
        self.label_sn_counts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_sn_counts)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.groupBox_last_sn = QGroupBox(self.centralwidget)
        self.groupBox_last_sn.setObjectName(u"groupBox_last_sn")
        self.groupBox_last_sn.setFont(font1)
        self.groupBox_last_sn.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-color: none;\n"
"    margin-top: 60px;\n"
"    font-size: 40px;\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 5px 150px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_last_sn)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_last_sn = QLabel(self.groupBox_last_sn)
        self.label_last_sn.setObjectName(u"label_last_sn")
        self.label_last_sn.setFont(font3)
        self.label_last_sn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_last_sn)


        self.verticalLayout_6.addWidget(self.groupBox_last_sn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lineEdit_input_sn = QLineEdit(self.centralwidget)
        self.lineEdit_input_sn.setObjectName(u"lineEdit_input_sn")
        font4 = QFont()
        font4.setPointSize(25)
        self.lineEdit_input_sn.setFont(font4)
        self.lineEdit_input_sn.setStyleSheet(u"background-color: white")
        self.lineEdit_input_sn.setMaxLength(80)
        self.lineEdit_input_sn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_input_sn.setDragEnabled(False)
        self.lineEdit_input_sn.setPlaceholderText(u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 SN:")

        self.horizontalLayout_3.addWidget(self.lineEdit_input_sn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu = QMenuBar(MainWindow)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 1430, 42))
        font5 = QFont()
        font5.setPointSize(20)
        self.menu.setFont(font5)
        self.menu.setDefaultUp(False)
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setFont(font5)
        MainWindow.setMenuBar(self.menu)

        self.menu.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.action_set_config)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Packing Scan Logging", None))
        self.action_new_project.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_close.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_set_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.action_set_default_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.action_saveas.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0432\u0438\u0434", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043b\u043e\u0442\u0435", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_instruction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.action_about_programs.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.action_set_config.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox_model.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.label_vender.setText(QCoreApplication.translate("MainWindow", u"TV Hartens", None))
        self.label_model.setText(QCoreApplication.translate("MainWindow", u"HTM-55UHD05B-S2 UK", None))
        self.groupBox_date.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"12.11.2024\n"
"09:17:21", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435:", None))
        self.label_lot_count.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0442: 1200 \u0448\u0442", None))
        self.label_sn_counts.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435: 2 \u0441\u0442\u043e\u043b\u0431\u0430", None))
        self.groupBox_last_sn.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u0443\u0434\u0430\u0447\u043d\u044b\u0439 SN", None))
        self.label_last_sn.setText(QCoreApplication.translate("MainWindow", u"SN: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", None))
        self.lineEdit_input_sn.setText("")
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

