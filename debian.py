import shell


def executeUpgrade():
    shell.executeCommand('apt-get update')
    shell.executeCommand('apt-get upgrade')


def executeInstall(pkg_name):
    shell.executeCommand('apt-get install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeCommand('apt-get remove ' + pkg_name)
    shell.executeCommand('apt-get autoremove')


def executeFindByName(name):
    shell.executeCommand('apt-cache search --names-only ' + name)


def executeFindByFile(file_name):
    shell.executeCommand('apt-file search ' + file_name)


def executeCheck():
    shell.executeCommand('apt-get check')
    shell.executeCommand('debsums | grep \'﻿ OK\'')


def executeContent(pkg_name):
    shell.executeCommand('apt-file show ' + pkg_name)
