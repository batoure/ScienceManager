from subprocess import Popen, PIPE


class bteqFactory(object):
    """ A factory to execute BTEQ scripts """
    def __init__(self):
        pass

    def exec_module(self, file, args=None):
        #'var/tpt/export_data.txt'
        #'var/tpt/import_data.txt'
        p = Popen(['tbuild', '-f', file], stdout=PIPE, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            if line.decode("utf-8") == '[1] "Exit(0)"\r\n':
                print('error has been raised')
                p.kill()
                break
            print(line.decode("utf-8")),
        p.communicate() # close p.stdout, wait for the subprocess to exit
        return True