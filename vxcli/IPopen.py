#!/usr/bin/env python3
# IPopen
# Used to run command that we want to interact with.
# Source: https://stackoverflow.com/questions/19880190/interactive-input-output-using-python

######################
# Imports & Globals
######################

import sys
import os
import subprocess
import threading
import select


######################
# IPopen
######################

class IPopen(object):

    def __init__(self):
        pass

    def run(self, command):
        env = os.environ.copy()
        p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #sys.stdout.write("Started Local Terminal...\r\n\r\n")

        def writeall(p):
            while True:
                # print("read data: ")
                data = p.stdout.read(1).decode("utf-8")
                if not data:
                    break
                sys.stdout.write(data)
                sys.stdout.flush()

        writer = threading.Thread(target=writeall, args=(p,))
        writer.start()

        try:
            while writer.is_alive():
                # https://stackoverflow.com/questions/3471461/raw-input-and-timeout
                ready, _, _ = select.select([sys.stdin], [], [], 1)

                if ready:
                    #d = sys.stdin.read(1)
                    d = sys.stdin.readline()
                    if not d:
                        break
                    self._write(p, d.encode())

        except EOFError:
            pass

        finally:
            p.kill()


    def _write(self, process, message):
        process.stdin.write(message)
        process.stdin.flush()
