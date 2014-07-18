import wx
import undoChangesWindowGui
from blankFunc import *

class undoChangesWindow( undoChangesWindowGui.undoChangesWindowGui ):
    def __init__( self, parent, items, direction ):
        undoChangesWindowGui.undoChangesWindowGui.__init__( self, parent )
        index = self.checkList.InsertItems(items, 0)
        self.numFiles = len(items)
        i = 0
        numDelete = 0
        while i < self.numFiles:
            if "unversioned" in items[i]:
                self.checkList.Delete(i)
                numDelete += 1
            i = i + 1

        self.numFiles = self.numFiles - numDelete
        self.listFiles = items
        self.selectFlag = 1
        self.dirPath = direction
        i = 0
        while i < self.numFiles:
            self.checkList.Check(i, True)
            i = i + 1
    selectFlag = 1
    numFiles = 0
    dirPath = " "
    listFiles = []

    def selectDeselectAllFunc( self, event ):
        i = 0
        if self.selectFlag == 0:
            self.selectFlag = 1
            while i < self.numFiles:
                self.checkList.Check(i, True)
                i = i + 1
        elif self.selectFlag == 1:
            self.selectFlag = 0
            while i < self.numFiles:
                self.checkList.Check(i, False)
                i = i + 1

    def okClickFunc( self, event ):
        i = 0
        selectedFiles = []
        while i < self.numFiles:
            if self.checkList.IsChecked(i):
                selectedFiles.append(self.listFiles[i])
            i = i + 1

        Undo(self.dirPath, selectedFiles)

        msg = "Undo changes complete!"
        dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Message", style=wx.OK|wx.ICON_INFORMATION)
        result = dlg.ShowModal()

    def cancelClickFunc( self, event ):
        self.Close()


