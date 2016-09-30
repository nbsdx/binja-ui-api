
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
