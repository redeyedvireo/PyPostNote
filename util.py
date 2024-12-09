import sys
import os.path
from pathlib import Path
import platform
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

def getDatabasePath(applicationName: str, databaseName: str) -> str:
  """Returns the complete path of the database.

  Returns:
      str: App data directory.
  """
  if platform.system() == 'Windows':
    # This attempts to use whatever directory is in the APPDATA environment variable, if it exists.
    # If the APPDATA environment variable doesn't exist, the application directory is used.
    directory = os.getenv('APPDATA', getScriptPath())
    return os.path.join(directory, applicationName, databaseName)

  elif platform.system() == 'Linux':
    # On Linux, use "~/.PyPostNote/Notes.db"
    homeDirObj = Path.home()
    appDataDir = homeDirObj / f'.{applicationName}' / databaseName
    return os.fspath(appDataDir)

  else:
    print('The application data directory is currently only supported on Windows and Linux')
    return ''

def getPrefsPath(applicationName: str, prefsFileName: str) -> str:
  """ Returns the full path to the prefs file. """
  if platform.system() == 'Windows':
    # This attempts to use whatever directory is in the APPDATA environment variable, if it exists.
    # If the APPDATA environment variable doesn't exist, the application directory is used.
    directory = os.getenv('APPDATA', getScriptPath())
    return os.path.join(directory, applicationName, prefsFileName)

  elif platform.system() == 'Linux':
    # On Linux, use "~/.PyPostNote/PyPostNote.ini"
    homeDirObj = Path.home()
    appDataDir = homeDirObj / f'.{applicationName}' / prefsFileName
    return os.fspath(appDataDir)

  else:
    print('The application data directory is currently only supported on Windows and Linux')
    return ''

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
