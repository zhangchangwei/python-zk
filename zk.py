from kazoo.client import KazooClient

# from urllib import parse
import urllib
import sys
from urlparse import urlparse



zk = KazooClient(hosts='xxx.xxx.xxx.xxx:2181')
zk.start()
node = zk.get_children('/dubbo')
# print('node:', node)


ip_list=[]
for i in node:
    pro = zk.get_children('/dubbo/'+i+'/providers')
    if len(pro) != 0:
        urldata = urllib.unquote(pro[0])

        result = urlparse(urldata)
        ip_list.append(result.netloc)

port = sys.argv[1]

for i in ip_list:
    if port in i:
        print(i.split(':')[0])

zk.stop()
