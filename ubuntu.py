from debian import *


def executeLocalize(language_name):
    executeInstall('language-selector-common')
    shell.executeCommand('check-language-support --language=' + language_name)
