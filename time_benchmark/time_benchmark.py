#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import time

class Benchmark():
    def __init__(self):
        self.time_wall_start = time.time()
        self.time_cpu_start = time.clock()

    def diff_time_wall_secs(self):
        return (time.time() - self.time_wall_start)

    def print_time(self, fptr):
        print(file=fptr)
        print("Benchmark  wall=%.3fm  cpu=%.3fm" % (
            self.diff_time_wall_secs() / 60.0,
            (time.clock() - self.time_cpu_start) / 60.0,
            ), 
            file=fptr)


