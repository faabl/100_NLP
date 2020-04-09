# -*- coding: utf-8 -*-
# どうやら日本語を認識しないらしい


def n_gram(target,n):
    result=[]
    for index in range(len(target)-n+1): #3の場合の時のbi-gramは[0,1]の二つ
        result.append(target[index:index+n])
    return result


def check(target, word):
    for tmp in target:
        if tmp == word:
            return True

    return False


input1 = "paraparaparadise"
input2 = "paragraph"

bi_1 = set(n_gram(input1, 2))
print('X : ' + str(bi_1))

bi_2 = set(n_gram(input2, 2))
print('Y : ' + str(bi_2))

print((bi_1 or bi_2))
print("積集合 : " + str(bi_1 and bi_2))
print("差集合 : " + str(bi_1 - bi_2))
print((check(bi_1, "se")))
# print("se" in bi_1)
print(check(bi_2, "se"))