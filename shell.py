import os


def executeShellCommand(command_line, is_log = False) -> object:
    command_line = 'PATH=$PATH:/usr/local/bin;' + command_line.replace("$", "\\$") + ' > /dev/tty'

    if is_log:
        print("exec: " + command_line)

    result_pipe = os.popen(command_line)
    result_     = result_pipe.readlines()
    result      = []

    for line in result_:
        # noinspection PyTypeChecker
        result.append(line.replace("\n", ""))

    return result
