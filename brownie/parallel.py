# coding: utf-8
"""
    brownie.parallel
    ~~~~~~~~~~~~~~~~

    Implements useful parallelization stuff.

    :copyright: 2010 by Daniel Neuhaeuser
    :license: BSD, see LICENSE.rst for details
"""
import os

try:
    from multiprocessing import cpu_count as get_cpu_count
except ImportError:
    def get_cpu_count(default=None):
        try:
            cpu_count = os.sysconf('SC_NPROCESSORS_ONLN')
            if cpu_count >= 1:
                return cpu_count
        except AttributeError, ValueError:
            # availability is restricted to unix
        if default is not None:
            return default
        raise NotImplementedError()

get_cpu_count.__doc__ = """
Returns the number of available processors on this machine.

If default is ``None`` and the number cannot be determined a
:exc:`NotImplementedError` is raised.
"""