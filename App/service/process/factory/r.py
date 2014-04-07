from subprocess import Popen, PIPE


class rFactory(object):
    """ A factory to execute CRAN scripts """
    def __init__(self, log):
        self._log = log
        pass

    def exec_module(self, file, args=None):
        #'var/R/helloWorld.R'
        p = Popen(['Rscript', file], stdout=PIPE, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            if line.decode("utf-8") == '[1] "Exit(0)"\r\n':
                self._log.warn('error has been raised')
                p.kill()
                break
            self._log.info(line.decode("utf-8")),
        p.communicate() # close p.stdout, wait for the subprocess to exit
        return True