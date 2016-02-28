import shell


def executeUpgrade():
    shell.executeShellCommand('pkg update')


def executeInstall(pkg_name):
    shell.executeShellCommand('pkg install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeShellCommand('pkg uninstall ' + pkg_name)


def executeFindByName(name):
    shell.executeShellCommand('pkg search ' + name)
