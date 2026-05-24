import os
import subprocess
import sys

class MemoryErrorsAnalyser:
    def __init__(self, test_exe, test_filename):
        self.test_exe = test_exe
        prefix = ""
        self.tests = []
        self.commands = []
        with open(test_filename) as f:
            lines = f.readlines()
            for line in lines:
                comment_pos = line.find('#')
                if comment_pos != -1:
                    line = line[:comment_pos].strip()
                if line.endswith('.\n'):
                    prefix = line[:-1].strip('\n')
                elif line.endswith('/0') or line[-2] != '/':
                    name = prefix + line.strip()
                    self.tests.append(name)

        for test in self.tests:
            log_filename = test.replace('.','_').replace('/','_') + '.txt'
            command = f"--log-file={log_filename} --leak-check=full --track-origins=yes {self.test_exe} --gtest_filter={test}"
            self.commands.append(command)

    def analyse(self, make_it_so):
        for command in self.commands:
            command = "valgrind " + command
            print(command)
            if make_it_so:
                subprocess.call(command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise ValueError(f"Usage: python {sys.argv[0]} <test_exe> <test_filename> <makeItSo>")

    analyser = MemoryErrorsAnalyser(sys.argv[1], sys.argv[2])
    analyser.analyse(sys.argv[3]=="makeItSo")
