import wx
from blankFunc import *
import unlockAndPushWindowGui

# Implementing unlockAndPushWindGow
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
    #comment = "No comment"
	# Handlers for unlockAndPushWindow events.
    def commentTextFunc( self, event ):
        #print self.commentBox.GetValue()
        # TODO: Implement commentTextFunc
        pass

    def commentEnterFunc( self, event ):
        # "123"
        # TODO: Implement commentEnterFunc
        pass

    def listBoxSelectedItemFunc( self, event ):
		# TODO: Implement listBoxSelectedItemFunc
		pass

    def listBoxToggledFunc( self, event ):
		# TODO: Implement listBoxToggledFunc
		pass

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
        # Peredavat Ane self.dirPath
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

		# TODO: Implement okClickFunc

    def cancelClickFunc( self, event ):
        self.Close()
		# TODO: Implement cancelClickFunc
		#pass

"""app = wx.App(False)
frame = formsUnlockAndPushWindow(None, ["111", "222"])
frame.Show(True)
app.MainLoop()"""

