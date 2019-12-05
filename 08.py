# -*- coding: utf-8 -*-
def cipher(target):
    result = ''
    for c in target:
        if c.islower():
            result += chr(219-ord(c))
        else:
            result += c
    
    return result

target = " I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(target)
result = cipher(target)
print('暗号化:' + result)

# 復号化
result2 = cipher(result)
print('復号化:' + result2)

# 復号化で元に戻っているかチェック
if result2 != target:
    print('元に戻っていない！？')