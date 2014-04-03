import subprocess
#import fabric.api as fabric


class Process(object):
    """ A service to execute external applications """
    def __init__(self, log):
        self.log = log

    def x_module(self, query):
        subprocess.check_output(["ipconfig"])