input1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
input2=input1.split()
ans=map((lambda x: len(x)- x.count(',') - x.count('.')),input2)
print(list(ans))

