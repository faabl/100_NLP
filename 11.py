file_name="hightemp.txt"
with open(file_name) as f:
    for tmp in f:
        print(tmp.replace('\t',' '),end='')

