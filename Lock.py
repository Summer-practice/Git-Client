# -*- coding: utf-8 -*-
"""
To implement the "Pull": 
-Receive a list of locked files 
-Set "read only" on all files except already locked by the user
"""
import pickle
import os
from Unknowname import username
from Unknowname import filename
from Unknowname import USER_LOCK
def Check():
    """returns the dict or 0 if the file is empty"""
    if os.stat(USER_LOCK).st_size==0:
        return 0  
    else:
        with open(USER_LOCK, 'r') as f:
            fileuser = pickle.load(f)#fileuser is a dict,key==filename,value==user who locked
        return fileuser
        
def LockedFile(username, filename):
    """Returns 0 if the file is unlocked, 1 if locked"""
    fileuser = Check()
    if fileuser == 0:
        return 0
    elif filename in fileuser:
            return 1
    else:
        return 0
        
def ListOfLockedFiles():
    """Returns a list of locked files or None if user_lock is empty"""
    fileuser = Check()
    if fileuser == 0:
        return None
    else:
        return fileuser.keys()
    
def FilesAndUsers():
    """Returns a dict,key==filename,value==user who locked  or None if user_lock is empty"""
    fileuser = Check()
    if fileuser == 0:
        return None
    else:
        return fileuser
        
def ReadOnly()
print LockedFile(username, filename)  