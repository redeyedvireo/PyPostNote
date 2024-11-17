from PySide6 import QtCore, QtWidgets, QtGui
import sys
import os.path
import logging
from logging.handlers import RotatingFileHandler
from util import getScriptPath
from postnote import PostNoteWindow

kLogFile = 'PyPostNote.log'
kMaxLogileSize = 1024 * 1024

def shutdownApp():
  logging.info("Shutting down...")
  logging.shutdown()

def getLogfilePath():
  return os.path.join(getScriptPath(), kLogFile)

def main():
  console = logging.StreamHandler()
  rotatingFileHandler = RotatingFileHandler(getLogfilePath(), maxBytes=kMaxLogileSize, backupCount=9)
  logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                          handlers=[ rotatingFileHandler, console ])

  app = QtWidgets.QApplication([])

  logging.info("PyPostNote startig up...")

  window = PostNoteWindow()
  window.initialize()

  # TODO: Eventually, don't want  to show the window
  # window.hide()
  window.show()

  returnValue = app.exec()
  shutdownApp()

  sys.exit(returnValue)

# ---------------------------------------------------------------
if __name__ == "__main__":
  main()