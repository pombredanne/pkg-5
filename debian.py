import shell


def executeUpgrade():
    shell.executeShellCommand('apt-get update')
    shell.executeShellCommand('apt-get upgrade')


def executeInstall(pkg_name):
    shell.executeShellCommand('apt-get install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeShellCommand('apt-get remove ' + pkg_name)


def executeFindByName(name):
    shell.executeShellCommand('apt-cache search --names-only ' + name)


def executeFindByFile(file_name):
    shell.executeShellCommand('apt-file search ' + file_name)


def executeCheck():
    shell.executeShellCommand('apt-get check')
    shell.executeShellCommand('debsums | grep \'﻿ OK\'')
