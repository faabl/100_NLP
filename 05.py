def n_gram(target,n):
    result = []

    for index,tmp in enumerate(target):
        if(index == len(target)-n+1):
            break
        result.append(target[index:index+n])

    return result


input = "I am an NLPer"
char_gram = n_gram(input,2)
print(char_gram)

input2 = input.split()
word_gram = n_gram(input2,2)
print(word_gram)