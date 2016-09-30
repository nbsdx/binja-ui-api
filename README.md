# binja-ui-api
Set of API calls to interact with the Binary Ninja UI

Handful of APIs to mess with Binary Ninja's UI (Qt5). 

##**YOU MUST HAVE PyQt5 INSTALLED TO USE THIS API**

### Examples:

Add a new Menu tree to a 'Plugins' menu.

```python
import BinjaUI as ui

def foo():
  print "foo"

def bar():
  print "bar"

ui.Util.AddMenuTree( {
  "MyPlugin": {
    "Foo" : foo,
    "Bar" : bar
   }
} );
```

Create a new tab (next to the XRefs tab)
```python
import BinjaUI as ui
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

def injectTab():
  """
  We need to actually create our new Widgets in this function.
  If widgets are created outside of the GUI thread, bad things
  happen. The WidgetInjector class ensures that the widget is
  constructed in the GUI thread, so you just need to pass a
  function to WidgetInjector that will create and return your
  new Widget.
  """
  def CreateNewTab():
    def onClick():
      print "New Button :D"

    button = QtWidgets.QPushButton("Press Me!")
    button.released.connect(onClick)

    tw = ui.Components.TabWidget()
    tw.addTab(button, "New!")

    return button
  
  injector = ui.WidgetInjector(CreateNewTab)
  # Do the injection
  injector.inject()

# Could also be bn.PluginCommand.... if you need the current view
Util.AddMenuTree( {"Add New Tab" : injectTab} )
