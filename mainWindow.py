import wx
import mainWindowGui

"""from Lock import *
from Unlock import *
from Try_and_lock import  *
from GitProcessor import *"""

from unlockAndPushWindow import *
from undoChangesWindow import *
from blankFunc import *
from sys import maxint

class mainWindow ( mainWindowGui.mainWindowGui ):
    dirPath = " "
    selectedFilesPaths = []
    def __init__( self, parent ):
        mainWindowGui.mainWindowGui.__init__( self, parent )

    def enterPathFunc( self, event ):
        self.dirPath = self.browse_path.GetValue()
        # + check for invalid input!!!!!
        self.selectedFilesPaths = []
        self.list_ctrl.DeleteAllItems()
        self.showDirectoryFiles(event)

    def browseButtonFunc( self, event ):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE)
        self.dirPath = " "
        self.selectedFilesPaths = []
        if dlg.ShowModal() == wx.ID_OK:
            self.browse_path.SetValue(dlg.GetPath())
            self.dirPath = dlg.GetPath()
        dlg.Destroy()
        self.list_ctrl.DeleteAllItems()
        self.showDirectoryFiles(event)

    def showDirectoryFiles( self, event ):
        dirFiles = getGitFiles(self.dirPath) + getOtherFiles(self.dirPath)
        dirFiles.sort()
        col = 0
        i = 0
        data = []
        dictStatus = getStatusFiles(self.dirPath)
        for item in dirFiles:
            info = "%s:(%s)" % (col, item)
            data.append(info)
            index = self.list_ctrl.InsertStringItem(maxint, dirFiles[i])
            #i = i+1
            for col, text in enumerate(dirFiles[i:]):
                self.list_ctrl.SetStringItem(index, col+1, dictStatus[item])
            i = i+1

    def itemDeselectedFunc( self, event ):
        item = event.GetItem()
        self.selectedFilesPaths.remove(self.dirPath + "\\" + item.GetText())

    def itemSelectedFunc( self, event ):
        item = event.GetItem()
        self.selectedFilesPaths.append(self.dirPath + "\\" + item.GetText())

    def pullFunc( self, event ):
        if IsGit(self.dirPath) == 1 :
            msg = "Cannot pull recent changes. The current folder is not under Git version control!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
        elif self.dirPath == " ":
            msg = "You must choose a directory for pull!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
        else:
            Pull(self.dirPath)

            msg = "Pull complete!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Message", style=wx.OK|wx.ICON_INFORMATION)
            result = dlg.ShowModal()


    def lockFunc( self, event ):
        if self.selectedFilesPaths == []:
            msg = "You have not selected files for locking!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
        else:
            LockFiles(self.selectedFilesPaths, getUserEmail())
            msg = "Lock complete!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Message", style=wx.OK|wx.ICON_INFORMATION)
            result = dlg.ShowModal()

    def unlockAndPushFunc( self, event ):
        if self.dirPath != " ":
            dictLockedStatus = getStatusLockedFiles(self.dirPath)
            listLockedStatus = []
            for item in dictLockedStatus:
                listLockedStatus.append(item + " ( " + dictLockedStatus[item] + " ) ")
            frame2 = unlockAndPushWindow(None, listLockedStatus, self.dirPath)
            frame2.Show(True)
        else:
            msg = "You must choose a directory for push!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()

    def undoChangesFunc( self, event ):
        if self.dirPath != " ":
            dictLockedStatus = getStatusLockedFiles(self.dirPath)
            listLockedStatus = []
            for item in dictLockedStatus:
                listLockedStatus.append(item + " ( " + dictLockedStatus[item] + " ) ")
            frame3 = undoChangesWindow(None, listLockedStatus, self.dirPath)
            frame3.Show(True)
        else:
            msg = "You must choose a directory for Undo changes!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()

app = wx.App(False)
frame = mainWindow(None)
frame.Show(True)
app.MainLoop()
