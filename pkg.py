#!/bin/python3


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


platform_name = platform.dist()[0]
exec('import ' + platform_name + ' as pkg')


dict_command_function   = dict()
dir_                    = dir(pkg)
commands                = ''
for function_name in dir_:
    if function_name[:7] == 'execute':
        command_name    = convertFunctionNameToParameterName(function_name[7:])            
        commands        = commands + command_name + ' | '
        dict_command_function[command_name] = function_name
commands = commands[:-2]


if len(sys.argv) <  2:
    print('pkg ' + commands + '[name]')


if len(sys.argv) == 2:
    command = sys.argv[1]
    exec('pkg.' + dict_command_function[command] + '()')
    

if len(sys.argv) == 3:
    command = sys.argv[1]
    name    = sys.argv[2]
    exec('pkg.' + dict_command_function[command] + '(name)')
