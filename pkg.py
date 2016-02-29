#!/usr/bin/env python3


import platform
import sys
import re


def splitByUpcase(src):
    return re.findall('[A-Z][a-z]*', src)


def convertFunctionNameToParameterName(function_name):
    word_list       = splitByUpcase(function_name)
    parameter_name  = ''
    for word in word_list:
        parameter_name = parameter_name + word.lower() + '-'
    return parameter_name[:-1]


platform_name = platform.dist()[0].lower()
if platform_name == '':
    platform_name = platform.system().lower()
exec('import ' + platform_name + ' as pkg')


def showPlatform():
    print('platform: ' + platform_name)
    exit(0)


dict_command_function   = dict()
dir_                    = dir(pkg)
for function_name in dir_:
    if function_name[:7] == 'execute':
        command_name    = convertFunctionNameToParameterName(function_name[7:])            
        dict_command_function[command_name] = function_name


commands = ''
for command in dict_command_function.keys():
    params = ''
    exec('func_code = pkg.' + dict_command_function[command] + '.__code__')

    for param in func_code.co_varnames:
        params = params + param

    commands = commands + "    " + command + ' ' + params + "\n"

help = "pkg\n    platform\n" + commands


if len(sys.argv) <  2:
    print(help)
    exit(0)
    

command = sys.argv[1]


if command != 'platform'  and  command not in dict_command_function.keys():
    print("unknown command: " + command + "\n")
    print(help)
    exit(1)


if len(sys.argv) == 2:
    if command == 'platform':
        showPlatform()
    exec('pkg.' + dict_command_function[command] + '()')
    

if len(sys.argv) == 3:
    name = sys.argv[2]
    exec('pkg.' + dict_command_function[command] + '(name)')
