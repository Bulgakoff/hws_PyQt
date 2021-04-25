# from tracker1 import *
#
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# ui.label.setText('sdfsjdfhioafASHGDSHHDS')
#
# sys.exit(app.exec_())
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from icecream import ic
import pickle

import os

ic(os.path.realpath(__file__))
dirname, filename = os.path.split(os.path.realpath(__file__))
ic(os.path)
ic(filename)
ic(dirname)
Form, Window = uic.loadUiType(dirname + "\\tracker1.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def save_to_file():
    global start_date, calc_date, descrip, dirname
    start_date = QDate(2021, 4, 1)
    data_to_save = {"start": start_date, "end": calc_date, "desc": descrip}
    with open(dirname + "\\config.txt", "wb") as file1:
        pickle.dump(data_to_save, file1)
    task = """schtasks /create /tr "python""" + os.path.realpath(
        __file__) + """" /tn "Трекер события" /sc MINUTE /mo 60 /ed """ + calc_date.toString("dd/MM/yyyy") + """ /F"""
    ic(task)
    os.system('chcp 1251')
    os.system(task)


def read_from_file():
    global start_date, calc_date, descrip, current_date, dirname
    try:
        with open(dirname + "\\config.txt", "rb") as file1:
            data_to_load = pickle.load(file1)
        # file1.close()
        start_date = data_to_load["start"]
        calc_date = data_to_load["end"]
        descrip = data_to_load["desc"]
        print(
            start_date.toString("dd-MM-yyyy"), calc_date.toString("dd-MM-yyyy"), descrip
        )
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainText(descrip)
        delta_days_left = start_date.daysTo(current_date)  # прошло дней
        delta_days_right = current_date.daysTo(calc_date)  # осталось дней
        days_total = start_date.daysTo(calc_date)  # ДНЕЙ ОТ НАЧАОА
        print(f'====> {delta_days_left} -'
              f' - {delta_days_right} === {days_total}')
        procent = int(delta_days_left * 100 / days_total)
        ic(procent)
        form.progressBar.setProperty("value", procent)
    except:
        print("нет файла ")

    # pass


def on_click():
    global calc_date, descrip, start_date
    start_date = current_date
    # start_date = form.calendarWidget.selectedDate()
    calc_date = form.calendarWidget.selectedDate()
    descrip = form.plainTextEdit.toPlainText()
    # ic(form.plainTextEdit.toPlainText())
    # ic(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    ic("Кликнули кнопку")
    # ic(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    # date = QDate(2021,2,25)
    # form.calendarWidget.setSelectedDate(date)
    save_to_file()


def on_click_cal():
    global start_date, calc_date
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'))
    form.dateEdit.setDate(form.calendarWidget.selectedDate())

    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    print(f" до события осталось {delta_days} дней")
    form.label_3.setText(f"до события осталось  {delta_days} дней(я)")
    # form.label.setText(f'до события осталось  {delta_days} дней(я)')


def on_date_changed():
    global start_date, calc_date
    # ic(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    date = QDate(form.dateEdit.date())
    form.calendarWidget.setSelectedDate(date)

    calc_date = date
    delta_days = start_date.daysTo(calc_date)
    print(f" до события осталось {delta_days} дней")
    form.label_3.setText(f"до события осталось  {delta_days} дней(я)")
    # pass


form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_cal)
form.dateEdit.dateChanged.connect(on_date_changed)  # в виджете
# dateEdit по событию (сигналу ) dateChanged привязываем к функции
# on_date_changed
# после вызова функции выше нижние пееременные пресчетаются
start_date = form.calendarWidget.selectedDate()
current_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()
descrip = form.plainTextEdit.toPlainText()
read_from_file()

form.label.setText(f"{start_date.toString('dd-MM-yyyy')}")

on_click_cal()

app.exec()
