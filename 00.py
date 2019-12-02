text = "stressed"
ans =''
for i in range(len(text)):
    ans+=text[len(text)-i-1]

print(ans)

# [start:stop:step]
ans2 = text[::-1]
print(ans2)