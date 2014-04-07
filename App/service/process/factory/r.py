from subprocess import Popen, PIPE


class Process(object):
    """ A service to execute external applications """
    def __init__(self, log):
        self.log = log

    def x_module(self, args, file):
        #'var/R/helloWorld.R'
        p = Popen(['Rscript', file], stdout=PIPE, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            if line.decode("utf-8") == '[1] "Exit(0)"\r\n':
                print('error has been raised')
                p.kill()
                break
            print(line.decode("utf-8")),
        p.communicate() # close p.stdout, wait for the subprocess to exit
        return True