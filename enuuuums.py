from enum import IntEnum, auto


class SMBOX_ICON_TYPE(IntEnum):
    ICON_NONE = auto(),
    ICON_WARNING = auto(),
    ICON_ERROR = auto(),
    ICON_INFO = auto()


class COMPARED_RESULT(IntEnum):
    COMPARED_NONE = auto(),
    COMPARED_FAIL = auto(),
    COMPARED_IS_SUCCESS_PROGRESS = auto(),
    COMPARED_SUCCESS = auto(),
