import shell


def executeUpgrade():
    shell.executeCommand('pkg update')


def executeInstall(pkg_name):
    shell.executeCommand('pkg install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeCommand('pkg uninstall ' + pkg_name)


def executeFindByName(name):
    shell.executeCommand('pkg search ' + name)
