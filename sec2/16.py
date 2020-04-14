import math
import sys

fname = 'hightemp.txt'
args = sys.argv
#これやったら「長さがたりない」って出るで
# if args[1] is None :
#     print("ないよ")

if len(sys.argv) >= 2:
    n = int(args[1])
else :
    n = int(input('N--> '))

with open(fname) as data_file:
    lines = data_file.readlines()

count=len(lines)
unit = math.ceil(count / n)


for i,offset in enumerate(range(0,count,unit),1):
    with open('child_{:02d}.txt'.format(i), mode='w') as out_file:
        for line in lines[offset:offset + unit]:
            out_file.write(line)



# import math

# fname = 'hightemp.txt'
# n = int(input('N--> '))

# with open(fname) as data_file:
#     lines = data_file.readlines()

# count = len(lines)
# unit = math.ceil(count / n)  # 1ファイル当たりの行数


# for i, offset in enumerate(range(0, count, unit), 1): #enumerate(個数，スタート番号)
#     with open('child_{:02d}.txt'.format(i), mode='w') as out_file:
#         for line in lines[offset:offset + unit]:
#             out_file.write(line)