from socket import *
from multiprocessing import Process
from dict_db import *

class Handle(Process):
    def __init__(self,conn):
        self.conn=conn
        super().__init__()
        self.db=Dictdata()

    def run(self):
        while True:
            request=self.conn.recv(1024)
            if not request or request==b'E':
                break

        self.db.close()
        self.conn.close()


class Dict_server:
    def __init__(self,host='',port=0):
        self.host=host
        self.port=port
        self.address=(host,port)
        self.sock=self.create_socket()

    def create_socket(self):
        sock=socket()
        sock.bind(self.address)
        return sock

    #启动服务
    def server_forever(self):
        self.sock.listen(5)
        print("LISTEN THE PORT %d" % self.port)
        #循环连接客户端
        while True:
            conn,addr=self.sock.accept()
            print("Ccnnect from",addr)
            #自定义进程类创建进程
            p=Handle(conn)
            p.start()


if __name__=='__main__':
    dict_server=Dict_server(host='0.0.0.0',port=16464)
    dict_server.server_forever()