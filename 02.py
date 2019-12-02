from functools import reduce
input1 = "パトカー"
input2 = "タクシー"
ans = ""
for i in range(len(input1)):
    ans += input1[i]+input2[i]
print(ans)

result = "".join(reduce(lambda x,y: x+y,zip(input1,input2)))
print(result)

#from functools import reduce
# 高階関数　reduce(func,iter,initializer)
#zip 複数のリストをforで回したい時