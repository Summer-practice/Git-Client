# -*- coding: utf-8 -*-
"""
For the "Lock":
-Checking the status of the file (locked / unlocked)
-If the file is already locked cause the error window
-If the file is unlocked add it to the file with name "user_lock", remove status "Read only"
"""
import pickle
import os
import stat
import wx

from Unlock import GetUserLockName
from Lock import LockedFile
from Lock import UserLockGet
from GitProcessor import getLocalPath#Unfortunately, I don't have any directory for this function

def LockFiles(list_of_files, username):#list_of_files is List of files to lock
    """
    If file is locked by another user calls the error window.
    if not - puts the file name in the user_lock
    """
    
    lockList  = list()
    errorList = list()
    USER_LOCK = GetUserLockName()
    userLockNew = dict()
    
    for element in list_of_files:#There are 2 lists: already locked and unlocked
        if not LockedFile(element):
            lockList.append(element)
        else:
            errorList.append(element)
        
    if UserLockGet():
        userLockDict = UserLockGet()
        
    if lockList:
        for element in lockList:
            userLockDict[element] = username
            
        for element in userLockDict:#Cut off part of the way. Because it's differ from user to user
            newElem = element[len(getLocalPath())-len(os.path.dirname(getLocalPath())):len(element)]
            userLockNew[newElem] = userLockDict[element]
            
        os.chmod(USER_LOCK, stat.S_IWRITE)   
        with open(USER_LOCK, 'w') as f:
             pickle.dump(userLockNew,f)
        os.chmod(USER_LOCK, stat.S_IREAD)
        RemoveReadOnly(lockList)
        
    if errorList:#Call the error window.
        for element in errorList:
            msg = "Cannot lock the file %s. It is already locked by %s!" %(element, userLockDict[element])
            dlg2 = wx.MessageDialog(parent=None, message=msg, caption="Git Client Error", style=wx.OK|wx.ICON_ERROR)
            result = dlg2.ShowModal() 
    
        
def RemoveReadOnly(lockList):
    """Remove "Read only" from files locked by this user"""
    
    for element in lockList:
        os.chmod(element, stat.S_IWRITE)
            
        
        