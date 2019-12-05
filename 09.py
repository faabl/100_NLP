import random

origin = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

sep = origin.split()
ans=[]
for tmp in sep:
    tmp2 = tmp
    if len(tmp) > 5:
        # tmp2 = tmp[0] +  ''.join(random.sample(tmp[1:-1], len(tmp)-2)) + tmp[len(tmp)-1] 
        chr_list = list(tmp[1:-1])
        random.shuffle(chr_list)
        tmp2=tmp[0] + ''.join(chr_list) + tmp[-1]
    
    ans.append(tmp2)

print(ans)
    
        
