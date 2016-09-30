
from PyQt5 import QtWidgets, QtCore, QtGui

def _app():
    return QtWidgets.QApplication.instance()

from . import Components

class WidgetInjector(QtCore.QObject):

    def __init__(self, func):
        QtCore.QObject.__init__(self)
        self.widget_func = func
        self.widget = None
        self.injected = False
        self.tc_count = 0

    def event(self, evt):
        print "Got Event [Thread: {}]".format(self.thread())

        if (evt.type() == QtCore.QEvent.ThreadChange) and not self.injected:
            self.tc_count = self.tc_count + 1
            if self.tc_count == 2:
                print "User event"
                self.widget = self.widget_func()
                self.injected = True
                return True

        return False

    def inject(self):
        guiThread = Components.MainWindow().thread()

        # If we're not in the GUI thread, we need to move to it
        if not (guiThread == self.thread()):
            self.moveToThread(guiThread)
            _app().postEvent(self, QtCore.QEvent(QtCore.QEvent.ThreadChange))

        # We're good to go - the GUI thread and this are the same.
        else:
            self.widget = self.widget_func()
            self.injected = True
