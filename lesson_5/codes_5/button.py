# ---------------- Графический интерфейс пользователя. PyQt5 ------------------
#                Приложение "Калькулятор". Класс цифровой кнопки


import sys
from PyQt5.QtWidgets import QSizePolicy, QToolButton


class Button(QToolButton):
    def __init__ (self, text, parent):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = QToolButton.sizeHint(self)
        h = size.height() + 20
        size.setHeight(h)
        size.width = max((size.width(), size.height()))
        return size



