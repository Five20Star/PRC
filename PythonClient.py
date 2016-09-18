# coding=utf-8

from servicePy import Client
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

def pythonServerExe():
    try:
        # transport = TSocket.TSocket('localhost', 30303)
        transport = TSocket.TSocket('192.168.1.19', 30303)  
        transport = TTransport.TBufferedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)
        transport.open()
        print "The return value is : " 
        print client.get(100)
        print "............"
        transport.close()
    except Thrift.TException, tx:
        print '%s' % (tx.message)
        
        
if __name__ == '__main__':
    pythonServerExe()
