# -*- coding: utf-8 -*-

import wx
import wx.xrc

class unlockAndPushWindowGui ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Unlock and Push", pos = wx.DefaultPosition, size = wx.Size( 300,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.textComment = wx.StaticText( self, wx.ID_ANY, u"Enter your comments:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textComment.Wrap( -1 )
		self.textComment.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.textComment.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer1.Add( self.textComment, 0, wx.ALL, 5 )

		self.commentBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.commentBox.SetMinSize( wx.Size( -1,85 ) )

		bSizer1.Add( self.commentBox, 3, wx.ALL|wx.EXPAND, 5 )

		checkListChoices = []
		self.checkList = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListChoices, 0 )
		bSizer1.Add( self.checkList, 6, wx.ALL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.checkBoxSelect = wx.CheckBox( self, wx.ID_ANY, u"Select / deselect all", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkBoxSelect.SetValue(True)
		self.checkBoxSelect.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer2.Add( self.checkBoxSelect, 1, wx.ALL, 5 )

		self.showUnversioned = wx.CheckBox( self, wx.ID_ANY, u"Show unversioned items", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.showUnversioned.SetValue(True)
		self.showUnversioned.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer2.Add( self.showUnversioned, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 4 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.OkButton = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OkButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer3.Add( self.OkButton, 1, wx.ALL, 5 )

		self.CancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CancelButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer3.Add( self.CancelButton, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.commentBox.Bind( wx.EVT_TEXT, self.commentTextFunc )
		self.commentBox.Bind( wx.EVT_TEXT_ENTER, self.commentEnterFunc )
		self.checkList.Bind( wx.EVT_LISTBOX, self.listBoxSelectedItemFunc )
		self.checkList.Bind( wx.EVT_CHECKLISTBOX, self.listBoxToggledFunc )
		self.checkBoxSelect.Bind( wx.EVT_CHECKBOX, self.selectDeselectAllFunc )
		self.showUnversioned.Bind( wx.EVT_CHECKBOX, self.showUnversionedFunc )
		self.OkButton.Bind( wx.EVT_BUTTON, self.okClickFunc )
		self.CancelButton.Bind( wx.EVT_BUTTON, self.cancelClickFunc )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class

	def commentTextFunc( self, event ):
		event.Skip()

	def commentEnterFunc( self, event ):
		event.Skip()

	def listBoxSelectedItemFunc( self, event ):
		event.Skip()

	def listBoxToggledFunc( self, event ):
		event.Skip()

	def selectDeselectAllFunc( self, event ):
		event.Skip()

	def showUnversionedFunc( self, event ):
		event.Skip()

	def okClickFunc( self, event ):
		event.Skip()

	def cancelClickFunc( self, event ):
		event.Skip()


