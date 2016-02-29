import shell


def executeUpgrade():
    shell.executeCommand('urpmi --replacefiles --auto-update --auto')


def executeInstall(pkg_name):
    shell.executeCommand('urpmi ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeCommand('urpme --auto-orphans ' + pkg_name)


def executeFindByName(name):
    shell.executeCommand('urpmq --fuzzy ' + name)


def executeFindByFile(file_name):
    shell.executeCommand('urpmf ' + file_name)


def executeCheck():
    shell.executeCommand('rpm --verify -a')


def executeContent(pkg_name):
    shell.executeCommand('rpm -ql ' + pkg_name)
