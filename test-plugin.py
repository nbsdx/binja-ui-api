
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

import BinjaUI as ui
from BinjaUI import Util, Components


# Let's add another tab next to the Xrefs panel!
# This is complicated, because we have to make sure
# that our new widget is constructed in the main
# GUI thread, otherwise the Widget will display
# outside the QMainWindow....

# ALSO, we need to have a binary open so we can be
# in the correct state.... We can delay injecting
# our components by adding an actiont to the plugin
# menu ;)

def setupUI():
    def CreateNewTab():
        def onClick():
            print "New UI Button Pressed :D"

        button = QtWidgets.QPushButton("Press Me!")
        button.released.connect(onClick)

        tw = Components.TabWidget()
        tw.addTab(button, "New!")

        return button

    wi = ui.WidgetInjector(CreateNewTab)
    wi.inject()

"""
    Add our setup function to the plugins menu
"""
ui.Util.AddMenuTree( {'Add New Tab' : setupUI} )

def foo():
    print "Foo"

def bar():
    print "Bar"

"""
    Add a silly menu tree as an example
"""
Util.AddMenuTree( {
    "Example Menu" : {
        "Inner1" : foo,
        "Inner2" : {
            "Last" : bar
            }
        }
    } )

print "Test Plugin Done Loading"
