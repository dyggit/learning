# _*_ coding:utf-8 _*_

import os
import sys

os.system('clear')

retry_limit = 3
retry_count = 0

account_file = 'account.txt'
lock_file = 'account_lock.txt'

while retry_count < retry_limit:  # 只要重试不超过3次就不断循环
    username = input('请输入用户名：')
    username = username.strip()
    lock_check = open(lock_file)  # 当用户输入用户名后，打开LOCK 文件 以检查是否此用户已经LOCK了

    for line in lock_check.readlines():  # 循环LOCK文件
        if username == line.strip('\n'):  # 去掉换行符
            sys.exit('用户名 %s 已经被锁定，退出' % username)  # 如果LOCK了就直接退出
    password = raw_input('\033[32;41mPassword:\033[0m')  # 输入密码

    f = open(account_file, 'r')  # 打开帐号文件
    match_flag = False  # 默认为Flase,如果用户match 上了，就设置为 True

    for line in f.readlines():
        user, passwd = line.strip('\n').split()  # 去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user,passwd两个变量
        if username == user and password == passwd:  # 判断用户名和密码是否都相等
            print('hello, %s !!' % username)
            match_flag = True  # 相等就把循环外的match_flag变量改为了True
            break  # 然后就不用继续循环了，直接 跳出，因为已经match上了
    f.close()

    if match_flag == False:  # 如果match_flag还为False,代表上面的循环中跟本就没有match上用户名和密码，所以需要继续循环
        print('sorry,%s is unmatched' % username)
        retry_count += 1  # 计数器加1
    else:
        print('wlecome login my learning system!')
        break  # 用户成功登录，退出脚本

else:
    print("you account %s is locked!!!" % username)
    g = open(lock_file, 'a')
    g.write(username)  # 被锁用户追加到用户锁文件
    g.write('\n')
    g.close()
