# -*- coding: utf-8 -*-
"""
To implement the "Pull": 
-Receive a list of locked files 
-Set "read only" on all files except already locked by the user
"""
import pickle
import os, stat
from Unknowname import username#just for check. I I'll remove it
from Unknowname import filename#just for check. I I'll remove it
from Unknowname import USER_LOCK#just for check. I I'll remove it
def Check():#need a path to the user_lock
    """returns the dict or 0 if the file is empty"""
    if os.stat(USER_LOCK).st_size==0:
        return 0  
    else:
        with open(USER_LOCK, 'r') as f:
            fileuser = pickle.load(f)#fileuser is a dict,key==filename,value==user who locked
        return fileuser
        
def LockedFile(filename):
    """Returns 0 if the file is unlocked, 1 if locked"""
    fileuser = Check()
    if fileuser == 0:
        return 0
    elif filename in fileuser:
            return 1
    else:
        return 0
        
def ListOfLockedFiles():#need a path to the user_lock
    """Returns a list of locked files or None if user_lock is empty"""
    fileuser = Check()
    if fileuser == 0:
        return None
    else:
        return fileuser.keys()
    
def FilesAndUsers():#need a path to the user_lock
    """Returns a dict,key==filename,value==user who locked  or None if user_lock is empty"""
    fileuser = Check()
    if fileuser == 0:
        return None
    else:
        return fileuser
        
def ReadOnly(username, path):
    """Set "read only" on file if it wasn't blocked by current user"""
    fileuser = Check()
    if fileuser == 0:
        os.chmod(path, stat.S_IREAD)
    elif path not in fileuser:
        os.chmod(path, stat.S_IREAD)
    elif fileuser[path] != username:
        os.chmod(path, stat.S_IREAD)

def Walk(dir, username):#need a path to the repository and username
    """Recursively through all the files and subdirectories of this repository"""
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            ReadOnly(username,path)
        else:
            Walk(path, username)