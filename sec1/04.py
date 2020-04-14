input = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num_first_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
input2 = input.split()
ans = {}
for index,tmp in enumerate(input2):
    if (index+1) in num_first_only: #インデックス＋１しないとずれる
        ans[input2[index][0:1]] = index
    else:
        ans[input2[index][0:2]] = index

print(ans)