from ._version import get_versions
from .data import read_ulog

__version__ = get_versions()['version']
del get_versions

__all__ = ['read_ulog', '__version__']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
