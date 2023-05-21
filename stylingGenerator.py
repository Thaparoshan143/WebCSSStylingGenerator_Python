import os

# return the new path one step out, from given argument (inner path)
def getOuterPath(currDir):
    for num in range(len(currDir),1,-1):
        if currDirectory[num-1]=='/':
            innerIndex=num
            return currDir[0:innerIndex]
        
#return the new path one step in, from given argument (parent path) and next directory path
def getInnerPath(currDir,dir):
    if currDir[-1]=='/':
        return currDir+dir  
    else:
        return currDir+'/'+dir

# dislplay Menu Options for user:
def displayMenuOptions():
    print("\n====> Choose the Options <====")
    print("1. For Style Appending")
    print("2. Changing the working File Name")
    print("3. Changing the File Path/Directory")
    print("\n#Note : The File name must be mentioned by user before style appending\n")

parentDir=os.getcwd()

def updateUserOptions():
    try: 
        with open(parentDir+"/UserSelection.txt","r") as us:
            print("User File exits")
    except:
        print("User File is missing! Creating one...")
        with open(parentDir+"/UserSelection.txt","w") as nus:
            fileName="uni.css"
            fileDir=os.getcwd()
            nus.write(fileName+"\n"+fileDir)

def getCurrUserDirectory():
    try:
        with open(parentDir+"/UserSelection.txt","r") as cud:
            fileInfo=cud.read()
            fileInfo=str(fileInfo)
            for index,char in enumerate(fileInfo):
                if char == '/':
                    newFileInfo=fileInfo[index:]
                    break
            return newFileInfo
    except:
        print("Error! while opening the file! ")
        return os.getcwd()

def getCurrUserFileName():
    try:
        with open(parentDir+"/UserSelection.txt","r") as cud:
            fileInfo=cud.read()
            fileInfo=str(fileInfo)
            for index,char in enumerate(fileInfo):
                if char == '/':
                    newFileInfo=fileInfo[:index-1]
                    break
            return newFileInfo
    except:
        print("Error! while opening the file! ")
        return "uni.css"

def showStylingOption():
    pass

def showStylingMenu():
    fileName=getCurrUserFileName()
    currWorkingDir=getCurrUserDirectory()
    print("Current file Selected : " + fileName)
    print("Working Dir : " + currWorkingDir)

    showStylingOption()

displayMenuOptions()

menuOptChoice=int(input())

if menuOptChoice==1:
    showStylingMenu()
# elif menuOptChoice==2:
#     showFileChangingMenu()
# elif menuOptChoice==3:
#     showDirChangingMenu()

# updateUserOptions()

currDirectory=getCurrUserDirectory()
print("\nCurrent Working directory is : " + currDirectory)
