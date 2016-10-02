
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

from . import Components

def GetPluginMenu():
    menu = Components.Menu('Plugins')
    if not menu:
        mb = Components.MenuBar()
        menu = mb.addMenu('&Plugins')

    return menu

"""
    Add a Plugin sub-menu. The 'tree' map should
    be setup as so:

    {
        'menu-item1' : function,
        'menu-item2' : {
            'sub-menu-item1' : function
        },
        ...
    }

    It will be added to a top-level 'Plugin' menu,
    unless you supply the 'menu' param, inwhich it
    will start adding from the menu it is given.

"""
def AddMenuTree(tree, menu=None):

    if not menu:
        menu = GetPluginMenu()

    for x in tree:
        if hasattr(tree[x], '__call__'):
            action = QtWidgets.QAction(x, menu)
            action.triggered.connect(tree[x])
            menu.addAction(action)

        else:
            m = menu.addMenu(x)
            AddMenuTree(tree[x], m)

"""
    Get the font that's being used for Binja.
    THIS IS SLOW.
"""
def GetFont():
    from . import _app
    return [x for x in _app().allWidgets() if x.metaObject().className() == 'FunctionList'][0].font()


_filters = {}

class Filter(QtCore.QObject):
    def __init__(self, parent = None):
        QtCore.QObject.__init__(self, parent)
        self.filters = []

    def addFilter(self, f):
        self.filters.append(f)

    def eventFilter(self, obj, evt):
        for filter_ in self.filters:
            if filter_(obj, evt):
                return True

        return False

"""

    Installs an event filter on an object, just needs
    a function like so:

    def myFuncFilter(obj, evt):
        # ...
        return True/False
    returns True if it consumed the event, and no other
    filters should process the event, and False if the
    event can continue to be processed.
"""

def InstallEventFilterOnObject(obj, evtFilter):
    if obj in _filters:
        _filters[obj].addFilter(evtFilter)
    else:
        _filters[obj] = Filter()
        _filters[obj].addFilter(evtFilter)
        obj.installEventFilter(_filters[obj])



