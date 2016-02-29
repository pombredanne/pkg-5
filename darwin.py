import shell


def executeUpgrade():
    shell.executeShellCommand('brew upgrade')


def executeInstall(pkg_name):
    shell.executeShellCommand('brew install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeShellCommand('brew uninstall ' + pkg_name)


def executeFindByName(name):
    shell.executeShellCommand('brew search ' + name)


def executeContent(pkg_name):
    shell.executeShellCommand('brew list ' + pkg_name)
