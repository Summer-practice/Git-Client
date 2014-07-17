import wx
import mainWindowGui
from unlockAndPushWindow import *
from undoChangesWindow import *
from blankFunc import *
from sys import maxint

# Implementing gitClientGui
class mainWindow ( mainWindowGui.mainWindowGui ):
    dirPath = " "
    selectedFilesPaths = []
    def __init__( self, parent ):
        mainWindowGui.mainWindowGui.__init__( self, parent )
	# Handlers for gitClientGui events.

    def textPathFunc( self, event):
        # TODO: Implement textPathFunc
        #print "222"
        pass

    def enterPathFunc( self, event ):
        #print "111"
        #print self.browse_path.GetValue()
        self.dirPath = self.browse_path.GetValue()
        # + check for invalid input!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.selectedFilesPaths = []
        self.list_ctrl.DeleteAllItems()
        self.showDirectoryFiles(event)
        # TODO: Implement enterPathFunc
        #pass

    def browseButtonFunc( self, event ):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE)
        self.dirPath = " "
        self.selectedFilesPaths = []
        if dlg.ShowModal() == wx.ID_OK: #print "You chose %s" % dlg.GetPath()
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
        #index = self.list_ctrl.InsertStringItem(maxint, ". .")
        for item in dirFiles:
            info = "%s:(%s)" % (col, item)
            data.append(info)
            index = self.list_ctrl.InsertStringItem(maxint, dirFiles[i])
            #i = i+1
            for col, text in enumerate(dirFiles[i:]):
                self.list_ctrl.SetStringItem(index, col+1, dictStatus[item])
            i = i+1

    #def itemActivatedFunc( self, event ):
        # TODO: Implement itemActivatedFunc
        #pass

    def itemDeselectedFunc( self, event ):
        # TODO: Implement itemDeselectedFunc
        item = event.GetItem()
        self.selectedFilesPaths.remove(self.dirPath + "\\" + item.GetText())
        #print self.selectedFilesPaths
        #print "Item deselected:", item.GetText()
        #pass

    def itemSelectedFunc( self, event ):
        # TODO: Implement itemSelectedFunc
        item = event.GetItem()
        self.selectedFilesPaths.append(self.dirPath + "\\" + item.GetText())
        #print self.selectedFilesPaths
        #self.browse_path.SetValue(self.selectedFilesPaths[0])
        #print "Item selected:", item.GetText()
        #pass

    def pullFunc( self, event ):
		# TODO: Implement pullFunc
        if IsGit(self.dirPath) == 1 :
            #error
            msg = "Cannot pull recent changes. The current folder is not under Git version control!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
            """elif self.selectedFilesPaths == []:
            msg = "You have not selected files for pulling!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal() """
        elif self.dirPath == " ":
            msg = "You must choose a directory for pull!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
        else:
            Pull(self.dirPath)

            """#self.dirPath = " "
            self.selectedFilesPaths = []
            self.list_ctrl.DeleteAllItems()
            self.showDirectoryFiles(event)"""

            msg = "Pull complete!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Message", style=wx.OK|wx.ICON_INFORMATION)
            result = dlg.ShowModal()


    def lockFunc( self, event ):
        if self.selectedFilesPaths == []:
            msg = "You have not selected files for locking!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
            """msg = "Cannot lock the file. It is already locked by %s!" %"LOCKED E-MAIL"
            dlg2 = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg2.ShowModal()"""
        else:
            LockFiles(self.selectedFilesPaths, getUserMail())
            msg = "Lock complete!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Message", style=wx.OK|wx.ICON_INFORMATION)
            result = dlg.ShowModal()
		# TODO: Implement lockFunc
		#pass

    def unlockAndPushFunc( self, event ):
		# TODO: Implement unlockAndPushFunc
        #app2 = wx.App(False)
        if self.dirPath != " ":
            dictLockedStatus = getStatusLockedFiles(self.dirPath)
            listLockedStatus = []
            for item in dictLockedStatus:
                listLockedStatus.append(item + " ( " + dictLockedStatus[item] + " ) ")
            #print listLockedStatus
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
            #print listLockedStatus
            frame3 = undoChangesWindow(None, listLockedStatus, self.dirPath)
            frame3.Show(True)
        else:
            msg = "You must choose a directory for Undo changes!"
            dlg = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg.ShowModal()
		# TODO: Implement undoChangesFunc

"""app = wx.App()
wnd = formsGitClientGui(None)
app.MainLoop()"""

app = wx.App(False)

#create an object of Frame
frame = mainWindow(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
