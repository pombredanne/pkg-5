import shell


def executeUpgrade():
    shell.executeCommand('brew update')
    shell.executeCommand('brew upgrade')


def executeInstall(pkg_name):
    shell.executeCommand('brew install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeCommand('brew uninstall ' + pkg_name)


def executeFindByName(name):
    shell.executeCommand('brew search ' + name)


def executeInfo(pkg_name):
    shell.executeCommand('brew info ' + pkg_name)
