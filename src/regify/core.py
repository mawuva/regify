"""
Core module for the Regify package.
"""

from threading import RLock
from typing import Any, Callable, Dict, List, Optional


class Registry:
    """Registry thread-safe and extensible."""

    def __init__(self, name: str):
        self.name = name
        self._registry_map: Dict[str, Any] = {}
        self._lock = RLock()

    def _register(self, key: str, obj: Any) -> None:
        """Internal method to register a plugin or object in the registry."""
        with self._lock:
            if key in self._registry_map:
                raise ValueError(f"{self.name}: '{key}' already registered.")
            self._registry_map[key] = obj

    def register(self, key: Optional[str] = None) -> Callable:
        """Decorator to register a plugin or object in the registry."""

        def wrapper(obj: Any) -> Any:
            entry_name = key or obj.__name__
            self._register(entry_name, obj)
            return obj

        return wrapper

    def add(self, key: str, obj: Any) -> None:
        """Explicit addition of an object to the registry."""
        self._register(key, obj)

    def unregister(self, key: str) -> None:
        """Remove an entry from the registry."""
        with self._lock:
            self._registry_map.pop(key, None)

    def get(self, key: str) -> Any:
        """Get an object from the registry."""
        with self._lock:
            return self._registry_map[key]

    def keys(self) -> List[str]:
        """Get all keys in the registry."""
        with self._lock:
            return list(self._registry_map.keys())

    def list(self) -> Dict[str, Any]:
        """List all entries."""
        with self._lock:
            return dict(self._registry_map)

    def clear(self) -> None:
        """Clear the registry."""
        with self._lock:
            self._registry_map.clear()

    def __contains__(self, key: str) -> bool:
        """Check if a key is in the registry."""
        with self._lock:
            return key in self._registry_map

    def __len__(self) -> int:
        """Get the number of entries in the registry."""
        with self._lock:
            return len(self._registry_map)

    def __repr__(self) -> str:
        """Get the string representation of the registry."""
        return f"<Registry name={self.name} size={len(self)}>"
