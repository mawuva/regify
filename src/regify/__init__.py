"""
Regify package.

This package provides a thread-safe registry framework for Python objects, plugins, strategies, handlers, or any reusable objects.
"""

from .core import Registry
from .decorators import register
from .manager import RegistryManager

__version__ = "0.0.0"
__all__ = ["Registry", "register", "RegistryManager"]
