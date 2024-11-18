import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase
from PySide6.QtCore import Qt, QTimer
from datetime import datetime

from enuuuums import COMPARED_RESULT
from ui.untitled import Ui_MainWindow
from ui.settings_menu import Ui_SettingsWindow
from CSettings import Settings
from functions import send_message_box, SMBOX_ICON_TYPE
from CExcelLog import CExcelLog
from CConfig import CConfig

# pyside6-uic .\ui\untitled.ui -o .\ui\untitled.py
# pyside6-uic .\ui\settings_menu.ui -o .\ui\settings_menu.py
# pyside6-rcc .\ui\res.qrc -o .\ui\res_rc.py
# Press the green button in the gutter to run the script.

STANDART_SN_TEXT = 'SN: XXXXXXXXXX'


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__base_program_version = "0.1"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'Packing Scan Logging 2024 KVANT v0.1b')

        self.config = CConfig()
        try:
            self.config.load_data()
        except:
            self.config.create_config()
            self.config.load_data()

        self.timer = QTimer()
        self.timer.timeout.connect(self.set_update_current_time)
        self.timer.start(1000)

        self.settings_window = SettingsWindow(self)
        self.first_load = True
        self.settings_window.set_show(False)
        self.set_default()

        self.ui.action_set_config.triggered.connect(self.on_user_open_config)
        self.ui.lineEdit_input_sn.returnPressed.connect(self.on_user_input_sn)

    def on_user_input_sn(self):
        text = self.ui.lineEdit_input_sn.text()
        if 6 < len(text) < 64:
            clear_text = text.upper().replace(" ", "")
            if 6 < len(clear_text) < 64:
                if Settings.is_valid_sn(clear_text):
                    last_sn_string = InputBuffer.get_compare_string()

                    result = InputBuffer.set_comare(clear_text)
                    match result:
                        case COMPARED_RESULT.COMPARED_FAIL:
                            if last_sn_string != "":
                                self.set_last_sn(last_sn_string, '#ff0404')
                            else:
                                self.set_last_sn(clear_text, '#ff0404')

                        case COMPARED_RESULT.COMPARED_SUCCESS:
                            self.set_last_sn(clear_text, '#40ff22')
                            result = CExcelLog.print_log(
                                model=Settings.get_model(),
                                vender=Settings.get_vender(),
                                sn=clear_text)
                            if not result:
                                self.set_last_sn(clear_text, 'red')

                        case COMPARED_RESULT.COMPARED_IS_SUCCESS_PROGRESS:
                            self.set_last_sn(clear_text, '#fff335')

                self.ui.lineEdit_input_sn.clear()
                return
        self.ui.lineEdit_input_sn.clear()

    def on_user_open_config(self):
        self.settings_window.set_show(True)

    def set_default(self):
        self.set_model("-")
        self.set_vender("-")
        self.set_lot_count("0")
        self.set_sns("-")
        self.set_last_sn(STANDART_SN_TEXT, color='black')

    def set_close(self):
        self.settings_window.close()
        self.close()

    def set_model(self, text: str) -> None:
        self.ui.label_model.setText(text)

    def set_vender(self, text: str) -> None:
        self.ui.label_vender.setText(text)

    def set_lot_count(self, text: str) -> None:
        self.ui.label_lot_count.setText(f'Лот: {text} шт')

    def set_sns(self, text: str) -> None:
        self.ui.label_sn_counts.setText(f'Сравнение: {text}')

    def set_last_sn(self, text: str, color: str) -> None:
        self.ui.label_last_sn.setText(text)

        self.ui.label_last_sn.setStyleSheet(f"color: {color};")

    def set_update_current_time(self) -> None:
        current_time = datetime.now()
        self.ui.label_date.setText(f'{current_time.day:02}.{current_time.month:02}.{current_time.year}\n'
                                   f'{current_time.hour:02}:{current_time.minute:02}:{current_time.second:02}')


class SettingsWindow(QMainWindow):
    def __init__(self, main_window: MainWindow, parent=None):
        super().__init__(parent)

        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'Настройки')

        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.main_window = main_window

        self.ui.pushButton_set_settings.clicked.connect(self.on_user_press_on_set_setting)

    def on_user_press_on_set_setting(self):
        vendor: str = self.get_vender()
        model: str = self.get_model()
        count: str = self.get_lot_count()
        sns: str = self.get_sns()
        ERROR_LABEL = '!Error!'

        if not Settings.is_vendor_valid(vendor):
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Неверно задан Vendor устройства.\n\n"
                                  f"REGEX: '^[A-Za-z0-9]+$'",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)
            self.set_vender(ERROR_LABEL)
            return

        if not Settings.is_model_valid(model):
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Неверно задана Model устройства.\n\n"
                                  f"REGEX: '^[A-Za-z0-9 _,-]+$'",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)
            self.set_model(ERROR_LABEL)
            return

        if model == vendor:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Vendor и Model не должны быть одинаковы!",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)
            self.set_model(ERROR_LABEL)
            self.set_vender(ERROR_LABEL)
            return

        count_int: int = Settings.convert_data_to_int(count)
        if count_int == -1 or not Settings.is_only_integer(count) or (count_int > 10000 or count_int < 1):
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Неверно задан Lot Count устройства.\n\n"
                                  f"REGEX: '1 >= 10000'",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)
            self.set_lot_count(ERROR_LABEL)
            return

        if sns != "2 SN" and sns != "3 SN":
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Неверно задан SN counts.\n",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)

            self.main_window.set_close()
            return

        for item in (vendor, model, count):
            if item == ERROR_LABEL:
                send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                                 text=f"Неверно заданы поля -> '{ERROR_LABEL}'.\n",
                                 title="Ошибка",
                                 variant_yes="Ок", variant_no="", callback=None)
        sns_int = 0
        if sns == '2 SN':
            sns_int = 2
        elif sns == '3 SN':
            sns_int = 3

        if sns_int == 0:
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Неверно задан SN Count.",
                             title="Ошибка",
                             variant_yes="Ок", variant_no="", callback=None)
            return

        Settings.set_sns(sns_int)
        Settings.set_vender(vendor)
        Settings.set_model(model)
        Settings.set_lot_count(count)

        self.main_window.set_lot_count(count)
        self.main_window.set_vender(vendor)
        self.main_window.set_model(model)
        InputBuffer.set_max_checked(sns_int)
        InputBuffer.clear()
        self.main_window.set_last_sn(STANDART_SN_TEXT, 'black')

        self.main_window.set_sns("2 SN" if sns == '2 SN' else "3 SN" if sns == '3 SN' else "????")

        if self.main_window.first_load:
            self.main_window.first_load = False

        self.main_window.config.set_lvender(vendor)
        self.main_window.config.set_ldevice(model)
        self.main_window.config.set_lcount(count)

        self.close()

    def set_show(self, show_with_load_old_setting: bool):
        if show_with_load_old_setting:
            self.set_model(Settings.get_model())
            self.set_vender(Settings.get_vender())
            self.set_lot_count(str(Settings.get_lot_count()))
        else:
            old_vender = self.main_window.config.get_lvendor()
            old_dname = self.main_window.config.get_ldevice()
            old_count = self.main_window.config.get_lcount()

            if len(old_dname) > 0:
                self.set_model(old_dname)
            if len(old_vender) > 0:
                self.set_vender(old_vender)
            if len(old_count) > 0:
                self.set_lot_count(old_count)

        self.show()

    def set_default(self):
        self.ui.lineEdit_vendor.setText('-')
        self.ui.lineEdit_model.setText('-')
        self.ui.lineEdit_lot_count.setText('1200')

    def get_sns(self) -> str:
        return self.ui.comboBox.currentText()

    def get_model(self) -> str:
        return self.ui.lineEdit_model.text()

    def get_vender(self) -> str:
        return self.ui.lineEdit_vendor.text()

    def get_lot_count(self) -> str:
        return self.ui.lineEdit_lot_count.text()

    def set_model(self, text: str) -> None:
        self.ui.lineEdit_model.setText(text)

    def set_vender(self, text: str) -> None:
        self.ui.lineEdit_vendor.setText(text)

    def set_lot_count(self, text: str) -> None:
        self.ui.lineEdit_lot_count.setText(text)

    def closeEvent(self, event):
        if self.main_window.first_load:
            self.main_window.set_close()


class InputBuffer:
    current_checked_count = 0
    max_checked_count = 0
    checked_string = ""

    @classmethod
    def set_comare(cls, compared_sn: str) -> COMPARED_RESULT:
        if not cls.is_in_compare():  # не выполнялось
            cls.checked_string = compared_sn
            cls.current_checked_count = 1
            return COMPARED_RESULT.COMPARED_IS_SUCCESS_PROGRESS
        else:  # сравнение уже выполняется
            if cls.checked_string != compared_sn:
                cls.clear()
                return COMPARED_RESULT.COMPARED_FAIL
            else:
                cls.current_checked_count += 1
                if cls.current_checked_count >= cls.max_checked_count:
                    cls.clear()
                    return COMPARED_RESULT.COMPARED_SUCCESS
                else:
                    return COMPARED_RESULT.COMPARED_IS_SUCCESS_PROGRESS

    @classmethod
    def clear(cls):
        cls.current_checked_count = 0
        cls.checked_string = ""

    @classmethod
    def set_max_checked(cls, count: int):
        cls.max_checked_count = count

    @classmethod
    def is_in_compare(cls) -> bool:
        return True if cls.checked_string != "" else False

    @classmethod
    def get_compare_string(cls) -> str:
        return cls.checked_string


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
