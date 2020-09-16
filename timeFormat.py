import time
print(time.time())
t = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
i0 = t.find()