import shell


def executeUpgrade():
    shell.executeCommand('pkg update')


def executeInstall(pkg_name):
    shell.executeCommand('pkg install ' + pkg_name)


def executeRemove(pkg_name):
    shell.executeCommand('pkg uninstall ' + pkg_name)


def executeFindByName(name):
    shell.executeCommand('pkg search ' + name)


def executeFix(name):
    shell.executeCommand('pkg fix')


def executeLocalize(language__name):
    shell.executeCommand('pkg change-facet facet.locale.' + language_name + '=True')
    shell.executeCommand('pkg change-facet facet.locale.' + language_name + '_' + language_name.upper() + '=True')
