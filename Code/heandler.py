"""
==========
Author:TT
Time:2021/2/4  4:09 下午
Project: py30
Company:自动化测试
==========
"""

class Headler:
    def testHeadler(self,username=None,pwd=None):
        if username !=None and pwd !=None:
            if username =="python30" and pwd =="11111":
                code= {"msg":"登陆成功"}
                return code
            else:
                code = {"msg":"登陆失败"}
                return code
        else:
            code = {"msg": "所有参数不能为空"}
            return code
