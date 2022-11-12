# while True:
#     print(
#         """
#         ==============登录界面==========
#         1.登录    2.注册    3.退出
#         """
#     )
#     cmd=input("请输入选项：")
#     if cmd=='1':
#         pass
#     elif  cmd=='2':
#         pass
#     elif cmd=='3':
#         break
#     else:
#         print("请输入正确选项！")
#
#
# while True:
#     print(
#         """
#         ==============登录界面==========
#         1.查单词    2.历史记录    3.注销
#         """
#     )
#     cmd=input("请输入选项：")
#     if cmd=='1':
#         pass
#     elif cmd=='2':
#         pass
#     elif cmd=='3':
#         break
#     else:
#         print("请输入正确选项！")


##############################ver2######################
def menu_2():
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

def menu_1():
    while True:
        print(
            """
            ==============登录界面==========
            1.登录    2.注册    3.退出
            """
        )
        cmd=input("请输入选项：")
        if cmd=='1':
            menu_2()
        elif  cmd=='2':
            pass
        elif cmd=='3':
            break
        else:
            print("请输入正确选项！")

if __name__ == '__main__':
    menu_1()



