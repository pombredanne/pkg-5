import shell


def executeUpgrade():
    shell.executeShellCommand('urpmi --replacefiles --auto-update --auto')


def executeInstall(pkg_name):
    shell.executeShellCommand('urpmi ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeShellCommand('urpme --auto-orphans ' + pkg_name)


def executeFindByName(name):
    shell.executeShellCommand('urpmq --fuzzy ' + name)


def executeFindByFile(file_name):
    shell.executeShellCommand('urpmf ' + file_name)


def executeCheck():
    shell.executeShellCommand('rpm --verify -a')


def executeContent(pkg_name):
    shell.executeShellCommand('rpm -ql ' + pkg_name)
