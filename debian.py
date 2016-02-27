import shell


def executeUpgrade():
    shell.executeShellCommand('apt-get update && upt-get upgrade')


def executeInstall(pkg_name):
    shell.executeShellCommand('apt-get install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeShellCommand('apt-get remove ' + pkg_name)


def executeFindByName(name):
    shell.executeShellCommand('apt-get search ' + name)
