from abc import ABC
from enum import Enum


class Verbosity(Enum):
    OFF = 0
    NORMAL = 1
    VERBOSE = 2
    DEBUG = 3

class Outputter(ABC):
    def __init__(self, printfn, verbosityfn):
        self.printfn = printfn
        self.verbosityfn = verbosityfn

    def check(self, verbosity):
        return self.verbosityfn().value >= verbosity.value

    def poutput(self, msg, end='\n', verbosity=Verbosity.NORMAL):
        if self.check(verbosity):
            self.printfn(msg + end)

    def poutput_normal(self, msg, end='\n'):
        self.poutput(msg, end, verbosity=Verbosity.NORMAL)

    def poutput_verbose(self, msg, end='\n'):
        self.poutput(msg, end, verbosity=Verbosity.VERBOSE)

    def poutput_debug(self, msg, end='\n'):
        self.poutput(msg, end, verbosity=Verbosity.DEBUG)