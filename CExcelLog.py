from openpyxl import Workbook, load_workbook
from openpyxl.utils.cell import get_column_interval
from openpyxl.styles import (
    Alignment, Font
)

import os
import logging
from datetime import datetime

from functions import send_message_box, SMBOX_ICON_TYPE

class CExcelLog:
    _full_patch = None
    _file_name = None
    _file_name_in_logging = None
    _on_day_folder_name = None
    _BASE_FOLDER_NAME = "sn_logging_folder"

    # СТИЛЬ ШРИФТА
    _FONT_HEADER = Font(
        name='Calibri',
        size=30,
        bold=True,
        italic=False,
        vertAlign=None,
        underline='none',
        strike=False,
        color='FF000000'
    )
    _FONT_DATA = Font(
        name='Arial',
        size=20,
        bold=False,
        italic=False,
        vertAlign=None,
        underline='none',
        strike=False,
        color='FF000000'
    )
    _alignment = Alignment(
        horizontal='center',
        vertical='center',
        text_rotation=0,
        wrap_text=False,
        shrink_to_fit=False,
        indent=0
    )

    @classmethod
    def print_log(cls, vender: str, model: str, sn: str) -> bool:
        current_time = datetime.now()

        if cls._on_day_folder_name is None:
            cls._on_day_folder_name = f"{current_time.day:02}_{current_time.month:02}_{current_time.year}"
            cls._file_name = f"scanned_log_{current_time.day:02}_{current_time.month:02}_{current_time.year}.xlsx"
            cls._full_patch = f"{cls._BASE_FOLDER_NAME}/{cls._on_day_folder_name}/{cls._file_name}"
            cls._file_name_in_logging = (f"{cls._BASE_FOLDER_NAME}/{cls._on_day_folder_name}/scanned_log_"
                                         f"{current_time.day:02}_{current_time.month:02}_{current_time.year}.log")
            # print(cls._on_day_folder_name)
            # print(cls._file_name)
            # print(cls._full_patch)

        logging.basicConfig(level=logging.INFO, filename=cls._file_name_in_logging, filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s")

        full_date = f'{current_time.day:02}.{current_time.month:02}.{current_time.year} ' \
                    f'{current_time.hour:02}:{current_time.minute:02}:{current_time.second:02}'

        try:
            if not os.path.isdir(cls._BASE_FOLDER_NAME):
                os.mkdir(cls._BASE_FOLDER_NAME + "/")

            if not os.path.isdir(f"{cls._BASE_FOLDER_NAME}/{cls._on_day_folder_name}"):
                os.mkdir(f"{cls._BASE_FOLDER_NAME}/{cls._on_day_folder_name}" + "/")

            if os.path.exists(cls._full_patch) is False:
                wb = Workbook()
                ws = wb.active
                ws.title = "Сканировка устройств"
                ws.append(("Дата сканировки:", "Vendor:", "Model:", "SN:"))

                # задаём ширину и фонт для шапки
                cell_range = ws['A1':'D1']
                for i in cell_range:
                    for i2 in i:
                        letter_adress = i2.coordinate

                        ws[letter_adress].font = cls._FONT_HEADER
                        ws[letter_adress].alignment = cls._alignment

                interval = get_column_interval("A", "D")
                for item in interval:
                    ws.column_dimensions[item].width = 60
            else:
                wb = load_workbook(cls._full_patch)
                ws = wb.active

            ws.append((full_date,
                       vender, model, sn))

            for cell in ws:  # Проходим по ячейкам последней добавленной строки
                for item in cell:
                    letter_adress = item.coordinate
                    ws[letter_adress].font = cls._FONT_DATA  # Применяем шрифт к каждой ячейке
                    ws[letter_adress].alignment = cls._alignment

            wb.save(cls._full_patch)
            wb.close()

        except Exception as err:
            logging.warning(f"SN SuccessFull Scanned: Vendor: {vender} | Model: {model} | SN: {sn}")
            send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_ERROR,
                             text=f"Не могу записать данные!\n\n"
                                  f"Ошибка: '{err}'",
                             title="Критическая ошибка",
                             variant_yes="Ок", variant_no="", callback=None)

            return False

        logging.info(f"SN SuccessFull Scanned: Vendor: {vender} | Model: {model} | SN: {sn}")

        return True
