from subprocess import run, PIPE, CalledProcessError
import shlex
# run(cmd)
# run(cmd-as-one-str)
# run(cmd-as-list-of_words)


cmd1 = 'netstat -an'   # OK on windows, not OK on Mac/Linux without shell=True
cmd2 = ['netstat', '-anj']   # OK on all platforms

raw_command = 'netstat -jan'
command_words = shlex.split(raw_command)
print("command_words: {}".format(command_words))
run(command_words)
print('-' * 60)

try:
    process = run(command_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err)
else:
    for line in process.stdout.decode().splitlines():
        if 'ESTABLISHED' in line:
            print(line)






