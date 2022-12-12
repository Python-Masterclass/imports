import importlib.machinery
import sys
from pathlib import Path

from create_python_module import create_python_module


class IdlMetaFinder(importlib.machinery.PathFinder):
    @classmethod
    def find_spec(cls, fullname, path, target=None):
        # print(f"trying: {fullname=}, {path=}")
        if "." in fullname:
            leaf_name = fullname.split(".")[-1]
        else:
            leaf_name = fullname
        if path is None:
            path = sys.path
        for p in path:
            filepath = Path(p) / f"{leaf_name}.idl"
            if filepath.exists():
                create_python_module(leaf_name, p)


sys.meta_path[0:0] = [IdlMetaFinder]
