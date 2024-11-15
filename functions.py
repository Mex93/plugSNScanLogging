from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize
import re

from enuuuums import SMBOX_ICON_TYPE


def send_message_box(icon_style, text: str, title: str, variant_yes: str, variant_no: str, callback=None):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    match icon_style:
        case _, SMBOX_ICON_TYPE.ICON_NONE:
            msg.setIcon(QMessageBox.Icon.NoIcon)
        case SMBOX_ICON_TYPE.ICON_ERROR:
            msg.setIcon(QMessageBox.Icon.Critical)
        case SMBOX_ICON_TYPE.ICON_WARNING:
            msg.setIcon(QMessageBox.Icon.Warning)
        case SMBOX_ICON_TYPE.ICON_INFO:
            msg.setIcon(QMessageBox.Icon.Information)
        # case SMBOX_ICON_TYPE.ICON_SUCCESS:
        #     pass

    icon = QIcon()
    icon.addFile(u":/res/images/logo.ico", QSize(), QIcon.Normal, QIcon.Off)

    msg.setWindowIcon(icon)
    if len(variant_yes) > 0:
        msg.addButton(variant_yes, QtWidgets.QMessageBox.ButtonRole.YesRole)
    if len(variant_no) > 0:
        msg.addButton(variant_no, QtWidgets.QMessageBox.ButtonRole.NoRole)
    msg.setText(text)

    font = QFont()
    font.setFamilies([u"Segoe UI Emoji"])
    font.setPointSize(12)
    msg.setFont(font)

    if callback is not None:
        msg.buttonClicked.connect(callback)

    msg.exec()
    return msg
