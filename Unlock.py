# -*- coding: utf-8 -*-
"""
For the "Unlock & Push" and "Undo changes":
-Unlock the file
-Set "read only" on unlocked files"
"""
from Lock import Check
from Unknowname import USER_LOCK#just for check. I I'll remove it
import pickle
import os
import stat

def UnlockFiles(list_of_files):#list_of_files is List of files to unlock
    """Removes the files from  the "user_lock" and set "read only" on this files"""
    
    userLockDict = Check()
    
    for element in list_of_files:
        os.chmod(element, stat.S_IREAD)
        del userLockDict[element]
        
    if not userLockDict:#if the dict is empty
        open(USER_LOCK, 'w')
        USER_LOCK.close()
        
    else:
        with open(USER_LOCK, 'w') as f:
            pickle.dump(userLockDict,f)
    
    