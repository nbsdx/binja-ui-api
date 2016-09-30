
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from . import _app

def MainWindow():
    app = _app()

    return [x for x in app.allWidgets() if x.__class__ is QtWidgets.QMainWindow][0]

def MenuBar():
    app = _app()

    return [x for x in app.allWidgets() if x.__class__ is QtWidgets.QMenuBar][0]

"""
    TODO: If the menu you're looking for has a '&' in it,
    it will probably fail to find it. Also, if the '&' for
    the shortcut is not the first character, you're kinda
    SoL.
"""
def Menu(name):
    menubar = MenuBar()

    for x in menubar.children():
        if x.__class__ is QtWidgets.QMenu:
            if x.title().find(name) != -1:
                return x

    return None

def FunctionWindow():
    app = _app()

    views = [x for x in app.allWidgets() if x.__class__ is QtWidgets.QListView]

    for view in views:
        if view.parent().__class__ is QtWidgets.QWidget:
            if view.parent().parent().__class__ is QtWidgets.QSplitter:
                return view.parent()

    return None

def TabWidget():
    app = _app()

    views = [x for x in app.allWidgets() if x.__class__ is QtWidgets.QListView]

    for view in views:
        if view.parent().__class__ is QtWidgets.QStackedWidget:
            if view.parent().parent().__class__ is QtWidgets.QTabWidget:
                return view.parent().parent()

    return None
