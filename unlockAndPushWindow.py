import wx

"""from Lock import *
from Unlock import *
from Try_and_lock import  *"""

from blankFunc import *
import unlockAndPushWindowGui

class unlockAndPushWindow( unlockAndPushWindowGui.unlockAndPushWindowGui ):
    def __init__( self, parent, items, direction ):
        unlockAndPushWindowGui.unlockAndPushWindowGui.__init__( self, parent )
        index = self.checkList.InsertItems(items, 0)
        self.numFiles = len(items)
        self.listFiles = items
        self.selectFlag = 1
        self.dirPath = direction
        i = 0
        while i < self.numFiles:
            self.checkList.Check(i, True)
            i = i + 1
    selectFlag = 1
    showUnversionedFlag = 1
    numFiles = 0
    dirPath = " "
    listFiles = []

    def selectDeselectAllFunc( self, event ):
        i = 0
        if self.selectFlag == 0:
            #i = 0
            self.selectFlag = 1
            while i < self.numFiles:
                self.checkList.Check(i, True)
                i = i + 1
        elif self.selectFlag == 1:
            self.selectFlag = 0
            while i < self.numFiles:
                self.checkList.Check(i, False)
                i = i + 1

    def showUnversionedFunc( self, event ):
        i = 0
        if self.showUnversionedFlag == 0:
            self.showUnversionedFlag = 1
            while i < self.numFiles:
                if "unversioned" in self.listFiles[i]:
                    self.checkList.InsertItems([self.listFiles[i]], i)
                i = i + 1
        elif self.showUnversionedFlag == 1:
            self.showUnversionedFlag = 0
            while i < self.numFiles:
                if "unversioned" in self.listFiles[i]:
                    self.checkList.Delete(i)
                i = i + 1

    def okClickFunc( self, event ):
        i = 0
        selectedFiles = []
        while i < self.numFiles:
            if self.checkList.IsChecked(i):
                selectedFiles.append(self.listFiles[i])
            i = i + 1

        Push(self.dirPath, selectedFiles, self.commentBox.GetValue())
        UnlockFiles(selectedFiles)

        msg = "Unlock and Push complete!"
        dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Message", style=wx.OK|wx.ICON_INFORMATION)
        result = dlg.ShowModal()

    def cancelClickFunc( self, event ):
        self.Close()

