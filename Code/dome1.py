"""
==========
Author:TT
Time:2021/2/1  5:58 下午
Project: py30
Company:自动化测试
==========
"""
#不可变类型 数字  布尔值 字符串
#列表：可变类型，可增删改

# list_python30 =["111","2222",2222,True,90]

#添加数据
# #追加在末尾，列表.append()
# list_python30.append("chsicihs")
# print(list_python30)
#
# #
# #插队
# list_python30.insert(2,"chsicihs")
# print(list_python30)
#
# #合并 列表1 .extend(列表) ：将列表2追加到列表1
# new_list=["chjkkbbn","dfghjklkjhnbvcdtyu"]
# list_python30.extend(new_list)
# print(list_python30)
#
# #修改列表数据
# list_python30[2]="0985678"
# print(list_python30)


# #拼接，反序 reverse
# new_list=["chjkkbbn","dfghjklkjhnbvcdtyu","qw","qwert","gd","123456uytrew"]
# # ss="".join(new_list)
# # print(ss.upper())
# # print(new_list)
# # ss.reverse()
# # print(ss)
# # print(" ".join(ss))
# for item in range(len(new_list)):
#     print(item)
#     print(new_list)
#

#乘法表
#
# for index in range(1,5):
#     print("")  #换行
#     print("第{}行".format(index))
#     for item in range(1,index+1):
#         print(item,end="  ")
#
#

from Code.heandler import Headler
import unittest

class TestCode(unittest.TestCase):
    def test_login(self):
        res = Headler().testHeadler("python30","11111")
        self.assertEqual(res,{"登陆成功"})










