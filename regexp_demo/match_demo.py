import re


def test():
    import re
    pattern = re.compile(r'^\d+', flags=re.MULTILINE)
    text = '123\n456\n789'
    result = pattern.findall(text)
    print(result)  # 输出: ['123', '456', '789']

# 测试正则表达
# 1.单引号、双引号、三引号都是可以用来匹配的
# 2.match只能从字符串的开头开始匹配，search能匹配整个字符串
# 3.^和$只能匹配字符串的开头和结尾，原始需要匹配的字符串，例如'hello world',这个原始字符串^h,d$才行
if __name__ == '__main__':
    line = 'url("https://helloworld.com")'
    line = '''url("https://turing.captcha.qcloud.com/cap_union_new_getcapbysig?img_index=1&image=02790500009f324100000015123e98223928&sess=s0OoVMNbRoHImihkilE5pgpgW_xbgggEqqe-Tc87Aby_ftET0ztNPjnomALZoc0vkvwN9Q1uqIiSO0BrHjxAwWcWp79nd64yXAhsD_AKT_PtGGlE7ysZcUbw4qBIdTOgM_k1icrvRXnTG0l9BislteT5Dx8YSW62msAzKcFkuAPuhW4PO8WHk_dJcPskpPyDAP4X43UAhggsOAkN1b1uB-JisyMlH21TS1iAe1RBo4xqAbh1ZiNFQaqmZ3qmKhPsscg5oQRepHXIZ3tRJh5daPF1UCTKNgoqi93i8Gsf4dK_6u2UsI22-UMx1i6HDQ2Eyv3l5s6W_Dra8q1EaQ9xcYRO-hNMHl9mSmKNoqaFbu5Lgu5tngCDF1JVE_S_5xYBBT")'''
    # match匹配
    matchObj = re.match(r'u', line, re.M | re.I)
    if matchObj:
        print("match匹配（只能匹配原始字符串开头，匹配不到开头，就返回空）: ", matchObj.group())
    else:
        print("match没有匹配内容")

    # sarch匹配,匹配url=https://helloworld.com
    # 注意，这个^使用必须是从字符串开头匹配，例如^u,就能匹配成功，^h就会失败;$的使用也是类似的
    # 感觉^和$基本没有作用
    matchObj = re.search(r'https.*\"', line, re.M | re.I)
    if matchObj:
        print("search（全字符串匹配）: ", matchObj.group())
    else:
        print("search没有匹配内容")

    test()
