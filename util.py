import sys
import os.path
from pathlib import Path
import platform
import datetime
from struct import unpack_from
import logging
from PySide6 import QtCore, QtWidgets, QtGui

def getScriptPath():
  if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path, executable = os.path.split(sys.executable)
  else:
    application_path = os.path.dirname(os.path.abspath(__file__))

  return application_path

def getStorageDirectory(applicationName: str) -> str:
  """Returns the directory where the database (Notes.db) and preferences (PyPostNote.ini) files
  are stored.

  Args:
      applicationName (str): Application name.

  Returns:
      str: Directory where the database and preferences files are stored.
  """
  if platform.system() == 'Windows':
    # This attempts to use whatever directory is in the APPDATA environment variable, if it exists.
    # If the APPDATA environment variable doesn't exist, the application directory is used.
    directory = os.getenv('APPDATA', getScriptPath())
    return os.path.join(directory, applicationName)

  elif platform.system() == 'Linux':
    # On Linux, use "~/.PyPostNote"
    homeDirObj = Path.home()
    appDataDir = homeDirObj / f'.{applicationName}'
    return os.fspath(appDataDir)

  else:
    logging.error('The application data directory is currently only supported on Windows and Linux')
    return ''

def getDatabasePath(applicationName: str, databaseName: str) -> str:
  """Returns the complete path of the database.

  Returns:
      str: App data directory.
  """
  dataDirectory = getStorageDirectory(applicationName)
  return os.path.join(dataDirectory, databaseName)

def getPrefsPath(applicationName: str, prefsFileName: str) -> str:
  """ Returns the full path to the prefs file. """
  dataDirectory = getStorageDirectory(applicationName)
  return os.path.join(dataDirectory, prefsFileName)

def getStyleDefsPath(applicationName: str, styleDefsFileName: str) -> str:
  """ Returns the full path to the style definitions file. """
  dataDirectory = getStorageDirectory(applicationName)
  return os.path.join(dataDirectory, styleDefsFileName)

def copyQRect(src: QtCore.QRect) -> QtCore.QRect:
  """Makes a deep copy of a QRect.  Simply assigning one QRect to another one will not perform a
     copy; it will simply assign a reference, so that both rects point to the same QRect.

  Args:
      src (QtCore.QRect): QRect to copy
  """
  return QtCore.QRect(src.topLeft(), src.bottomRight())

def copyQSize(src: QtCore.QSize) -> QtCore.QSize:
  """Makes a deep copy of a QSize.  Simply assigning one QSize to another one will not perform a
     copy; it will simply assign a reference, so that both sizes point to the same QSize.

  Args:
      src (QtCore.QSize): QSize to copy

  Returns:
      QtCore.QSize: A deep copy of the QSize object.
  """
  return QtCore.QSize(src.width(), src.height())

def createTopicIcon(width: int, height: int, bgColor: QtGui.QColor, textColor: QtGui.QColor, text: str):
  tempPixmap = QtGui.QPixmap(width, height)

  tempPixmap.fill(bgColor)

  painter = QtGui.QPainter(tempPixmap)
  painter.setPen(textColor)
  painter.drawText(QtCore.QRect(0, 0, width, height), \
                    QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter, \
                    text)
  painter.end()

  return QtGui.QIcon(tempPixmap)

# Format date
def formatDateAndTime(inDate: datetime.date) -> str:
  return inDate.strftime("%a %b %d %Y   %I:%M %p")

def printGeometry(geometry: bytes):
  results = unpack_from('>IHHIIIIIIIIIBBI', geometry)
  # for index, item in enumerate(results):
  #   if index == 0:
  #     print(hex(item))
  #   else:
  #     print(item)

  def windowGeometry(x, y, x2, y2):
    width = x2 - x
    height = y2 - y
    return f'x: {x}, y: {y}, width: {width}, height: {height}'

  print(f'Magic Number: {hex(results[0])}')
  print(f'Major Version: {results[1]}')
  print(f'Minor Version: {results[2]}')
  # print(f'Frame Geometry: {results[3]}, {results[4]}, {results[5]}, {results[6]}')
  print(f'Frame Geometry: {windowGeometry(results[3], results[4], results[5], results[6])}')
  # print(f'Normal Geometry: {results[7]}, {results[8]}, {results[9]}, {results[10]}')
  print(f'Normal Geometry: {windowGeometry(results[7], results[8], results[9], results[10])}')
  print(f'Screen number: {results[11]}')
  print(f'Maximized: {results[12]}')
  print(f'FullScreen: {results[13]}')
  print(f'Screen width: {results[14]}')

def bytesToQByteArray(data: bytes) -> QtCore.QByteArray:
  return QtCore.QByteArray(data)
