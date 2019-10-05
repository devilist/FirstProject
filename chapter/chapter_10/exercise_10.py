import os

pid = os.getpid()
where = os.getcwd()
print("current pid: ", pid, " workspace dir: ", where)
if hasattr(os, "getuid"):
    uid = os.getuid()
    print("current uid: ", uid)
if hasattr(os, "getgid"):
    gid = os.getgid()
    print(" gid: ", gid)

#############################################################################

import subprocess

# ret = subprocess.getoutput('date')
# print("rurrent date: ", ret)

import multiprocessing


def do_this(what):
    whoami(what)


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
    whoami("main program")
    for n in range(4):
        process = multiprocessing.Process(target=do_this, args=("I am function %s" % n,))
        process.start()
