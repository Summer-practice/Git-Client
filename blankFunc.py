def IsGit(dirPath):
	# 0 if is Git
	# 1 if is NOT Git repository
	return 0
def getGitFiles(dirPath):
	# return list of git files
	return ["2one.c", "3two.cpp", "three.py", "four.txt"]

def getOtherFiles(dirPath):
	# return list of other files
	return ["4five.doc", "1six.icon", "seven.ppt", "eight.xlsx"]

def getStatusFiles(dirPath):
	# return dict name:status
	return {"2one.c": "no one", "3two.cpp": "1@1.ru", "three.py" : "unversioned", "four.txt" : "unversioned", "4five.doc" : "unversioned", "1six.icon" : "unversioned", "seven.ppt" : "juli-jakovleva@yandex.ru", "eight.xlsx" : "unversioned"}
	
def getUserMail():
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
	return {"\\temp\\one.c": "changed", "\\temp\\plus\\two.cpp": "unversioned", "\\three.py" : "changed", "\\four.txt" : "removed"}

def Push(dirPath, listPushedFiles, comment):
	# push the list. with comment. from dirPath
	return 0
	
def Undo(dirPath, listUndoFiles):
	# undo the list from dirPath
	return 0
	
def UnlockFiles(list_of_files):
	# unlock list
	return 0