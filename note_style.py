from enum import Enum
from PySide6 import QtCore, QtWidgets, QtGui

class ENoteBackground(Enum):
  eSolid = 0
  eColorCycling = 1

  # To be implemented in the future
  # eGradient,
  # eImage,
  # eVideo

class NoteStyle:
  def __init__(self):
    # Some defaults
    self.backgroundColor = QtGui.QColor("yellow")
    self.textColor = QtGui.QColor("black")
    self.backgroundType = ENoteBackground.eSolid
    self.transparency = 100
