from __future__ import unicode_literals

__all__ = ['VERSION', '__version__']

VERSION = (1, 2, 1, 'alpha', 0)

__version__ = ".".join([str(x) for x in VERSION][:3])
