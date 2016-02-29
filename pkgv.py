#!/usr/bin/env python3


import platform
import sys
import re


# -----load pkg by platform
# define variables:
#       platform_name
#       help_text
#       command_dictionary


def splitByUpCase(src):
    return re.findall('[A-Z][a-z]*', src)


def convertFunctionNameToParameterName(function_name):
    word_list       = splitByUpCase(function_name)
    parameter_name  = ''
    for word in word_list:
        parameter_name = parameter_name + word.lower() + '-'
    return parameter_name[:-1]


platform_name = platform.dist()[0].lower()
if platform_name == '':
    platform_name = platform.system().lower()
exec('import ' + platform_name + ' as pkg')

command_dictionary  = dict()
dir_                = dir(pkg)
for function_name in dir_:
    if function_name[:7] == 'execute':
        command_name                        = \
            convertFunctionNameToParameterName(function_name[7:])
        command_dictionary[command_name]    = \
            function_name

commands = ''
dictionary_commands = list(command_dictionary.keys())
dictionary_commands.sort()
for command in dictionary_commands:
    params      = ''
    func_code   = ''
    exec('func_code = pkg.' + command_dictionary[command] + '.__code__')

    for param in func_code.co_varnames:
        params += param

    commands = commands + "    " + command + ' ' + params + "\n"
help_text = "pkg command [argument]\n\ncommands:\n    platform\n" + commands

interface_commands = [
    'upgrade',
    'install',
    'remove',
    'check',
    'find-by-name',
    'find-by-file',
    'find-by-info',
    'info',
    'fix',
    'localize'
]

interface_commands_not_implemented = []
for interface_command in interface_commands:
    if interface_command not in dictionary_commands:
        interface_commands_not_implemented.append(interface_command)
interface_commands_not_implemented.sort()

if len(interface_commands_not_implemented) > 0:
    help_text += "\nnot implemented commands:\n"
    for interface_command in interface_commands_not_implemented:
        help_text += "    " + interface_command + "\n"


# -----


# ----- command line


if len(sys.argv) < 2:
    print(help_text)
    exit(0)
else:
    if len(sys.argv) == 2 and sys.argv[1] == 'platform':
        print('platform: ' + platform_name)
        exit()
    else:
        try:
            exec('pkg.' + command_dictionary[sys.argv[1]] + '(*sys.argv[2:])')
        except TypeError:
            print(help_text)
            exit(1)
        except BaseException as e:
            print(e)
            exit(1)


# -----
