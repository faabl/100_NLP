# def n_gram(target,n):
#     result = []

#     for index,tmp in enumerate(target):
#         if(index == len(target)-n+1):
#             break
#         result.append(target[index:index+n])

#     return result


# input = "I am an NLPer"
# char_gram = n_gram(input,2)
# print(char_gram)

# input2 = input.split()
# word_gram = n_gram(input2,2)
# print(word_gram)

def n_gram(target,n):
    result=[]
    for index in range(len(target)-n+1): #3の場合の時のbi-gramは[0,1]の二つ
        result.append(target[index:index+n])
    return result

input = "I am an NLPer"
#単語bi-gram
w_input=input.split(" ")
ans1= n_gram(w_input,2)
print(ans1)

#文字bi-gram スペース含むbigram
ans2 = n_gram(input,2)
print(ans2)