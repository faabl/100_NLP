def main():
    fname = 'hightemp.txt'
    ans=set()
    with open(fname) as data_file:
        for line in data_file:
            cols=line.split("\t")
            ans.add(cols[0])

    # シェルと比較のため，ソート
    #しようと思ったけど，"sort"コマンドと並びが異なる...漢字の扱いかいが違う?
    # ans=sorted(ans)
    # print(ans)
    for tmp in ans:
        print(tmp)


if __name__ == "__main__":
    main()