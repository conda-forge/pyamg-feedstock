import sys

print("sys.platform = ", sys.platform)
print("sys.version = ", sys.version)

import pyamg
pyamg.test(verbose=False)
