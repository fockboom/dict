from socket import *
import sys

class Handle:
    def __init__(self):
        self.server_address=('127.0.0.1',16464)
        self.sock=self.connect()


    def  connect(self):
        sock=socket()
        sock.connect(self.server_address)
        return sock

    def do_login(self):
        self.sock.send(b'test')


    def do_exit(self):
        self.sock.send(b'E')
        self.sock.close()
        sys.exit("谢谢使用")





#与用户交互

class DICTView:
    def __init__(self):
        self.handle=Handle()

    def menu_2(self):

        while True:
            print(
                """
                ==============登录界面==========
                1.查单词    2.历史记录    3.注销
                """
            )
            cmd = input("请输入选项：")
            if cmd == '1':
                pass
            elif cmd == '2':
                pass
            elif cmd == '3':
                break
            else:
                print("请输入正确选项！")

    def menu_1(self):
        while True:
            print(
                """
                ==============登录界面==========
                1.登录    2.注册    3.退出
                """
            )
            cmd = input("请输入选项：")
            if cmd == '1':
                self.handle.do_login()
                self.menu_2()
            elif cmd == '2':
                pass
            elif cmd == '3':
                self.handle.do_exit()
            else:
                print("请输入正确选项！")

    def main(self):
        self.menu_1()

if __name__=='__main__':
    dict_server=DICTView()
    dict_server.main()
