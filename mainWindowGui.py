# -*- coding: utf-8 -*-

import wx
import wx.xrc

class mainWindowGui ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Git Client", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.path_text = wx.StaticText( self, wx.ID_ANY, u"Path:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.path_text.Wrap( -1 )
        bSizer6.Add( self.path_text, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.browse_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer6.Add( self.browse_path, 1, wx.ALL, 5 )

        self.browse_button = wx.Button( self, wx.ID_ANY, u"Browse...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.browse_button, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

		#self.list_ctrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST|wx.LC_SINGLE_SEL )
        self.list_ctrl = wx.ListCtrl(self, 0, style=wx.LC_REPORT | wx.BORDER_NONE | wx.LC_EDIT_LABELS | wx.LC_SORT_ASCENDING | wx.LC_VRULES)
        self.list_ctrl.Show(True)
        self.list_ctrl.InsertColumn(0, "Files & Folders")
        self.list_ctrl.InsertColumn(1, "Locked by")
        self.list_ctrl.SetColumnWidth(0, 140)
        self.list_ctrl.SetColumnWidth(1, 190)
        bSizer7.Add( self.list_ctrl, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer2.Add( bSizer7, 10, wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 12, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.pull_button = wx.Button( self, wx.ID_ANY, u"Pull", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.pull_button, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.lock_button = wx.Button( self, wx.ID_ANY, u"Lock", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.lock_button, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.unlock_and_push = wx.Button( self, wx.ID_ANY, u"Unlock and Push", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.unlock_and_push, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.undo_changes = wx.Button( self, wx.ID_ANY, u"Undo changes...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.undo_changes, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.Add( bSizer3, 5, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

		# Connect Events
        self.browse_path.Bind( wx.EVT_TEXT_ENTER, self.enterPathFunc )
        self.browse_button.Bind( wx.EVT_BUTTON, self.browseButtonFunc )
        #self.list_ctrl.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.itemActivatedFunc )
        self.list_ctrl.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.itemDeselectedFunc )
        self.list_ctrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.itemSelectedFunc )
        self.pull_button.Bind( wx.EVT_BUTTON, self.pullFunc )
        self.lock_button.Bind( wx.EVT_BUTTON, self.lockFunc )
        self.unlock_and_push.Bind( wx.EVT_BUTTON, self.unlockAndPushFunc )
        self.undo_changes.Bind( wx.EVT_BUTTON, self.undoChangesFunc )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def enterPathFunc( self, event ):
		event.Skip()

	def browseButtonFunc( self, event ):
		event.Skip()

	def itemActivatedFunc( self, event ):
		event.Skip()

	def itemDeselectedFunc( self, event ):
		event.Skip()

	def itemSelectedFunc( self, event ):
		event.Skip()

	def pullFunc( self, event ):
		event.Skip()

	def lockFunc( self, event ):
		event.Skip()

	def unlockAndPushFunc( self, event ):
		event.Skip()

	def undoChangesFunc( self, event ):
		event.Skip()


