import gevent
from gevent import monkey

monkey.patch_all()

import socket

hosts = ['www.baidu.com',
         'www.youku.com',
         'www.iqiyi.com']

jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print('gevent: ', job.value)
