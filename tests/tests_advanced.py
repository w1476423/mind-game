import os, sys

path=os.path.abspath(__file__)

# print(path)

fd=os.path.dirname(path)

# print(fd)

directoryName=os.path.dirname(fd)

# print(directoryName)

modulePath=os.path.join(directoryName,'src')

print(modulePath)

#sets the path. equivalent of set PYTHONPATH='src'
sys.path.append(modulePath)


import edugame.api
