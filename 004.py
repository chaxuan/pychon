import os
os.chdir("D:\数据\python数据")

def main():#定义主界面函数
    print("*"*50)
    print("欢迎进入密码薄管理系统")
    print("*" * 50)
    print("1.增加网址和密码")
    print("2.删除网址和密码")
    print("3.修改网址和密码")
    print("4.查询网址和密码")

#main()

def add_book():
    f = open("baocun.txt",'w')
    web = input("请输入网址：")+'\n'
    password = input("请输入密码：")
    f.write(web)
    f.write(password)
    f.close()
#add_book()

def del_book():
    book = ""
    f = open("baocun.txt",'r')
    web = input("请输入网址：")
    password = input("请输入密码：")
    fr = f.read()
    f.close()
    #print(type(fr))
    if web in fr and password in fr:
        f1 = open("baocun.txt", 'w')
        f1.write(book)
        f1.close()
        print("删除成功")
    else:
        print("未找到对应网址或密码，请检查后重试")
#del_book()

def change_book():
    f = open("baocun.txt", 'r')
    web = input("请输入旧网址：")
    password = input("请输入旧密码：")
    fr = f.read()
    f.close()
    # print(type(fr))
    if web in fr and password in fr:
        f1 = open("baocun.txt", 'w')
        new_web = input("请输入新网址：") + '\n'
        new_password = input("请输入新密码：")
        f1.write(new_web)
        f1.write(new_password)
        f.close()
        print("更改成功")
    else:
        print("未找到对应网址或密码，请检查后重试")
#change_book()

def seek_book():
    f = open("baocun.txt", 'r')
    web = input("请输入网址：")
    password = input("请输入密码：")
    fr = f.read()
    f.close()
    if web in fr and password in fr:
        print("已找到：\n",fr)
    else:
        print("未找到对应网址或密码，请检查后重试")
#seek_book()

main()
while True:
    num = input("请输入操作指令：\n")
    num = int(num)
    if num == 1:
        add_book()
    elif num == 2:
        del_book()
    elif num == 3:
        change_book()
    elif num == 4:
        seek_book()
#print("输入错误，请重新输入")