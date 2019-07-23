"""
在这里添加各种自定义的断言，断言失败抛出AssertionError就OK。
"""

def assertHTTPCode(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error

def assertStr(response,l,r,e ):
    par = response.partition(l)
    res=(par[2].partition(r))[0][:]
    if res!=e:
        raise AssertionError('断言失败，字符串:'+res+'与预期结果:'+e+'不符')

def cut(str,l,r ):
    par = str.partition(l)
    res=(par[2].partition(r))[0][:]
    return res