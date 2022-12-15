import importlib.machinery
import importlib.util
import sys
from pathlib import Path

from create_python_module import create_python_module


class IdlFileFinder(importlib.machinery.FileFinder):
    def find_spec(self, fullname, target=None):
        print(f"trying: {fullname=}, {self.path=}")
        if "." in fullname:
            leaf_name = fullname.split(".")[-1]
        else:
            leaf_name = fullname

        for p in self.path:
            filepath = Path(p) / f"{leaf_name}.idl"
            if filepath.exists():
                create_python_module(leaf_name, p)
                del sys.path_importer_cache[p]


loader_details = (
    importlib.machinery.SourceFileLoader,
    importlib.machinery.SOURCE_SUFFIXES,
)

sys.path_hooks.insert(0, IdlFileFinder.path_hook(loader_details))
# importlib.invalidate_caches()