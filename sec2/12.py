file_name="hightemp.txt"
col1 = []
col2=[]
with open(file_name) as f:
    for tmp  in f:
        tmp2 = tmp.split('\t')
        col1.append(tmp2[0])
        col2.append(tmp2[1])


with open('col1.txt', mode='w') as col1_file, \
    open('col2.txt', mode='w') as col2_file:

    for tmp in range(len(col1)):
        col1_file.write(col1[tmp]+'\n')
        col2_file.write(col2[tmp]+'\n')


# '\'を用いると行を跨いでかけるよ

#fname = 'hightemp.txt'
# with open(fname) as data_file, \
#         open('col1.txt', mode='w') as col1_file, \
#         open('col2.txt', mode='w') as col2_file:
#     for line in data_file:
#         cols = line.split('\t')
#         col1_file.write(cols[0] + '\n')
#         col2_file.write(cols[1] + '\n')