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

from Lock import LockedFile
from Lock import Check
from Unknowname import USER_LOCK#just for check. I I'll remove it

def LockFiles(list_of_files, username):#list_of_files is List of files to lock
    """
    If file is locked by another user calls the error window.
    if not  puts the file name in the user_lock
    """
    lockList  = list()
    errorList = list()
    
    for element in list_of_files:
        if not LockedFile(element):
            lockList.append(element)
        else:
            errorList.append(element)
        
    if Check():
        userLockDict = Check()
        
    if lockList:
        for element in lockList:
            userLockDict[element] = username
            
        with open(USER_LOCK, 'w') as f:
             pickle.dump(userLockDict,f)
        RemoveReadOnly(lockList)
        
    if errorList:
        pass #Call the error window
    
        
def RemoveReadOnly(lockList):
    """Remove "Read only" from files locked by this user"""
    
    for element in lockList:
        os.chmod(element, stat.S_IWRITE)
            
        
        