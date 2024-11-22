import sys
import os.path
from pathlib import Path
import platform

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