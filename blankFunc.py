def IsGit(dirPath):
	# 0 if is Git
	# 1 if is NOT Git repository
	return 0
def getGitFiles(dirPath):
	# return list of git files
	return ["splash.avi", "splash.wav", "icon.png", "readme.txt"]

def getOtherFiles(dirPath):
	# return list of other files
	return ["song.wav", "mini.icon"]

def getStatusFiles(dirPath):
	# return dict name:status
	return {"readme.txt": "no one", "icon.png": "vasiya@gmail.ru", "song.wav" : "unversioned", "splash.wav" : "vasiya@gmail.ru", "splash.avi" : "petya@yandex.ru", "mini.icon" : "unversioned"}

def getUserEmail():
	#return current user's e-mail
	return "returned-e-mail@mail.ru"

def LockFiles(list_of_files, usermail):
	# lock the files from list_of_files
	return 0

def Pull(dirPath):
	# pull the project
	return 0

def getStatusLockedFiles(dirPath):
	#return "path to locked file":"status of this file"
	return {"\\icon.png": "changed", "\\song.wav": "unversioned", "\\splash.wav" : "changed", "\\res\\old_icon.png" : "removed"}

def Push(dirPath, listPushedFiles, comment):
	# push the list. with comment. from dirPath
	return 0

def Undo(dirPath, listUndoFiles):
	# undo the list from dirPath
	return 0

def UnlockFiles(list_of_files):
	# unlock list
	return 0