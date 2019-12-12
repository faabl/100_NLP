import itertools
with open('col1.txt') as col1,open('col2.txt') as col2,\
    open('merge.txt',mode='w')as merge:
    for c1,c2 in zip(col1,col2):
        merge.write(c1.rstrip()+'\t'+c2.rstrip()+'\n')
        # print(c1.rstrip()+'\t'+c2.rstrip())


# with open('col1.txt') as col1_file, \
#         open('col2.txt') as col2_file, \
#         open('merge.txt', mode='w') as out_file:

#     for col1_line, col2_line in zip(col1_file, col2_file):
#         out_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')
