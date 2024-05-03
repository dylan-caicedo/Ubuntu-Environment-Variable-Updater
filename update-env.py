import sys, os
args = sys.argv
PARAMETER_NAME = 'var'
PARAMETER_VALUE = 'value'
ENV_FILE_PATH = 'TEST_FILE'

def findArg(parameterName):
    parameter = [x.split("=") for x in args if x.split("=")[0] == parameterName]
    if len(parameter) == 0 or parameter is None:
        raise Exception(f'You must specify the argument and value for "{parameterName}"')
    else: 
        return parameter[0][1]

def getVarLineFromVarName(varName):
    return f'export {varName}='
def updateExistingVariable(fileText, varName, varValue):
    varLine = getVarLineFromVarName(varName)
    varNameStartIndex = fileText.find(varLine) + len(varLine)
    varNameEndIndex = fileText.find('"', varNameStartIndex + 1, len(fileText))
    newFileText = f'{fileText[0:varNameStartIndex]}\"{varValue}\"{fileText[varNameEndIndex + 1: len(fileText)]}'
    
    return newFileText
def updateNonExistingVariable(fileText, varName, varValue):
    newLine = "\n" if len(fileText.strip()) != 0 else ""
    varLine = getVarLineFromVarName(varName)
    return f'{fileText}{newLine}{varLine}"{varValue}"'

def updateVariableInFileText(fileText):
    varName = findArg(PARAMETER_NAME)
    varValue = findArg(PARAMETER_VALUE)
    varLine = getVarLineFromVarName(varName)
    if fileText.find(varLine) == -1:
        fileText = updateNonExistingVariable(fileText, varName, varValue)
    else: 
        fileText = updateExistingVariable(fileText, varName, varValue)

    return fileText

def writeNewTextOnFile(fileName, fileText):
    file = open(fileName, 'w')
    file.write(fileText)
    file.flush()
    file.truncate()
    file.close()

def readFile(fileName):
    file = open(fileName, 'r')
    fileText = file.read()
    file.close()
    return fileText

fileName = os.environ[ENV_FILE_PATH]
content = readFile(fileName)
newContent = updateVariableInFileText(content)
writeNewTextOnFile(fileName, newContent)