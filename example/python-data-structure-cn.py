'''
第三章：递归

1.整数的进制转换
将一个整数转换为一个二进制和十六进制字符串
这里用base，表示任意进制
'''
def jinzhi_Convert(num:int,base:int) -> str:
    base_str = '0123456789ABCDEF'
    if num < base:
        return base_str[num]
    return jinzhi_Convert(num//base,base) + base_str[num%base]

# res = jinzhi_Convert(4,2)
# print(res)

#改非递归：DIY
def notR_jinzhi_Convert1(num,base) -> str:
    stk = []
    base_str = '0123456789ABCDEF'
    if num < 0:
        return False
    if num < base:
        return base_str[num]
    a = num//base
    res = base_str[num%base]
    stk.append(a)
    while stk:
        b = stk.pop()
        res = base_str[b%base] + res
        if b // base > 0:
            a = b // base
            stk.append(a)
        else:
            return res


#书上的写法：变量少，逻辑清晰，更细理解
def notR_jinzhi_Convert2(num,base) -> str:
    stk = []
    base_str = '0123456789ABCDEF'
    while num > 0:
        if num < base:
            stk.append(base_str[num])
        else:
            stk.append(base_str[num%base])
        num //= base
    res = ''
    while stk:
        res += stk.pop()
    return res


res = notR_jinzhi_Convert2(4,2)
print(res)

