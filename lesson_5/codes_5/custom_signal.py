from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot


class AddUserDialog(QtWidgets.QWidget):
    fill_progress = pyqtSignal(int)

    def __init__(self, user_adder):
        super().__init__()
        self._user_adder = user_adder
        # init ui

        self.fill_progress.connect(self.fill_progress_bar.setValue)
        self.user_name_edit.textChanged.connect(self.on_user_name_changed)
        self.password_edit.textChanged.connect(self.on_user_name_changed)
        self.ok_btn.clicked.connect(self.on_submit)

    def on_user_name_changed(self):
        progress += 1
        self.fill_progress.emit(progress)
        self.validate()

    def on_password_changed(self):
        self.validate()

    def validate(self):
        pass

    def on_submit(self):
        self._user_adder.add_user(user_name, password)


class Storage:
    def __init__(self, dlg) -> None:
        self._dlg = dlg
        dlg.btn.clicked.connect(self.add_user)

    def add_user(self, user_name, ...):
        pass
