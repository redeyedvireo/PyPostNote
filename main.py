from PySide6 import QtCore, QtWidgets, QtGui
import sys
import os.path
import logging
from logging.handlers import RotatingFileHandler
from preferences import Preferences
from style_manager import StyleManager
from util import getScriptPath
from postnote import PostNoteWindow
from database import Database
from topic_manager import TopicManager
from note_manager import NoteManager

kLogFile = 'PyPostNote.log'
kMaxLogileSize = 1024 * 1024

def shutdownApp():
  logging.info("Shutting down...")
  logging.shutdown()

def getLogfilePath():
  return os.path.join(getScriptPath(), kLogFile)

def main(debug: bool):
  """Main entry point.

  Args:
      debug (bool): If True, the app will run in debug mode.  In this case,
                    the database will be named NotesDebug.db.
  """
  console = logging.StreamHandler()
  rotatingFileHandler = RotatingFileHandler(getLogfilePath(), maxBytes=kMaxLogileSize, backupCount=9)
  logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                          handlers=[ rotatingFileHandler, console ])

  app = QtWidgets.QApplication([])

  logging.info("PyPostNote starting up...")

  QtWidgets.QApplication.setQuitOnLastWindowClosed(False)

  preferences = Preferences()
  database = Database()
  topicManager = TopicManager()
  styleManager = StyleManager()
  noteManager = NoteManager(database, topicManager, styleManager, preferences)
  window = PostNoteWindow(database, noteManager, topicManager, styleManager, preferences, debug)

  window.initialize()

  # Don't want  to show the window
  # window.hide()

  returnValue = app.exec()

  database.closeDatabase()
  shutdownApp()

  sys.exit(returnValue)

# ---------------------------------------------------------------
if __name__ == "__main__":
  debug = False
  for arg in sys.argv:
    if arg == 'debug':
      debug = True
      break

  main(debug)