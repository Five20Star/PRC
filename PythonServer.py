# coding=utf-8
'''
Created on 2013-9-22

@author: hanqunfeng
'''

import sys
import time
from servicePy import Processor
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.server import TServer


import socket
# 实现类
class PythonServiceServer:
     def get(self, id):
         time.sleep(5)
         print socket.gethostbyname(socket.gethostname())
         return "get=="+str(id)
     
handler = PythonServiceServer()
# 注册实现类
processor = Processor(handler)
transport = TSocket.TServerSocket('192.168.1.19',30303)
tfactory = TTransport.TBufferedTransportFactory()
# pfactory = TBinaryProtocol.TBinaryProtocolFactory()
pfactory = TCompactProtocol.TCompactProtocolFactory()

#server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
server = TServer.TForkingServer(processor, transport, tfactory, pfactory)
print "Starting python server..."
server.serve()
print "done!"    
