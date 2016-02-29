from subprocess import Popen, PIPE


def executeCommand(command_line, is_log = False) -> object:
    command_line = 'PATH=$PATH:/usr/local/bin;' + command_line.replace("$", "\\$") + ' > /dev/tty 0> /dev/tty'

    if is_log:
        print("exec: " + command_line)

    result_pipe = Popen(command_line, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
    result_     = result_pipe.stdout.read().decode("utf-8")
    error       = result_pipe.stderr.read().decode("utf-8")
    result      = []

    for line in result_:
        # noinspection PyTypeChecker
        result.append(line.replace("\n", ""))

    if error != '':
        raise BaseException(error)

    return result
