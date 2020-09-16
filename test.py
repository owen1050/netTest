import os

stream = os.popen("ping -c 1 8.8.8.8")
out = stream.read()
print(out)
