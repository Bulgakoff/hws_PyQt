# ---------------- Графический интерфейс пользователя. PyQt5 ------------------
#                              Unit-тестирование 
import sys
import pytest
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from calculator import Calculator
from button import Button

# Объект приложения нужно создать обязательно
app = QApplication(sys.argv)

# Тестируемую GUI-форму тоже нужно создать, но можно не показывать
calc = Calculator()


# Модуль PyQt5.QtTest предоставляет класс QTest, 
# содержащий методы для эмуляции нажатия клавиш клавиатуры и кликов мышью. 
# Обратите внимание, данный класс реализует не все методы оригинального QTest библиотеки Qt. 

# Документация: http://doc.qt.io/qt-5/QTest.html

# Основные функции:
#  keyClick, keyClicks, keyEvent, keyPress, keyRelease, mouseClick, mouseDClick, 
#  mouseEvent, mouseMove, mousePress, mouseRelease, qSleep, qWait, qWaitForWindowActive, 
#  qWaitForWindowExposed, touchEvent, waitForEvents


def click_button_with_label(widget, label):
    ''' Клик на кнопке с нужной меткой '''
    if isinstance(widget, Button) and widget.text() == label:
        QTest.mouseClick(widget, Qt.LeftButton)


def click_digit(form, label):
    ''' Клик на цифровой кнопке '''
    for widget in form.digitButtons:
        click_button_with_label(widget, label)


def click(form, label):
    ''' Клик на обычной кнопке '''
    for name, widget in form.__dict__.items():
        click_button_with_label(widget, label)


@pytest.fixture(autouse=True)
def clear_all():
    ''' Фикстура для сброса калькулятора. 
        Для выполнения между тестами
    '''
    calc.clearAll()


def test_summ():
    ''' Простой тест функции сложения '''
    click_digit(calc, '5')
    click(calc, '+')
    click_digit(calc, '7')
    click(calc, '=')
    assert calc.display.text() == '12.0'


def test_read_only_display():
    ''' Тест заблокированного ввода в окно дисплея (ReadOnly = True) '''
    QTest.keyClicks(calc.display, "3.5")
    assert calc.display.text() == '0'
