from multiprocessing import Process
import time


class MyProcess(Process):
    def init(self, loop):
        Process.init(self)
        self.loop = loop
