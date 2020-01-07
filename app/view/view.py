import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine


class ELEMENTS_NAME:
    pass


class View(QQmlApplicationEngine):
    UI = "view/ui.qml"

    def __init__(self):
        super().__init__()
        super().load(QUrl(View.UI))
        self._ui = super().rootObjects()
        self._elements = {}

    def get_element(self, name: str):
        return self._elements[name]


if __name__ == "__main__":
    sys_argv = sys.argv
    sys_argv += ["--style", "material"]
    app = QApplication(sys_argv)
    view = View()

    app.exec()
