# -*- coding: utf-8 -*-
"""
For the "Unlock & Push" and "Undo changes":
-Unlock the file
-Set "read only" on unlocked files"
"""
from Lock import UserLockGet
import pickle
import os
import stat

def UnlockFiles(list_of_files):#list_of_files is List of files to unlock
    """Removes the files from  the "user_lock" and set "read only" on this files"""
    
    USER_LOCK = GetUserLockName()
    userLockDict = UserLockGet()
    userLockNew = dict()
    
    for element in list_of_files:
        os.chmod(element, stat.S_IREAD)
        del userLockDict[element]
        
    os.chmod(USER_LOCK, stat.S_IWRITE)    
    if not userLockDict:#if the dict is empty
        open(USER_LOCK, 'w')
        USER_LOCK.close()
        
    else:
        for element in userLockDict:#Cut off part of the way. Because it's differ from user to user
            newElem = element[len(LocalRepositoryName())-len(os.path.dirname(LocalRepositoryName())):len(element)]
            userLockNew[newElem] = userLockDict[element]
        with open(USER_LOCK, 'w') as f:
            pickle.dump(userLockNew,f)
    os.chmod(USER_LOCK, stat.S_IREAD)        
            
def GetUserLockName():
    """"Returns a path to the "user_lock" """
    
    repositoryName = RemoteRepositoryName() #It must returns path to the remote repository
    return os.path.join(repositoryName, 'user_lock.pickle')
    
    
    