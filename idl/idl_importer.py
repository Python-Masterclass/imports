import importlib.machinery
import importlib.util
import sys
from pathlib import Path
import dataclasses

from idl_parser import parse_idl


class IdlImporter(importlib.machinery.PathFinder):
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
                spec = importlib.util.spec_from_file_location(leaf_name, filepath, loader=cls())
                return spec
                # create_python_module(leaf_name, p)

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        with open(module.__spec__.origin) as f:
            data = f.read()
        class_name, attributes = parse_idl(data)
        datacls = dataclasses.make_dataclass(class_name, attributes)
        setattr(module, class_name, datacls)



sys.meta_path.insert(0, IdlImporter)
