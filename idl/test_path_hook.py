import sys

import path_hook
print(sys.path_importer_cache)

import interface
# from result_data import ResultData

x = interface.ResultData(1, "hallo", 3.14)
print(x)
