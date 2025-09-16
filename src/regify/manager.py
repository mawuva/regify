"""
Manager module for the Regify package.
"""

from typing import Dict

from regify.core import Registry


class RegistryManager:
    """Centralize multiple registries for a project."""

    def __init__(self) -> None:
        self._registries: Dict[str, Registry] = {}

    def create_registry(self, name: str) -> Registry:
        """Create a new registry."""
        if name in self._registries:
            raise ValueError(f"Registry '{name}' already exists.")
        registry = Registry(name)
        self._registries[name] = registry
        return registry

    def get_registry(self, name: str) -> Registry:  # type: ignore
        """Get a registry."""
        return self._registries[name]

    def all(self) -> Dict[str, Registry]:
        """Get all registries."""
        return dict(self._registries)

    def __repr__(self) -> str:
        """Get the string representation of the registry manager."""
        return f"<RegistryManager registries={list(self._registries.keys())}>"
