import shell


def executeUpgrade():
    shell.executeCommand('pkg upgrade')


def executeInstall(pkg_name):
    shell.executeCommand('pkg install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeCommand('pkg remove ' + pkg_name)
    shell.executeCommand('pkg autoremove')


def executeFindByName(name):
    shell.executeCommand('pkg search ' + name)
