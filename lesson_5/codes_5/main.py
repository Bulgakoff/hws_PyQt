# ---------------- Графический интерфейс пользователя. PyQt5 ------------------
#                 Приложение "Калькулятор". Запуск приложения 

import sys
from PyQt5.QtWidgets import QApplication

from calculator import Calculator

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
