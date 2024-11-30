from PySide6 import QtCore, QtWidgets, QtGui
from ui_button_bar_widget import Ui_ButtonBarWidget
from util import copyQRect

kHideInterval = 1500
kGrowWaitTime =	100
kAnimateInterval = 200

class ButtonBarWidget(QtWidgets.QWidget):
  def __init__(self, textEditRect: QtCore.QRect, parent: QtWidgets.QWidget):
    super(ButtonBarWidget, self).__init__(parent)

    self.ui = Ui_ButtonBarWidget()
    self.ui.setupUi(self)

    self.initialSize = QtCore.QSize()     # Initially is invalid
    self.positionWidget(textEditRect)

    self.setMouseTracking(True)

    # The grow start timer is used to provide a brief delay before starting the grow process.
    # This is to prevent the bar from starting to grow while the cursor is being dragged around the screen.
    self.growStartTimer = QtCore.QTimer()
    self.growStartTimer.setSingleShot(True)
    self.growStartTimer.setInterval(kGrowWaitTime)
    self.growStartTimer.timeout.connect(self.onGrowWaitTimeout)

    # The hide timer initiates hiding after a period of time of inactivity
    self.hideTimer = QtCore.QTimer()
    self.hideTimer.setSingleShot(True)
    self.hideTimer.setInterval(kHideInterval)
    self.hideTimer.timeout.connect(self.onTimerTimeout)

    # Create animators
    self.shrinkAnimator = QtCore.QPropertyAnimation(self, b'geometry')
    self.shrinkAnimator.setDuration(kAnimateInterval)
    self.shrinkAnimator.finished.connect(self.onShrinkFinished)

    self.growAnimator = QtCore.QPropertyAnimation(self, b'geometry')
    self.growAnimator.setDuration(kAnimateInterval)
    self.growAnimator.finished.connect(self.onGrowFinished)
    
  def enterEvent(self, event: QtCore.QEvent):
    if self.isBarShrunk():
      # The bar is hidden.  Go ahead and grow it, after a brief waiting period.
      self.growStartTimer.start()

  def leaveEvent(self, event: QtCore.QEvent):
    if self.growAnimator.state() == QtCore.QAbstractAnimation.State.Running:
      # The bar is in the process of being grown, but has not finished.  In this case,
      # stop the animation and return the bar to its shrunk state.
      self.growAnimator.stop()
      self.shrinkButtonBar()

    if self.isBarGrown():
      # The bar is shown.  Go ahead and hide it.
      self.shrinkButtonBar()

  def setTopicMenu(self, menu: QtWidgets.QMenu):
    self.ui.topicButton.setMenu(menu)
    
  def positionWidget(self, textEditRect: QtCore.QRect):
    if not self.initialSize.isValid():
      self.initialSize = self.size()

    barSize = self.initialSize

    kBorder = 5

    self.grownButtonBarRect = copyQRect(textEditRect)

    self.grownButtonBarRect.setTop(textEditRect.top())
    self.grownButtonBarRect.setLeft(textEditRect.left() + kBorder)
    self.grownButtonBarRect.setRight(textEditRect.right() - kBorder)
    self.grownButtonBarRect.setBottom(textEditRect.top() + barSize.height())

    self.move(self.grownButtonBarRect.topLeft())

    # Shrunk rectangle
    self.shrunkButtonBarRect = copyQRect(self.grownButtonBarRect)
    self.shrunkButtonBarRect.setBottom(self.shrunkButtonBarRect.top() + 5)

    # Size it to fit within the width of the note
    barSize.setWidth(self.grownButtonBarRect.width())
    barSize.setHeight(5)

    self.resize(barSize)

    self.hideWidgets()
    self.show()
    self.raise_()
    self.activateWindow()

  def hideWidgets(self):
    self.ui.deleteButton.hide()
    self.ui.propertiesButton.hide()

  def showWidgets(self):
    self.ui.deleteButton.show()
    self.ui.propertiesButton.show()    

  def onGrowWaitTimeout(self):
    # If the mouse is still within the widget, go ahead and grow the bar
    if self.isMouseInWidget():
      self.growButtonBar()

  def isMouseInWidget(self):
    mousePos = QtGui.QCursor.pos()
    widgetRect = self.rect()
    
    ul = widgetRect.topLeft()
    lr = widgetRect.bottomRight()

    ulGlobal = self.mapToGlobal(ul)
    lrGlobal = self.mapToGlobal(lr)

    widgetRectGlobal = QtCore.QRect()
    widgetRectGlobal.setTopLeft(ulGlobal)
    widgetRectGlobal.setBottomRight(lrGlobal)
    
    return widgetRectGlobal.contains(mousePos)

  def isBarGrown(self):
    return self.size().height() >= self.grownButtonBarRect.height()

  def isBarShrunk(self):
    return self.size().height() <= self.shrunkButtonBarRect.height()

  def growButtonBar(self):
    # self.growAnimator.setStartValue(self.shrunkButtonBarRect)
    self.growAnimator.setEndValue(self.grownButtonBarRect)

    self.showWidgets()
    self.growAnimator.start()

  def shrinkButtonBar(self):
    # self.shrinkAnimator.setStartValue(self.grownButtonBarRect)
    self.shrinkAnimator.setEndValue(self.shrunkButtonBarRect)

    self.shrinkAnimator.start()

  def onTimerTimeout(self):
    if not self.isMouseInWidget():
      self.shrinkButtonBar()
    else:
      # The mouse cursor is over top of the widget.  Don't hide, but
      # restart the hide timer.
      self.hideTimer.start()

  def onShrinkFinished(self):
    self.hideWidgets()

  def onGrowFinished(self):
    pass      # Do nothing?

  # ******************** SLOTS ********************

  @QtCore.Slot()
  def on_deleteButton_clicked(self):
    print('Delete button clicked')

  @QtCore.Slot()
  def on_hideButton_clicked(self):
    print('Hide button clicked')

  @QtCore.Slot()
  def on_propertiesButton_clicked(self):
    print('Properties button clicked')

  @QtCore.Slot()
  def on_topicButton_clicked(self):
    print('Topic button clicked')