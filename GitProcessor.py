import subprocess as sp
import os

def Pull(dirPath):
    oldPath = os.path.abspath()
    os.chdir(dirPath)
    cmd = 'git pull'
    try:
        errorlevel = sp.call(cmd, shell = True)
        if(errorlevel==0)
            Walk(dirPath, getUserEmail()) #readonly всем незаблокированным!!!
        return errorlevel

    finally:
        os.chdir(oldPath)
        


def Push(dirPath,FilesPath,comment):      #comment - комментарий пользователя
                                          #FilesPath список файлов для push-a
    oldPath = os.path.abspath()
    os.chdir(dirPath)
    i = len(FilesPath)
    cmd = 'git add %s\%s' %(dirPath,str(FilesPath[len(FilesPath)-i]))
    try:
        while (i>0):
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
            UnlockFiles(FilesPath) #разблокируем файлы
        return errorlevel
        
    finally:
        os.chdir(oldPath)

def Undo (dirPath,UndoFiles)
    oldPath = os.path.abspath()
    os.chdir(dirPath)
    i = len(UndoFiles)
    path = dirPath+"\\"+str(UndoFiles[len(UndoFiles)-i])
    cmd = 'git checkout --%s\%s' %(dirPath,str(UndoFiles[len(UndoFiles)-i]))
    try:
        while (i>0):
              errorlevel = sp.call(cmd, shell = True)
              if errorlevel!=0:
                  return errorlevel
              i=i-1
              Readonly(getUserEmail(),path)
        return errorlevel
    finally:
        os.chdir(oldPath)       
        
    
        

def IsGit(dirPath)  #является ли текущая директория .git?

    oldPath = os.path.abspath()
    os.chdir(dirPath)
    cmd = 'git status'
    try:
        errorlevel = sp.call(cmd, shell = True)
        return errorlevel
    finally:
        os.chdir(oldPath)
        

def getUserEmail()
   cmd = 'git config user.email'
    PIPE = sp.PIPE
    p = sp.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
         stderr=sp.STDOUT, close_fds=False)
    s = p.stdout.readline()
    return s


def getOtherFiles (dirPath) #возвращает список остальных файлов, т.е. не включённых в git
    oldPath = os.path.abspath()
    os.chdir(dirPath)
    OtherFiles = []
    cmd = 'gir ls-files --others'
    PIPE = sp.PIPE
    p = sp.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
        stderr=sp.STDOUT, close_fds=False)
    while True:
        s = p.stdout.readline()
        if not s: break
        OtherFiles.append(s)
    os.chdir(oldPath)
    return OtherFiles


def getLockedFiles (dirPath) # возвращает словарь изменённых файлов и  их статусы
    oldPath = os.path.abspath()
    os.chdir(dirPath)
    dictChangedFiles= {}
    cmd 'git diff --name-status'
    PIPE = subprocess.PIPE
    p = sp.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
         stderr=sp.STDOUT, close_fds=False)
    while True:
        s = p.stdout.readline()
        if not s: break
        dictChangedFiles[s[2:len(s)]] = s[0]
            
    return dictChangedFiles
    

def getStatusLockedFiles(dirPath) #Функция возвращает словарь, ключ - путь к файлу, значение - статус
      
    
