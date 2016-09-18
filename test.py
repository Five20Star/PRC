# -*- coding: utf8 -*-
# code by Shurrik
import threading, time, httplib
from servicePy import Client
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

HOST = "192.168.1.19"; #主机地址 例如192.168.1.101
PORT = 30303 #端口
TOTAL = 0 #总数
SUCC = 0 #响应成功数
FAIL = 0 #响应失败数
EXCEPT = 0 #响应异常数
MAXTIME=0 #最大响应时间
MINTIME=100 #最小响应时间，初始值为100秒
GT3=0 #统计3秒内响应的
LT3=0 #统计大于3秒响应的
# 创建一个 threading.Thread 的派生类
class RequestThread(threading.Thread):
    # 构造函数
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.test_count = 0

    # 线程运行的入口函数
    def run(self):

        self.test_performace()


    def test_performace(self):
            global TOTAL
            global SUCC
            global FAIL
            global EXCEPT
            global GT3
            global LT3
            transport = None
            try:
                st = time.time()
                transport = TSocket.TSocket('192.168.1.19', 30303)
                transport = TTransport.TBufferedTransport(transport)
                protocol = TCompactProtocol.TCompactProtocol(transport)
                client = Client(protocol)
                transport.open()
                result = client.get(100)
                print "The return value is : "
                print client.get(100)
                print "............"
                start_time
                if result:
                    TOTAL+=1
                    SUCC+=1
                else:
                    TOTAL+=1
                    FAIL+=1
                time_span = time.time()-st
                print '%s:%f\n'%(self.name,time_span)
                self.maxtime(time_span)
                self.mintime(time_span)
                if time_span>3:
                    GT3+=1
                else:
                    LT3+=1
            except Thrift.TException, tx:
                print '%s' % (tx.message)            
                TOTAL+=1
                EXCEPT+=1
            transport.close()
    def maxtime(self,ts):
            global MAXTIME
            print ts
            if ts>MAXTIME:
                MAXTIME=ts
    def mintime(self,ts):
            global MINTIME
            if ts<MINTIME:
                MINTIME=ts
        
# main 代码开始
print '===========task start==========='
# 开始的时间
start_time = time.time()
# 并发的线程数
thread_count = 100

i = 0
while i <= thread_count:
    t = RequestThread("thread" + str(i))
    t.start()
    i += 1
t=0
#并发数所有都完成或大于50秒就结束
while TOTAL<thread_count|t>50:
        t+=1
        time.sleep(1)
print '===========task end==========='
print "total:%d,succ:%d,fail:%d,except:%d"%(TOTAL,SUCC,FAIL,EXCEPT)
print 'response maxtime:',MAXTIME
print 'response mintime',MINTIME
print 'great than 3 seconds:%d,percent:%0.2f'%(GT3,float(GT3)/(TOTAL or 1))
print 'less than 3 seconds:%d,percent:%0.2f'%(LT3,float(LT3)/(TOTAL or 1))

