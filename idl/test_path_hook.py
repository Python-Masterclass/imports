import sys

import path_hook
print(sys.path_importer_cache)

import result_data
# from result_data import ResultData

x = result_data.ResultData(1, "hallo", 3.14)
print(x)
