import pandas as pd
import numpy as np 
from itertools import groupby
import sys
import time

def main():
    if len(sys.argv) <= 1:
        print("ファイル名を入れてください")
        return -1
    file_name=sys.argv[1]

    # start=time.time()
    #pandasで書いた場合
    #実行時間: 0.03513693809509277
    # data = pd.read_table(file_name,names=('県','都市','温度','ひにち'),header = None)
    # sort_data=data.groupby('県',as_index=False).size().sort_values(ascending=False)
    # for index,num in enumerate(sort_data):
    #     print(sort_data.index[index],'\t',num)
    #pandasを使わない場合
    #実行時間:0.0003020763397216797
    with open(file_name) as f:
        lines = f.readlines()
    
    kens= [line.split('\t')[0] for line in lines]

    kens.sort()
    result = [(ken,len(list(group))) for ken, group in groupby(kens)]
    result.sort(key=lambda ken:ken[1],reverse=True)

    for ken in result:
        print('{ken}\t{count}'.format(ken=ken[0], count=ken[1]))

    # p_time=time.time()-start
    # print(p_time)
    
    
    


if __name__ == "__main__":
    main()