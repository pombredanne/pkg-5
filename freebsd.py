import shell


def executeUpgrade():
    shell.executeShellCommand('pkg upgrade')


def executeInstall(pkg_name):
    shell.executeShellCommand('pkg install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeShellCommand('pkg remove ' + pkg_name)
    shell.executeShellCommand('pkg autoremove')


def executeFindByName(name):
    shell.executeShellCommand('pkg search ' + name)


def executeFindByFile(file_name):
    shell.executeShellCommand('pkg search ' + file_name)
