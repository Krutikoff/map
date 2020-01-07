import sys
import PyQt5
from PyQt5 import QtCore

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

fileDialog = None

Engine = None

def ok_clicked():
    print("Ok")


def cancel_clicked():
    print("Cancel")


def file_load():
    print("file load")
    name = Engine.rootContext().contextProperty("path")
    
    if fileDialog is None:
        return

    name = "n"
    print(name)

def file_dialog(val):
    print(val)



if __name__ == "__main__":
    sys_argv = sys.argv
    sys_argv += ['--style', 'material']
    app = QApplication(sys_argv)
    engine = QQmlApplicationEngine()
    engine.load(QUrl("view/map.qml"))
    app.setOrganizationName("map")
    app.setOrganizationDomain("map")
    app.setApplicationName("map")
    root, *tail = engine.rootObjects()
    play_button = root.findChild(QtCore.QObject, "PlayButton")
    play_button.clicked.connect(ok_clicked)

    cancel_button = root.findChild(QtCore.QObject, "CancelButton")
    cancel_button.clicked.connect(cancel_clicked)

    file_load_button = root.findChild(QtCore.QObject, "FileLoadButton")
    file_load_button.clicked.connect(file_load)

    fileDialog = root.findChild(QtCore.QObject, "FileDialog")

    fileDialog.messageRequired.connect(file_dialog)

    aNumber = engine.rootContext().contextProperty("aNumber")
    name = engine.rootContext().contextProperty("path")
    Engine = engine

    app.exec()
