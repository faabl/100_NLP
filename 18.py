import sys

def  main():
    if len(sys.argv) <= 1:
        print("ファイル名を入れてください")
        return -1
    file_name=sys.argv[1]
    
    with open(file_name) as f:
        lines=f.readlines()
    
    #入力は文字列のため，keyを数字に変換後，sort
    lines.sort(key= lambda line : float(line.split('\t')[2]),reverse=True)
    
    for tmp in lines:
        print(tmp,end='')


if __name__ == "__main__":
    main()