# _*_ coding:utf-8 _*_


def myint(s):
    # if str.isdigit(s):
    #     s = int(s)
    # else:
    #     s = s.decode('utf-8')
    # return s
    try:
        eval(s)
    except NameError:
        return s
    except SyntaxError:
        return s
    else:
        return eval(s)

a = raw_input("请输入：")

print (myint(a))
