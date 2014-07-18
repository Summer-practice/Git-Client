import subprocess as sp
import os

def Pull(dirPath):
    
    os.chdir(dirPath)
    cmd = 'git pull'
  
    errorlevel = sp.call(cmd, shell = True)
    if(errorlevel==0)
        Walk(dirPath, getUserEmail()) #readonly for all unlocked!!!
    return errorlevel

          


def Push(dirPath,FilesPath,comment):      #FilesPath - files for 'push'
   
    os.chdir(dirPath)
    i = len(FilesPath)
    while (i>0):
            cmd = 'git add %s' %str(FilesPath[len(FilesPath)-i])
            errorlevel = sp.call(cmd, shell = True)
            if errorlevel!=0:
                return errorlevel
            i=i-1
    cmd = 'git commit -m \"%s\"' %comment
    errorlevel = sp.call(cmd, shell = True)
    if errorlevel!=0:
        return errorlevel
    cmd = 'git push'
    errorlevel = sp.call(cmd, shell = True)

    if errorlevel == 0:
        UnlockFiles(FilesPath) 
    return errorlevel
        
   

    

def Undo (dirPath,UndoFiles):
  
    os.chdir(dirPath)
    i = len(UndoFiles)
    while (i>0):
        path = dirPath+"\\"+str(UndoFiles[len(UndoFiles)-i])
        cmd = 'git checkout -- %s' %UndoFiles[len(UndoFiles)-i]
        errorlevel = sp.call(cmd, shell = True)
        if errorlevel!=0:
            return errorlevel
        i=i-1
        UnlockFiles(FilesPath)
    return errorlevel
    
        

def IsGit(dirPath):  #.git?

    os.chdir(dirPath)
    cmd = 'git status'
    errorlevel = sp.call(cmd, shell = True)
    return errorlevel
    
        

def getUserEmail():
    cmd = 'git config user.email'
    PIPE = sp.PIPE
    p = sp.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
         stderr=sp.STDOUT, close_fds=False)
    s = p.stdout.readline()
    return s


def getOtherFiles (dirPath): #unversioned files
    
    os.chdir(dirPath)
    OtherFiles = []
    cmd = 'git ls-files --others'
    PIPE = sp.PIPE
    p = sp.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
        stderr=sp.STDOUT, close_fds=False)
    while True:
        s = p.stdout.readline()
        if not s: break
        OtherFiles.append(s)
    return OtherFiles



def getGitFiles (dirPath):       #return a list with GIT files (main window)
    os.chdir(dirPath)
    GitFiles = []
    cmd = 'git ls-files --cached'
    PIPE = sp.PIPE
    p = sp.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
        stderr=sp.STDOUT, close_fds=False)
    while True:
        s = p.stdout.readline()
        if not s: break
        GitFiles.append(s)
    return GitFiles
        


def getLockedFiles (dirPath): #dict [name of changed file] = status (M or D)
    
    os.chdir(dirPath)
    dictChangedFiles= {}
    cmd = 'git diff --name-status'
    PIPE = subprocess.PIPE
    p = sp.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
         stderr=sp.STDOUT, close_fds=False)
    while True:
        s = p.stdout.readline()
        if not s: break
        dictChangedFiles[s[2:len(s)]] = s[0]
            
    return dictChangedFiles
    

def getLocalPath(dirPath): #Path for locak git repository
    for name in os.listdir(dirPath):
        path = os.path.join(dirPath, name)
        s = str(path)
        i = len(s)        
        while(s[i-1] != '\\'):
            i=i-1
        names = s[i:len(s)]

        if (os.path.isdir(path)and names=='.git'):
            ret = s[0:len(s)-5]
            return ret

    s = str(dirPath)
    i = len(s)        
    while(s[i-1] != '\\'):
        i=i-1
    dirPath = s[0:i-1]
    getLocalPath(dirPath)
      
    
