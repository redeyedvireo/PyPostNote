import configparser
import logging
import os.path
from pathlib import Path


class EDoubleClickAction:
  eDCACreateSmallNote = 0
  eDCACreateMediumNote = 1
  eDCACreateLargeNote = 2
  eDCACreateExtraLargeNote = 3
  eDCAQuickCreateDialog = 4
  eDCAShowAllNotes = 5

kGeneralSection = 'general'

kPrefAutoSaveMinutes = 'autoSaveMinutes'
kPrefDoubleClickAction = 'doubleClickAction'
kPrefAutoShutdownEnabled = 'autoShutdownEnabled'
kPrefAutoShutdownTime = 'autoShutdownTime'
kPrefDefaultFontFamily = 'defaultFontFamily'
kPrefDefaultFontSize = 'defaultFontSize'

kDefaultAutoSaveMinutes = 10
kDefaultAutoShutdownTime = '12:00'
kDefaultFontFamily = 'Arial'
kDefaultFontSize = 10

class Preferences:
  def __init__(self):
    self.prefsPath = ''

    self.autoSaveMinutes = kDefaultAutoSaveMinutes
    self.doubleClickAction = EDoubleClickAction.eDCACreateMediumNote
    self.autoShutdownEnabled = False
    self.autoShutdownTime = kDefaultAutoShutdownTime

    self.defaultFontFamily = kDefaultFontFamily
    self.defaultFontSize = kDefaultFontSize

  def readPrefsFile(self, preferencesPath: str):
    """ Reads the prefs from the prefs INI file. """
    self.prefsPath = preferencesPath
    configObj = configparser.ConfigParser()

    if not os.path.exists(self.prefsPath):
      # The prefs file does not exist.  Create it with app defaults
      self.writePrefsFile()
    else:
      try:
        configObj.read(self.prefsPath)

        self.autoSaveMinutes = configObj.getint(kGeneralSection, kPrefAutoSaveMinutes, fallback=kDefaultAutoSaveMinutes)
        self.doubleClickAction = configObj.getint(kGeneralSection, kPrefDoubleClickAction, fallback=int(EDoubleClickAction.eDCACreateMediumNote))
        self.autoShutdownEnabled = configObj.getboolean(kGeneralSection, kPrefAutoShutdownEnabled, fallback=False)
        self.autoShutdownTime = configObj.get(kGeneralSection, kPrefAutoShutdownTime, fallback=kDefaultAutoShutdownTime)
        self.defaultFontFamily = configObj.get(kGeneralSection, kPrefDefaultFontFamily, fallback=kDefaultFontFamily)
        self.defaultFontSize = configObj.getint(kGeneralSection, kPrefDefaultFontSize, fallback=kDefaultFontSize)

      except Exception as inst:
        errMsg = "Exception: {}".format(inst)
        logging.error(f'[readPrefsFile] {errMsg}')

  def writePrefsFile(self):
    configObj = configparser.ConfigParser()

    try:
      if not configObj.has_section(kGeneralSection):
        # The section must be created before data can be stored in it
        configObj[kGeneralSection] = {}

      configObj[kGeneralSection][kPrefAutoSaveMinutes] = str(self.autoSaveMinutes)
      configObj[kGeneralSection][kPrefDoubleClickAction] = str(self.doubleClickAction)
      configObj[kGeneralSection][kPrefAutoShutdownEnabled] = str(self.autoShutdownEnabled)
      configObj[kGeneralSection][kPrefAutoShutdownTime] = str(self.autoShutdownTime)
      configObj[kGeneralSection][kPrefDefaultFontFamily] = str(self.defaultFontFamily)
      configObj[kGeneralSection][kPrefDefaultFontSize] = str(self.defaultFontSize)

      # Make sure the directory exists
      directory = os.path.dirname(self.prefsPath)
      path = Path(directory)
      if not path.exists():
        try:
          path.mkdir(parents=True)
        except Exception as inst:
          errMsg = f"Error creating prefs directory: {inst}"
          logging.error(f'[writePrefsFile] {errMsg}')
          return

      with open(self.prefsPath, 'w') as configFile:
        configObj.write(configFile)

    except Exception as inst:
      errMsg = "Writing prefs file: {}".format(inst)
      logging.error(f'[writePrefsFile] {errMsg}')
