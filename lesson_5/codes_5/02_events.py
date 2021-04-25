import sys
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from pyqt5_helper import setup_plugin_path


class NewChatMsgEvent(QtCore.QEvent):
    def __init__(self, from_user, msg, tm):
        super().__init__(QtCore.QEvent.User)
        self._from_user = from_user
        self._msg = msg
        self._tm = tm


class DisconnectedFromServerEvent(QtCore.QEvent):
    def __init__(self):
        super().__init__(QtCore.QEvent.User)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def event(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            print("Нажата клавиша на клавиатуре")
            print("Код:", e.key(), ", текст:", e.text())
        elif e.type() == QtCore.QEvent.Close:
            print("Окно закрыто")
        elif e.type() == QtCore.QEvent.MouseButtonPress:
            print("Клик мышью. Координаты:", e.x(), e.y())

        # Событие отправляется дальше
        return super().event(e)


class EventHandler(QtCore.QObject):
    def event(self, e) -> bool:
        if e.type() == QtCore.QEvent.User:
            if isinstance(e, DisconnectedFromServerEvent):
                print(f"Disconnect event")
            elif isinstance(e, NewChatMsgEvent):
                pass
        return super().event(e)


class UiNotifier:
    def __init__(self, app, handler) -> None:
        self._app = app
        self._handler = handler

    def notify_disconnect(self):
        self._app.postEvent(self._handler, DisconnectedFromServerEvent())

    def notify_new_chat_msg(self, from_user, msg, tm):
        self._app.postEvent(self._handler, NewChatMsgEvent(from_user, msg, tm))


def mainloop(app, handler):
    time.sleep(3)
    app.postEvent(handler, DisconnectedFromServerEvent())


if __name__ == "__main__":
    setup_plugin_path()
    app = QtWidgets.QApplication(sys.argv)
    handler = EventHandler()
    window = MyWindow()
    window.show()

    thr = threading.Thread(target=mainloop, args=(app, handler))
    thr.start()

    app.exec_()
    thr.join()
