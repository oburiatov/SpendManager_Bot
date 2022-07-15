from enum import Enum

token = "<your_token_here>"
db_file = "../db/database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_EXPENSE_NAME = "1"
    S_ENTER_EXPENSE_VALUE = "2"
    S_ENTER_EXPENSE_HASHTAG = "3"
    S_SEND_PIC = "4"
