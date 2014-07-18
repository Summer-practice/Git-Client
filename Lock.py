# -*- coding: utf-8 -*-
"""
For the "Pull": 
-Receive a list of locked files 
-Set "read only" on all files except already locked by the user
"""
import pickle
import os
import stat

from Unlock import GetUserLockName
from GitProcessor import getLocalPath#Unfortunately, I don't have any directory for this function

def UserLockGet():
    """Returns the dict or 0 if the user_lock is empty"""
    
    USER_LOCK = GetUserLockName()
    userLockNew = dict()
    
    if not os.stat(USER_LOCK).st_size:
        return 0  
        
    else:
        with open(USER_LOCK, 'r') as f:
            userLockDict = pickle.load(f)#userLockDict is a dict,key==filename,value==user who locked
        
        rep = getLocalPath()
        sect = rep[0:len(rep)-os.path.dirname(getLocalPath())]
        
        for element in userLockDict:#Add part of the way. Because it's different for different user
            newElem = sect + element
            userLockNew[newElem] = userLockDict[element]
        return userLockNew
        
        
def LockedFile(filename):
    """Returns 0 if the file is unlocked, 1 if locked"""
    
    userLockDict = UserLockGet() 
    
    if not userLockDict :
        return 0    
    elif filename in userLockDict:
            return 1        
    else:
        return 0
        
        
def ListOfLockedFiles():
    """Returns a list of locked files or False if "user_lock" is empty"""
    
    userLockDict = UserLockGet()
    
    if not userLockDict :
        return False    
    else:
        return userLockDict.keys()
        
        
        
def ReadOnly(username, path):
    """Set "read only" on file if it wasn't blocked by user"""
    
    userLockDict = UserLockGet()
    
    if not LockedFile(path) :
        os.chmod(path, stat.S_IREAD)
        
    elif userLockDict[path] != username:
        os.chmod(path, stat.S_IREAD)
        

def Walk(direct, username):#need a path to the  local repository and username
    """Recursively through all the files and subdirectories of this repository"""
    
    for name in os.listdir(direct):
        path = os.path.join(direct, name)
        
        if os.path.isfile(path):
            ReadOnly(username,path)
            
        else:
            Walk(path, username)